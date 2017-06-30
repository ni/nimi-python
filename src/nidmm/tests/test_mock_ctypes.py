import nidmm

import pytest

from unittest.mock import ANY
from unittest.mock import sentinel
from unittest.mock import call
from unittest.mock import Mock
from unittest.mock import patch

import ctypes


def expectingLibraryCalls(*names):
    def real_decorator(testMethod):
        testMethod.names = list(names)
        return testMethod
    return real_decorator


class TestSession(object):
    def setup_method(self, method):
        additionalFunctions = getattr(method, 'names', [])
        self.MockLibrary = Mock(spec = ['niDMM_InitWithOptions'] + additionalFunctions)

        # Set up the patches
        patched_get_library = patch('nidmm.session.library.get_library', return_value=self.MockLibrary)
        patched_get_library.start()
        self.errors_patcher = patch('nidmm.session.errors._handle_error')
        self.MockHandleError = self.errors_patcher.start()
        types_patcher = patch('nidmm.session.ctypes_types.ViSession_ctype')
        MockSession = types_patcher.start()
        ctypes_patcher = patch('nidmm.session.ctypes.pointer', return_value=sentinel)
        MockSessionPointer = ctypes_patcher.start()

        # Configure the Mock calls
        self.MockLibrary.niDMM_InitWithOptions.return_value = sentinel

        # Construct the session
        # @TODO: test the forwarding of the parameters
        self.session = nidmm.Session('dev1')

        # Test the calls executed in the constructor
        assert MockSessionPointer.mock_calls == [call(MockSession.return_value)]
        assert self.MockLibrary.niDMM_InitWithOptions.mock_calls == [call(ANY, ANY, ANY, ANY, sentinel)]
        assert self.MockHandleError.mock_calls == [call(ANY, sentinel)]

        # Cleanup the setup code
        self.MockLibrary.reset_mock()
        self.MockHandleError.reset_mock()
        patched_get_library.stop()  # Nobody should be calling get_library() anymore
        types_patcher.stop()  # ditto
        ctypes_patcher.stop()  # ditto

    def teardown_method(self, method):
        self.errors_patcher.stop()

    @expectingLibraryCalls('niDMM_close')
    def test_close(self):
        self.MockLibrary.niDMM_close.return_value = 0
        viBefore = self.session.vi
        self.session.close()
        assert self.MockLibrary.niDMM_close.mock_calls == [call(viBefore)]

    def test_enter_justReturnsSession(self):
        assert self.session.__enter__() is self.session

    def test_exit_justCallsClose(self):
        with patch.object(self.session, 'close') as MockCloseMethod:
            self.session.__exit__(None, None, None)
            assert MockCloseMethod.call_count == 1

    @expectingLibraryCalls('niDMM_reset')
    def test_reset(self):
        self.session.reset()
        assert self.MockLibrary.niDMM_reset.mock_calls == [call(self.session.vi)]
        assert self.MockHandleError.mock_calls == [call(self.session, self.MockLibrary.niDMM_reset.return_value)]
