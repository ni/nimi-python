
build_info = {
    'variables': {
        'driver': 'nimodinst',
    },
    'clean': [
        {'command': 'rmdir', 'params': {'path': '%(OUTPUT_DIR)s/%(driver)s'}}
    ],
    'make': [
        {'command': 'mkdir',
         'params': {'path': '%(OUTPUT_DIR)s/%(driver)s/%(driver)s/tests'}},
        {'command': 'codegen',
         'params': {'template': '%(TEMPLATE_DIR)s/attributes.py.mako',
                    'output_file': '%(OUTPUT_DIR)s/%(driver)s/%(driver)s/attributes.py'},
        },
        {'command': 'codegen',
         'params': {'template': '%(TEMPLATE_DIR)s/enums.py.mako',
                    'output_file': '%(OUTPUT_DIR)s/%(driver)s/%(driver)s/enums.py'},
        },
        {'command': 'codegen',
         'params': {'template': '%(TEMPLATE_DIR)s/library.py.mako',
                    'output_file': '%(OUTPUT_DIR)s/%(driver)s/%(driver)s/library.py'},
        },
        {'command': 'codegen',
         'params': {'template': '%(SOURCE_DIR)s/%(driver)s/templates/session.py.mako',
                    'output_file': '%(OUTPUT_DIR)s/%(driver)s/%(driver)s/session.py'},
        },
        {'command': 'codegen',
         'params': {'template': '%(TEMPLATE_DIR)s/ctypes_library.py.mako',
                    'output_file': '%(OUTPUT_DIR)s/%(driver)s/%(driver)s/ctypes_library.py'},
        },
        {'command': 'codegen',
         'params': {'template': '%(TEMPLATE_DIR)s/errors.py.mako',
                    'output_file': '%(OUTPUT_DIR)s/%(driver)s/%(driver)s/errors.py'},
        },
        {'command': 'codegen',
         'params': {'template': '%(TEMPLATE_DIR)s/__init__.py.mako',
                    'output_file': '%(OUTPUT_DIR)s/%(driver)s/%(driver)s/__init__.py'},
        },
        {'command': 'copy',
         'params': {'src': '%(TEMPLATE_DIR)s/visa2ctypes.py',
                    'dest': '%(OUTPUT_DIR)s/%(driver)s/%(driver)s/ctypes_types.py'},
        },
        {'command': 'copy',
         'params': {'src': '%(TEMPLATE_DIR)s/visa2python.py',
                    'dest': '%(OUTPUT_DIR)s/%(driver)s/%(driver)s/python_types.py'},
        },
        {'command': 'copy',
         'params': {'src': '%(SOURCE_DIR)s/%(driver)s/tests',
                    'dest': '%(OUTPUT_DIR)s/%(driver)s/%(driver)s/tests'},
        },
    ],
    'make_installer': [
        {'command': 'codegen',
         'params': {'template': '%(TEMPLATE_DIR)s/setup.py.mako',
                    'output_file': '%(OUTPUT_DIR)s/%(driver)s/setup.py'},
        },
        {'command': 'copy',
         'params': {'src': 'README.rst',
                    'dest': '%(OUTPUT_DIR)s/%(driver)s/README.rst'},
        },
        {'command': 'setup_test',
         'params': {'src-dir': '%(OUTPUT_DIR)s/%(driver)s'},
        },
        {'command': 'sdist',
         'params': {'src-dir': '%(OUTPUT_DIR)s/%(driver)s'},
        },
        {'command': 'wheel',
         'params': {'src-dir': '%(OUTPUT_DIR)s/%(driver)s'},
        },
    ],
}
