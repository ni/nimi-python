# This file was generated
<%
    import build.helper as helper

    config            = template_parameters['metadata'].config
    attributes        = helper.filter_codegen_attributes(config['attributes'])
    functions         = config['functions']

    module_name       = config['module_name']
    c_function_prefix = config['c_function_prefix']

    functions = helper.filter_codegen_functions(functions)

    close_function_name = helper.camelcase_to_snakecase(config['close_function'])
%>\

import ${module_name}._library_interpreter as _library_interpreter
import ${module_name}.errors as errors

# Used for __repr__ and __str__
import pprint

pp = pprint.PrettyPrinter(indent=4)


class AttributeViInt32(object):

    def __init__(self, owner, attribute_id, index):
        self._owner = owner
        self._index = index
        self._attribute_id = attribute_id

    def __getitem__(self, index):
        return self._owner._get_installed_device_attribute_vi_int32(self._index, self._attribute_id)


class AttributeViString(object):

    def __init__(self, owner, attribute_id, index):
        self._owner = owner
        self._index = index
        self._attribute_id = attribute_id

    def __getitem__(self, index):
        return self._owner._get_installed_device_attribute_vi_string(self._index, self._attribute_id)


class _Device(object):

    # This is needed during __init__. Without it, __setattr__ raises an exception
    _is_frozen = False

    def __init__(self, owner, index):
        self._index = index
% for attribute in helper.sorted_attrs(attributes):
        self.${attributes[attribute]['name'].lower()} = Attribute${attributes[attribute]['type']}(owner, ${attribute}, index=index)
%   if 'documentation' in attributes[attribute]:
        '''
        ${helper.get_documentation_for_node_docstring(attributes[attribute], config, indent=4)}
        '''
%   endif
% endfor
        self._param_list = 'owner=' + pp.pformat(owner) + ', index=' + pp.pformat(index)
        self._is_frozen = True

    def __repr__(self):
        return '{0}.{1}({2})'.format('${module_name}', self.__class__.__name__, self._param_list)

    def __str__(self):
        ret_str = self.__repr__() + ':\n'
% for attribute in helper.sorted_attrs(attributes):
        ret_str += '    ${attributes[attribute]['name'].lower()} = ' + pp.pformat(self.${attributes[attribute]['name'].lower()}) + '\n'
% endfor
        return ret_str

    def __getattribute__(self, name):
        if name in ['_is_frozen', 'index', '_param_list', '__class__', '__name__', '__repr__', '__str__', '__setattr__', ]:
            return object.__getattribute__(self, name)
        else:
            return object.__getattribute__(self, name).__getitem__(None)

    def __setattr__(self, name, value):
        if self._is_frozen:
            raise AttributeError("__setattr__ not supported.")
        object.__setattr__(self, name, value)


class _DeviceIterable(object):
    def __init__(self, owner, count):
        self._current_index = 0
        self._owner = owner
        self._count = count
        self._param_list = 'owner=' + pp.pformat(owner) + ', count=' + pp.pformat(count)
        self._is_frozen = True

    def _get_next(self):
        if self._current_index + 1 > self._count:
            raise StopIteration
        else:
            dev = _Device(self._owner, self._current_index)
            self._current_index += 1
            return dev

    def next(self):
        return self._get_next()

    def __next__(self):
        return self._get_next()

    def __repr__(self):
        return '{0}.{1}({2})'.format('${module_name}', self.__class__.__name__, self._param_list)

    def __str__(self):
        ret_str = self.__repr__() + ':\n'
        ret_str += '    current index = {0}'.format(self._current_index)
        return ret_str


class Session(object):
    '''${config['session_class_description']}'''

    # This is needed during __init__. Without it, __setattr__ raises an exception
    _is_frozen = False

    def __init__(self, driver):
        self._item_count = 0
        self._current_item = 0
        self._library_interpreter = _library_interpreter.LibraryInterpreter('windows-1251')
        self._library_interpreter._${config['session_handle_parameter_name']}, self._item_count = self._open_installed_devices_session(driver)
        self._param_list = "driver=" + pp.pformat(driver)

        self.devices = []
        for i in range(self._item_count):
            self.devices.append(_Device(self, i))

        self._is_frozen = True

    def __repr__(self):
        return '{0}.{1}({2})'.format('${module_name}', self.__class__.__name__, self._param_list)

    def __str__(self):
        ret_str = self.__repr__() + ':\n'
        for i in range(self._item_count):
            ret_str += str(_Device(self, i)) + '\n'
        return ret_str

    def __setattr__(self, key, value):
        if self._is_frozen and key not in dir(self):
            raise AttributeError("__setattr__ not supported.")
        object.__setattr__(self, key, value)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    # Iterator functions
    def __len__(self):
        return self._item_count

    def __iter__(self):
        return _DeviceIterable(self, self._item_count)

    def close(self):
        try:
            self._${close_function_name}()
        except errors.DriverError:
            self._library_interpreter._${config['session_handle_parameter_name']} = 0
            raise
        self._library_interpreter._${config['session_handle_parameter_name']} = 0

    ''' These are code-generated '''
% for func_name in sorted(functions):
% for method_template in functions[func_name]['method_templates']:

<%include file="${'/session.py' + method_template['session_filename'] + '.py.mako'}" args="f=functions[func_name], config=config, method_template=method_template" />\
% endfor
% endfor
