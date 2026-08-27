from pathlib import Path
from tempfile import TemporaryDirectory
from types import SimpleNamespace

from build.generate_template import generate_template
from build.helper.metadata_add_all import add_all_config_metadata


def _render_rep_caps(config):
    repo_root = Path(__file__).resolve().parents[2]
    template_path = repo_root / 'build' / 'templates' / 'rep_caps.rst.mako'
    metadata = SimpleNamespace(config=add_all_config_metadata(config))
    with TemporaryDirectory() as temp_dir:
        output_path = Path(temp_dir) / 'rep_caps.rst'
        generate_template(str(template_path), {'metadata': metadata}, str(output_path))
        return output_path.read_text()


def test_custom_documentation_overwrites_rep_caps_template_defaults():
    config = {
        'module_name': 'nifake',
        'c_function_prefix': 'niFake_',
        'repeated_capabilities': [
            {
                'prefix': 'res',
                'python_name': 'resources',
                'documentation': {
                    'description': 'Resource repeated capabilities use fully-qualified identifiers.',
                    'valid_indices': ['dev0/res0', 'dev0/res1'],
                    'examples': [
                        {
                            'code': (
                                "session.resources['dev0/res0'].channel_enabled = True\n"
                                "session.resources['dev0/res1'].channel_enabled = True"
                            ),
                            'description': (
                                'The first line enables resource 0.\n'
                                'The second line enables resource 1.'
                            ),
                        },
                        {
                            'code': "session.resources['dev0/res2'].channel_enabled = True",
                            'description': '',
                        },
                    ],
                },
            }
        ],
    }

    rendered = _render_rep_caps(config)

    assert 'Resource repeated capabilities use fully-qualified identifiers.' in rendered
    assert "Valid Indices: :python:`'dev0/res0, dev0/res1'`." in rendered
    assert "session.resources['dev0/res0'].channel_enabled = True" in rendered
    assert "session.resources['dev0/res1'].channel_enabled = True" in rendered
    assert "session.resources['dev0/res2'].channel_enabled = True" in rendered
    assert 'The first line enables resource 0.' in rendered
    assert 'The second line enables resource 1.' in rendered

    # Custom documentation should override the generic auto-prefix guidance.
    assert 'If no prefix is added to the items in the parameter' not in rendered
    assert "session.resources['0-2'].channel_enabled = True" not in rendered
    assert "'res0, res1, res2'" not in rendered


def test_rep_caps_template_preserves_default_prefixed_behavior():
    config = {
        'module_name': 'nifake',
        'c_function_prefix': 'niFake_',
        'repeated_capabilities': [
            {
                'prefix': 'channel',
                'python_name': 'channels',
            },
            {
                'prefix': '',
                'python_name': 'instruments',
            }
        ],
    }

    rendered = _render_rep_caps(config)

    assert 'If no prefix is added to the items in the parameter' in rendered
    assert "session.channels['0-2'].channel_enabled = True" in rendered
    assert "'channel0, channel1, channel2'" in rendered
    example_description = (
        "        passes a string of :python:`'channel0, channel1, channel2'` to the set attribute function."
    )
    assert rendered.count(example_description) == 2
    assert '\n    passes a string' not in rendered
    assert "set attribute function.\n\n\ninstruments\n" in rendered
    assert rendered.endswith('\n\n\n\n')
    assert not any(line.isspace() for line in rendered.splitlines())


def test_rep_caps_template_expands_default_documentation_fields():
    config = {
        'module_name': 'nifake',
        'c_function_prefix': 'niFake_',
        'repeated_capabilities': [
            {
                'prefix': 'channel',
                'python_name': 'channels',
                'documentation': {
                    'description': 'Custom channel documentation.',
                },
            }
        ],
    }

    rendered = _render_rep_caps(config)

    assert 'Custom channel documentation.' in rendered
    assert "session.channels['channel0-channel2'].channel_enabled = True" in rendered
    assert "'channel0, channel1, channel2'" in rendered
