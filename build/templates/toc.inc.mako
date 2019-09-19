<%
    import build.helper as helper

    config = template_parameters['metadata'].config
    module_name = config['module_name']
    enums = config['enums']
%>\
API Reference
--------------

.. toctree::

   ${module_name}/class
% if len(enums) > 0:
   ${module_name}/enums
% endif
   ${module_name}/errors
   ${module_name}/examples

