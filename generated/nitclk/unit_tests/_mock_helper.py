# -*- coding: utf-8 -*-
# This file was generated
import sys  # noqa: F401   - Not all mock_helpers will need this


class MockFunctionCallError(Exception):
    def __init__(self, function, param=None):
        self.function = function
        self.param = param
        msg = "{0} called without setting side_effect".format(self.function)
        if param is not None:
            msg += " or setting the {0} parameter return value".format(self.param)
        super(Exception, self).__init__(msg)


class SideEffectsHelper(object):
    def __init__(self):
        self._defaults = {}
        self._defaults['ConfigureForHomogeneousTriggers'] = {}
        self._defaults['ConfigureForHomogeneousTriggers']['return'] = 0
        self._defaults['FinishSyncPulseSenderSynchronize'] = {}
        self._defaults['FinishSyncPulseSenderSynchronize']['return'] = 0
        self._defaults['GetAttributeViReal64'] = {}
        self._defaults['GetAttributeViReal64']['return'] = 0
        self._defaults['GetAttributeViReal64']['value'] = None
        self._defaults['GetAttributeViSession'] = {}
        self._defaults['GetAttributeViSession']['return'] = 0
        self._defaults['GetAttributeViSession']['value'] = None
        self._defaults['GetAttributeViString'] = {}
        self._defaults['GetAttributeViString']['return'] = 0
        self._defaults['GetExtendedErrorInfo'] = {}
        self._defaults['GetExtendedErrorInfo']['return'] = 0
        self._defaults['GetExtendedErrorInfo']['errorString'] = None
        self._defaults['Initiate'] = {}
        self._defaults['Initiate']['return'] = 0
        self._defaults['IsDone'] = {}
        self._defaults['IsDone']['return'] = 0
        self._defaults['IsDone']['done'] = None
        self._defaults['SetAttributeViReal64'] = {}
        self._defaults['SetAttributeViReal64']['return'] = 0
        self._defaults['SetAttributeViSession'] = {}
        self._defaults['SetAttributeViSession']['return'] = 0
        self._defaults['SetAttributeViString'] = {}
        self._defaults['SetAttributeViString']['return'] = 0
        self._defaults['SetupForSyncPulseSenderSynchronize'] = {}
        self._defaults['SetupForSyncPulseSenderSynchronize']['return'] = 0
        self._defaults['Synchronize'] = {}
        self._defaults['Synchronize']['return'] = 0
        self._defaults['SyncronizeToSyncPulseSender'] = {}
        self._defaults['SyncronizeToSyncPulseSender']['return'] = 0
        self._defaults['WaitUntilDone'] = {}
        self._defaults['WaitUntilDone']['return'] = 0

    def __getitem__(self, func):
        return self._defaults[func]

    def __setitem__(self, func, val):
        self._defaults[func] = val

    def niTClk_ConfigureForHomogeneousTriggers(self, session_count, sessions):  # noqa: N802
        if self._defaults['ConfigureForHomogeneousTriggers']['return'] != 0:
            return self._defaults['ConfigureForHomogeneousTriggers']['return']
        return self._defaults['ConfigureForHomogeneousTriggers']['return']

    def niTClk_FinishSyncPulseSenderSynchronize(self, session_count, sessions, min_time):  # noqa: N802
        if self._defaults['FinishSyncPulseSenderSynchronize']['return'] != 0:
            return self._defaults['FinishSyncPulseSenderSynchronize']['return']
        return self._defaults['FinishSyncPulseSenderSynchronize']['return']

    def niTClk_GetAttributeViReal64(self, session, channel_name, attribute_id, value):  # noqa: N802
        if self._defaults['GetAttributeViReal64']['return'] != 0:
            return self._defaults['GetAttributeViReal64']['return']
        # value
        if self._defaults['GetAttributeViReal64']['value'] is None:
            raise MockFunctionCallError("niTClk_GetAttributeViReal64", param='value')
        if value is not None:
            value.contents.value = self._defaults['GetAttributeViReal64']['value']
        return self._defaults['GetAttributeViReal64']['return']

    def niTClk_GetAttributeViSession(self, session, channel_name, attribute_id, value):  # noqa: N802
        if self._defaults['GetAttributeViSession']['return'] != 0:
            return self._defaults['GetAttributeViSession']['return']
        # value
        if self._defaults['GetAttributeViSession']['value'] is None:
            raise MockFunctionCallError("niTClk_GetAttributeViSession", param='value')
        if value is not None:
            value.contents.value = self._defaults['GetAttributeViSession']['value']
        return self._defaults['GetAttributeViSession']['return']

    def niTClk_GetAttributeViString(self, session, channel_name, attribute_id, buf_size, value):  # noqa: N802
        if self._defaults['GetAttributeViString']['return'] != 0:
            return self._defaults['GetAttributeViString']['return']
        return self._defaults['GetAttributeViString']['return']

    def niTClk_GetExtendedErrorInfo(self, error_string, error_string_size):  # noqa: N802
        if self._defaults['GetExtendedErrorInfo']['return'] != 0:
            return self._defaults['GetExtendedErrorInfo']['return']
        if self._defaults['GetExtendedErrorInfo']['errorString'] is None:
            raise MockFunctionCallError("niTClk_GetExtendedErrorInfo", param='errorString')
        if error_string_size.value == 0:
            return len(self._defaults['GetExtendedErrorInfo']['errorString'])
        try:
            error_string_ref = error_string.contents
        except AttributeError:
            error_string_ref = error_string
        for i in range(len(self._defaults['GetExtendedErrorInfo']['errorString'])):
            error_string_ref[i] = self._defaults['GetExtendedErrorInfo']['errorString'][i]
        return self._defaults['GetExtendedErrorInfo']['return']

    def niTClk_Initiate(self, session_count, sessions):  # noqa: N802
        if self._defaults['Initiate']['return'] != 0:
            return self._defaults['Initiate']['return']
        return self._defaults['Initiate']['return']

    def niTClk_IsDone(self, session_count, sessions, done):  # noqa: N802
        if self._defaults['IsDone']['return'] != 0:
            return self._defaults['IsDone']['return']
        # done
        if self._defaults['IsDone']['done'] is None:
            raise MockFunctionCallError("niTClk_IsDone", param='done')
        if done is not None:
            done.contents.value = self._defaults['IsDone']['done']
        return self._defaults['IsDone']['return']

    def niTClk_SetAttributeViReal64(self, session, channel_name, attribute_id, value):  # noqa: N802
        if self._defaults['SetAttributeViReal64']['return'] != 0:
            return self._defaults['SetAttributeViReal64']['return']
        return self._defaults['SetAttributeViReal64']['return']

    def niTClk_SetAttributeViSession(self, session, channel_name, attribute_id, value):  # noqa: N802
        if self._defaults['SetAttributeViSession']['return'] != 0:
            return self._defaults['SetAttributeViSession']['return']
        return self._defaults['SetAttributeViSession']['return']

    def niTClk_SetAttributeViString(self, session, channel_name, attribute_id, value):  # noqa: N802
        if self._defaults['SetAttributeViString']['return'] != 0:
            return self._defaults['SetAttributeViString']['return']
        return self._defaults['SetAttributeViString']['return']

    def niTClk_SetupForSyncPulseSenderSynchronize(self, session_count, sessions, min_time):  # noqa: N802
        if self._defaults['SetupForSyncPulseSenderSynchronize']['return'] != 0:
            return self._defaults['SetupForSyncPulseSenderSynchronize']['return']
        return self._defaults['SetupForSyncPulseSenderSynchronize']['return']

    def niTClk_Synchronize(self, session_count, sessions, min_time):  # noqa: N802
        if self._defaults['Synchronize']['return'] != 0:
            return self._defaults['Synchronize']['return']
        return self._defaults['Synchronize']['return']

    def niTClk_SyncronizeToSyncPulseSender(self, session_count, sessions, min_time):  # noqa: N802
        if self._defaults['SyncronizeToSyncPulseSender']['return'] != 0:
            return self._defaults['SyncronizeToSyncPulseSender']['return']
        return self._defaults['SyncronizeToSyncPulseSender']['return']

    def niTClk_WaitUntilDone(self, session_count, sessions, timeout):  # noqa: N802
        if self._defaults['WaitUntilDone']['return'] != 0:
            return self._defaults['WaitUntilDone']['return']
        return self._defaults['WaitUntilDone']['return']

    # Helper function to setup Mock object with default side effects and return values
    def set_side_effects_and_return_values(self, mock_library):
        mock_library.niTClk_ConfigureForHomogeneousTriggers.side_effect = MockFunctionCallError("niTClk_ConfigureForHomogeneousTriggers")
        mock_library.niTClk_ConfigureForHomogeneousTriggers.return_value = 0
        mock_library.niTClk_FinishSyncPulseSenderSynchronize.side_effect = MockFunctionCallError("niTClk_FinishSyncPulseSenderSynchronize")
        mock_library.niTClk_FinishSyncPulseSenderSynchronize.return_value = 0
        mock_library.niTClk_GetAttributeViReal64.side_effect = MockFunctionCallError("niTClk_GetAttributeViReal64")
        mock_library.niTClk_GetAttributeViReal64.return_value = 0
        mock_library.niTClk_GetAttributeViSession.side_effect = MockFunctionCallError("niTClk_GetAttributeViSession")
        mock_library.niTClk_GetAttributeViSession.return_value = 0
        mock_library.niTClk_GetAttributeViString.side_effect = MockFunctionCallError("niTClk_GetAttributeViString")
        mock_library.niTClk_GetAttributeViString.return_value = 0
        mock_library.niTClk_GetExtendedErrorInfo.side_effect = MockFunctionCallError("niTClk_GetExtendedErrorInfo")
        mock_library.niTClk_GetExtendedErrorInfo.return_value = 0
        mock_library.niTClk_Initiate.side_effect = MockFunctionCallError("niTClk_Initiate")
        mock_library.niTClk_Initiate.return_value = 0
        mock_library.niTClk_IsDone.side_effect = MockFunctionCallError("niTClk_IsDone")
        mock_library.niTClk_IsDone.return_value = 0
        mock_library.niTClk_SetAttributeViReal64.side_effect = MockFunctionCallError("niTClk_SetAttributeViReal64")
        mock_library.niTClk_SetAttributeViReal64.return_value = 0
        mock_library.niTClk_SetAttributeViSession.side_effect = MockFunctionCallError("niTClk_SetAttributeViSession")
        mock_library.niTClk_SetAttributeViSession.return_value = 0
        mock_library.niTClk_SetAttributeViString.side_effect = MockFunctionCallError("niTClk_SetAttributeViString")
        mock_library.niTClk_SetAttributeViString.return_value = 0
        mock_library.niTClk_SetupForSyncPulseSenderSynchronize.side_effect = MockFunctionCallError("niTClk_SetupForSyncPulseSenderSynchronize")
        mock_library.niTClk_SetupForSyncPulseSenderSynchronize.return_value = 0
        mock_library.niTClk_Synchronize.side_effect = MockFunctionCallError("niTClk_Synchronize")
        mock_library.niTClk_Synchronize.return_value = 0
        mock_library.niTClk_SyncronizeToSyncPulseSender.side_effect = MockFunctionCallError("niTClk_SyncronizeToSyncPulseSender")
        mock_library.niTClk_SyncronizeToSyncPulseSender.return_value = 0
        mock_library.niTClk_WaitUntilDone.side_effect = MockFunctionCallError("niTClk_WaitUntilDone")
        mock_library.niTClk_WaitUntilDone.return_value = 0
