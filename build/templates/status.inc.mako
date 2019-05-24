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
table_contents.append(['{0} ({1})'.format(driver_name, module_name), '', ])
table_contents.append(['Driver Version Tested Against', config['latest_runtime_version_tested_against']])
table_contents.append(['Driver API Version', config['api_version']])
table_contents.append(['PyPI Version', '|{0}LatestVersion|'.format(module_name)])
table_contents.append(['Supported Python Version', '|{0}PythonVersion|'.format(module_name)])
table_contents.append(['Open Issues', '|{0}OpenIssues|'.format(module_name)])
table_contents.append(['Open Pull Requests', '|{0}OpenPRs|'.format(module_name)])

driver_status_table = helper.as_rest_table(table_contents, header=True)

%>
${helper.get_rst_header_snippet(driver_name + ' Python API Status', '-')}

${helper.get_indented_docstring_snippet(driver_status_table, indent=0)}


${helper.get_rst_picture_reference('{0}LatestVersion'.format(module_name), 'http://img.shields.io/pypi/v/{0}.svg'.format(module_name), 'Latest {0} Version'.format(driver_name), 'http://pypi.python.org/pypi/{0}'.format(module_name), indent=0)}

${helper.get_rst_picture_reference('{0}PythonVersion'.format(module_name), 'http://img.shields.io/pypi/pyversions/{0}.svg'.format(module_name), '{0} supported Python versions'.format(driver_name), 'http://pypi.python.org/pypi/{0}'.format(module_name), indent=0)}

${helper.get_rst_picture_reference('{0}OpenIssues'.format(module_name), 'https://img.shields.io/github/issues/ni/nimi-python/{0}.svg'.format(module_name), 'Open Issues + Pull Requests for {0}'.format(driver_name), 'https://github.com/ni/nimi-python/issues?q=is%3Aopen+is%3Aissue+label%3A{0}'.format(module_name), indent=0)}

${helper.get_rst_picture_reference('{0}OpenPRs'.format(module_name), 'https://img.shields.io/github/issues-pr/ni/nimi-python/{0}.svg'.format(module_name), 'Pull Requests for {0}'.format(driver_name), 'https://github.com/ni/nimi-python/pulls?q=is%3Aopen+is%3Aissue+label%3A{0}'.format(module_name), indent=0)}

