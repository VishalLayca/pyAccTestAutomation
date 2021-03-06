import pytest

from pytest_bdd import given
from selenium import webdriver


# Constants

DUCKDUCKGO_HOME = 'https://duckduckgo.com/'


# Hooks

def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    print(f'Step failed: {step}')



