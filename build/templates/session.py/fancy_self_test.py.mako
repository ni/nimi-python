<%page args="f, config, method_template"/>\
<%
    '''Call self-test and throw if there is a failure'''
    import build.helper as helper
    lock_indent = '    ' if f['use_session_lock'] else ''
    lock_indent_num = 4 if f['use_session_lock'] else 0
%>\
    def ${f['python_name']}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}):
        '''${f['python_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''
% if f['use_session_lock']:
        with self.lock():
% endif
        ${lock_indent}code, msg = self._self_test()
        ${lock_indent}if code:
        ${lock_indent}    raise errors.SelfTestError(code, msg)
        ${lock_indent}return None

