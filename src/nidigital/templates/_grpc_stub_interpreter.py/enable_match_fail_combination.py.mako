## This file is empty. We won't support gRPC, for now.
## Even though gRPC Device supports the function, the nisync Python API lacks gRPC support, so there's no point.
## If a user tries to call enable_match_fail_combination with a session runing on a gRPC Device Server, they will get an error
## because the method does not exist in _grpc_stub_interpreter.py.
## Most likely it will be an AttributeError, though it hasn't been tested.