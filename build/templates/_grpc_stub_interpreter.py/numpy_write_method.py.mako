<%page args="f, config, method_template"/>\
## numpy_read and numpy_write are identical for gRPC -- both return a NotImplementedError
<%include file="/_grpc_stub_interpreter.py/numpy_read_method.py.mako" args="f=f, config=config, method_template=method_template" />\
