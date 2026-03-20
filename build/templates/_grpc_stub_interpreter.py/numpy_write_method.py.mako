<%page args="f, config, method_template"/>\
## numpy_read and numpy_write use the same logic - both support gRPC with complex number handling when needed
<%include file="/_grpc_stub_interpreter.py/numpy_read_method.py.mako" args="f=f, config=config, method_template=method_template" />\
