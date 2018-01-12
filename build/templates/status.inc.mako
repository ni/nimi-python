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
table_contents.append(['**master branch status**', '|BuildStatus| |Docs| |MITLicense| |CoverageStatus|'])
table_contents.append(['**GitHub status**', '|OpenIssues| |OpenPullRequests|'])

status_table = helper.as_rest_table(table_contents, header=False)

table_contents = []
table_contents.append(['{0} ({1})'.format(driver_name, module_name), '', ])
table_contents.append(['Driver Version Tested Against', ''])
table_contents.append(['PyPI Version', '|{0}LatestVersion|'.format(module_name)])
table_contents.append(['Supported Python Version', '|{0}PythonVersion|'.format(module_name)])
table_contents.append(['Open Issues', '|{0}OpenIssues|'.format(module_name)])

driver_status_table = helper.as_rest_table(table_contents, header=True)

table_contents = []
table_contents.append(['Info', "Python bindings for {0}. See `GitHub <https://github.com/ni/nimi-python/>`_ for the latest source.".format(module_name)])
table_contents.append(['Author', 'National Instruments'])

info_table = helper.as_rest_table(table_contents, header=False)
%>

:orphan:

${helper.get_rst_header_snippet('Project Status', '-')}

${helper.get_indented_docstring_snippet(status_table, indent=0)}

${helper.get_indented_docstring_snippet(info_table, indent=0)}


${helper.get_rst_header_snippet(driver_name + ' Python API Status', '-')}

${helper.get_indented_docstring_snippet(driver_status_table, indent=0)}


${helper.get_rst_picture_reference('BuildStatus', 'https://img.shields.io/travis/ni/nimi-python.svg', 'Build Status - master branch', 'https://travis-ci.org/ni/nimi-python', indent=0)}

${helper.get_rst_picture_reference('Docs', 'https://readthedocs.org/projects/nimi-python/badge/?version=latest', 'Documentation Status - master branch', 'https://nimi-python.readthedocs.io/en/latest/?badge=latest', indent=0)}

${helper.get_rst_picture_reference('MITLicense', 'https://img.shields.io/badge/License-MIT-yellow.svg', 'MIT License', 'https://opensource.org/licenses/MIT', indent=0)}

${helper.get_rst_picture_reference('CoverageStatus', 'https://coveralls.io/repos/github/ni/nimi-python/badge.svg?branch=master&dummy=no_cache_please_1', 'Test Coverage - master branch', 'https://coveralls.io/github/ni/nimi-python?branch=master', indent=0)}

${helper.get_rst_picture_reference('OpenIssues', 'https://img.shields.io/github/issues/ni/nimi-python.svg', 'Open Issues + Pull Requests', 'https://github.com/ni/nimi-python/issues', indent=0)}

${helper.get_rst_picture_reference('OpenPullRequests', 'https://img.shields.io/github/issues-pr/ni/nimi-python.svg', 'Open Pull Requests', 'https://github.com/ni/nimi-python/pulls', indent=0)}

${helper.get_rst_picture_reference('{0}LatestVersion'.format(module_name), 'http://img.shields.io/pypi/v/{0}.svg'.format(module_name), 'Latest {0} Version'.format(driver_name), 'http://pypi.python.org/pypi/{0}'.format(module_name), indent=0)}

${helper.get_rst_picture_reference('{0}PythonVersion'.format(module_name), 'http://img.shields.io/pypi/pyversions/{0}.svg'.format(module_name), '{0} supported Python versions'.format(driver_name), 'http://pypi.python.org/pypi/{0}'.format(module_name), indent=0)}

${helper.get_rst_picture_reference('{0}OpenIssues'.format(module_name), 'https://img.shields.io/github/issues/ni/nimi-python/{0}.svg'.format(module_name), 'Open Issues + Pull Requests for {0}'.format(driver_name), 'https://github.com/ni/nimi-python/issues?q=is%3Aopen+is%3Aissue+label%3A{0}'.format(module_name), indent=0)}

