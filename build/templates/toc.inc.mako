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

   ${module_name}/class
% if len(config['repeated_capabilities']) > 0:
   ${module_name}/rep_caps
% endif
% if len(enums) > 0:
   ${module_name}/enums
% endif
   ${module_name}/errors
   ${module_name}/examples
% if grpc_supported:
   ${module_name}/grpc_session_options
% endif

