import pytest


def pytest_collection_modifyitems(items):
    '''Ignores initializer deprecation warnings for all nidcpower system tests.'''
    for item in items:
        item.add_marker(pytest.mark.filterwarnings('ignore:Attempting to initialize an independent channels session with a channels argument.:DeprecationWarning'))
        item.add_marker(pytest.mark.filterwarnings('ignore:Initializing session without independent channels enabled.:DeprecationWarning'))
