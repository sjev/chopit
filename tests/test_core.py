"""
test core functionality
"""


import pytest
import yaml
from pathlib import Path

CWD = Path(__file__).parents[1].absolute()


def test_config():
    """ test configuration file load """
    cfg_file = CWD / 'content/chopit.yml'
    print('-------------------')
    print('config file: ', cfg_file)
    assert cfg_file.exists(), 'config file not found'

    cfg = yaml.load(cfg_file.open(), Loader=yaml.FullLoader)

    print('Got config:', cfg)