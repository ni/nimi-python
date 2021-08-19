<%
    import build.helper as helper

    config         = template_parameters['metadata'].config
    module_name    = config['module_name']
    module_version = config['module_version']

    import glob
    import os

    examples_dir = os.path.join('src', module_name, 'examples')
    examples = glob.glob(examples_dir + '/**/*.py', recursive=True)
    examples = sorted(examples)

    # The examples page will show 2 things:
    #   1) URL to zip file containing all examples and in cases like nidigital, support files
    #   2) Code snippet and URL to example file in src folder, for each example
    #
    #  - If there is dev or pre ('a', 'b', 'rc') in module_version then:
    #       - it means code generator is being run during development
    #       - (1) will link to the zip file created during last release and the text will include "..for latest version.."
    #       - (2) will include current code snippet and URL will point to master branch
    #  - Else:
    #       - it means code generator is being run during a release
    #       - (1) will link to the zip file for the current release
    #       - (2) will include current code snippet and URL will point to release version

    with open('./LATEST_RELEASE') as vf:
        latest_release_version = vf.read().strip()
    released_zip_url = 'https://github.com/ni/nimi-python/releases/download/{0}/{1}_examples.zip'.format(latest_release_version, module_name)

    example_url_base = 'https://github.com/ni/nimi-python/blob/'

    from packaging.version import Version
    v = Version(module_version)

    if v.dev is None and v.pre is None:
        examples_zip_url_text = '`You can download all {0} examples here <{1}>`_'.format(module_name, released_zip_url)
        example_url_base += latest_release_version
    else:
        examples_zip_url_text = '`You can download all {0} examples for latest version here <{1}>`_'.format(module_name, released_zip_url)
        example_url_base += 'master'
%>\
${helper.get_rst_header_snippet('Examples', '=')}

${examples_zip_url_text}

% for e in examples:
${helper.get_rst_header_snippet(os.path.basename(e), '-')}

.. literalinclude:: ${os.path.join('..', '..', e).replace('\\', '/')}
   :language: python
   :linenos:
   :encoding: utf8
   :caption: `(${os.path.basename(e)}) <${example_url_base}/${e.replace('\\', '/')}>`_

% endfor
