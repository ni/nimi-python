<%
    import build.helper as helper

    config        = template_parameters['metadata'].config
    module_name = config['module_name']

    import os

    examples_dir = os.path.join('src', module_name, 'examples')
    examples = [f for f in os.listdir(examples_dir) if os.path.isfile(os.path.join(examples_dir, f)) and f.endswith('.py')]
    examples = sorted(examples)

    # If there is no dev or pre ('a', 'b', 'rc'), then the url should link to the (soon to exist) release
    # Otherwise we should just point to master

    # We need to use the global version and not the module version since the release version will match the global version
    # and may not match the module version
    with open('./VERSION') as vf:
        global_version = vf.read().strip()

    from packaging.version import Version
    v = Version(global_version)
    if v.dev is None and v.pre is None:
        url = 'https://github.com/ni/nimi-python/releases/download/{0}/{1}_examples.zip'.format(global_version, module_name)
    else:
        with open('./LATEST_RELEASE') as vf:
            latest_release_version = vf.read().strip()
        url = 'https://github.com/ni/nimi-python/releases/download/{0}/{1}_examples.zip'.format(latest_release_version, module_name)
%>\
${helper.get_rst_header_snippet('Examples', '=')}

`You can download all ${module_name} examples here <${url}>`_

% for e in examples:
${helper.get_rst_header_snippet(e, '-')}

.. literalinclude:: ${os.path.join('..', '..', examples_dir, e).replace('\\', '/')}
   :language: python
   :linenos:
   :encoding: utf8
   :caption: `(${e}) <https://github.com/ni/nimi-python/blob/master/src/${module_name}/examples/${e}>`_

% endfor
