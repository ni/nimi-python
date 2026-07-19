from pathlib import Path
from types import SimpleNamespace

from mako.template import Template


def _render_rep_caps(config):
    repo_root = Path(__file__).resolve().parents[2]
    template_path = repo_root / 'build' / 'templates' / 'rep_caps.rst.mako'
    template = Template(filename=str(template_path))
    metadata = SimpleNamespace(config=config)
    return template.render(template_parameters={'metadata': metadata})


def test_rep_caps_template_uses_custom_documentation_overrides():
    config = {
        'module_name': 'nifake',
        'c_function_prefix': 'niFake_',
        'repeated_capabilities': [
            {
                'prefix': 'res',
                'python_name': 'resources',
                'documentation': {
                    'description': 'Resource repeated capabilities use fully-qualified identifiers.',
                    'auto_prefix_addition_supported': False,
                    'valid_identifiers': ['dev0/res0', 'dev0/res1'],
                    'examples': [
                        "session.resources['dev0/res0'].channel_enabled = True",
                        "session.resources['dev0/res1'].channel_enabled = True",
                    ],
                },
            }
        ],
    }

    rendered = _render_rep_caps(config)

    assert 'Resource repeated capabilities use fully-qualified identifiers.' in rendered
    assert "Valid identifiers: :python:`'dev0/res0, dev0/res1'`." in rendered
    assert "session.resources['dev0/res0'].channel_enabled = True" in rendered
    assert "session.resources['dev0/res1'].channel_enabled = True" in rendered

    # Generic auto-prefix guidance should be suppressed when override disables it.
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
            }
        ],
    }

    rendered = _render_rep_caps(config)

    assert 'If no prefix is added to the items in the parameter' in rendered
    assert "session.channels['0-2'].channel_enabled = True" in rendered
    assert "'channel0, channel1, channel2'" in rendered
