
buildinfo = {
    'variables': {
        'driver': 'nidmm',
    },
    'clean': [
        {'command': 'rmdir', 'params': {'path': '%(OUTPUT_DIR)s/%(driver)s'}}
    ],
    'make': [
        {'command': 'mkdir', 'params': {'path': '%(OUTPUT_DIR)s/%(driver)s'}},
        {'command': 'template',
         'params': {'template': '%(TEMPLATE_DIR)s/attributes.py.mako',
                    'output_file': '%(OUTPUT_DIR)s/%(driver)s/attributes.py'},
        },
        {'command': 'template',
         'params': {'template': '%(TEMPLATE_DIR)s/enums.py.mako',
                    'output_file': '%(OUTPUT_DIR)s/%(driver)s/enums.py'},
        },
        {'command': 'template',
         'params': {'template': '%(TEMPLATE_DIR)s/library.py.mako',
                    'output_file': '%(OUTPUT_DIR)s/%(driver)s/library.py'},
        },
        {'command': 'template',
         'params': {'template': '%(TEMPLATE_DIR)s/session.py.mako',
                    'output_file': '%(OUTPUT_DIR)s/%(driver)s/session.py'},
        },
        {'command': 'template',
         'params': {'template': '%(TEMPLATE_DIR)s/errors.py.mako',
                    'output_file': '%(OUTPUT_DIR)s/%(driver)s/errors.py'},
        },
        {'command': 'template',
         'params': {'template': '%(TEMPLATE_DIR)s/__init__.py.mako',
                    'output_file': '%(OUTPUT_DIR)s/%(driver)s/__init__.py'},
        },
    ]
}
