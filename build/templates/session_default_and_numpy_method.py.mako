<%page args="f, config"/>\
<%
    '''Renders a Session method twice, once using the default template and once using the numpy template.'''
%>\
<%include file="/session_default_method.py.mako" args="f=f, config=config" /><%include file="/session_numpy_method.py.mako" args="f=f, config=config" />