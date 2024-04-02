<%
    import build.helper as helper

    config        = template_parameters['metadata'].config
    attributes    = helper.filter_codegen_attributes(config['attributes'])
    functions     = helper.filter_codegen_functions(config['functions'])
    module_name   = config['module_name']
    driver_name   = config['driver_name']
    c_function_prefix = config['c_function_prefix']
%>\
<%
table_contents = []
table_contents.append(['{} ({})'.format(driver_name, module_name), '', ])
table_contents.append(['Driver Version Tested Against', config['latest_runtime_version_tested_against']])
table_contents.append(['PyPI Version', '|{}LatestVersion|'.format(module_name)])
table_contents.append(['Supported Python Version', '|{}PythonVersion|'.format(module_name)])
table_contents.append(['Documentation', '|{}Docs|'.format(module_name)])
table_contents.append(['Open Issues', '|{}OpenIssues|'.format(module_name)])
table_contents.append(['Open Pull Requests', '|{}OpenPRs|'.format(module_name)])

driver_status_table = helper.as_rest_table(table_contents, header=True)

%>
${helper.get_rst_header_snippet(driver_name + ' Python API Status', '-')}

${helper.get_indented_docstring_snippet(driver_status_table, indent=0)}


${helper.get_rst_picture_reference('{}LatestVersion'.format(module_name), 'http://img.shields.io/pypi/v/{}.svg'.format(module_name), 'Latest {} Version'.format(driver_name), 'http://pypi.python.org/pypi/{}'.format(module_name), indent=0)}

${helper.get_rst_picture_reference('{}PythonVersion'.format(module_name), 'http://img.shields.io/pypi/pyversions/{}.svg'.format(module_name), '{} supported Python versions'.format(driver_name), 'http://pypi.python.org/pypi/{}'.format(module_name), indent=0)}

${helper.get_rst_picture_reference('{}Docs'.format(module_name), 'https://readthedocs.org/projects/{}/badge/?version=latest'.format(module_name), '{} Python API Documentation Status'.format(driver_name), 'https://{}.readthedocs.io/en/latest'.format(module_name), indent=0)}

${helper.get_rst_picture_reference('{}OpenIssues'.format(module_name), 'https://img.shields.io/github/issues/ni/nimi-python/{}.svg'.format(module_name), 'Open Issues + Pull Requests for {}'.format(driver_name), 'https://github.com/ni/nimi-python/issues?q=is%3Aopen+is%3Aissue+label%3A{}'.format(module_name), indent=0)}

${helper.get_rst_picture_reference('{}OpenPRs'.format(module_name), 'https://img.shields.io/github/issues-pr/ni/nimi-python/{}.svg'.format(module_name), 'Pull Requests for {}'.format(driver_name), 'https://github.com/ni/nimi-python/pulls?q=is%3Aopen+is%3Aissue+label%3A{}'.format(module_name), indent=0)}

