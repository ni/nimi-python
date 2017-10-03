<%
    import build.helper as helper

    config        = template_parameters['metadata'].config
    module_name = config['module_name']

    import os

    examples_dir = os.path.join('src', module_name, 'examples')
    examples = [f for f in os.listdir(examples_dir) if os.path.isfile(os.path.join(examples_dir, f)) and f.endswith('.py')]
    examples = sorted(examples)
%>\
${helper.get_rst_header_snippet('Examples', '=')}

% for e in examples:
${helper.get_rst_header_snippet(e, '-')}

.. literalinclude:: ${os.path.join('..', '..', examples_dir, e).replace('\\', '/')}
   :language: python
   :linenos:
   :encoding: utf8
   :caption: `(${e}) <https://github.com/ni/nimi-python/blob/master/src/${module_name}/examples/${e}>`_

% endfor
