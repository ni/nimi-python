# We need to maintain the version here since it needs to be updated by the build process on GitHub
config_additional_config = {
    # TODO(olsl21): Temporarily disable the new custom_types (#1715), they will be re-enabled in
    #  subsequent smaller PRs
    'custom_types': [],
    # TODO(olsl21): Temporarily add the new DriverTooNewError here as multiple PRs are requiring
    #  official metadata updates and it's difficult to order them correctly with all the PRs
    'extra_errors_used': [
        'InvalidRepeatedCapabilityError',
        'SelfTestError',
        'DriverTooNewError'
    ],
    'module_version': '1.4.2.dev0',
    'latest_runtime_version_tested_against': '21.8.0',
}
