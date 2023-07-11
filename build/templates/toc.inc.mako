<%
    import build.helper as helper

    config = template_parameters['metadata'].config
    module_name = config['module_name']
    enums = config['enums']
    grpc_supported = template_parameters['include_grpc_support']
%>\
API Reference
--------------

.. toctree::

   class
% if len(config['repeated_capabilities']) > 0:
   rep_caps
% endif
% if len(enums) > 0:
   enums
% endif
   errors
   examples
% if grpc_supported:
   grpc_session_options
% endif

