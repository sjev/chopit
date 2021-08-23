"""
test core functionality
"""
#pylint: disable=protected-access



from pathlib import Path
from chopit.core import MD_Parser, is_separator, parse_meta


config_file = Path(__file__).parents[1].absolute() / 'content/chopit.yml'


def test_parser():
    """ test md file parser """

    assert config_file.exists(), 'config file not found'
    parser = MD_Parser(config_file)

    assert parser._cfg['index']['template'] == 'index.html'

    blocks = parser.parse_section('index')
    print(blocks)
    assert len(blocks) == 2

    assert blocks[0]['name'] == 'block_1'
    assert blocks[1]['lang'] == 'en'



def test_sep():
    """ test sep block detection """
    assert is_separator('---')
    assert is_separator('--- ')
    assert is_separator('--- \n')
    assert is_separator('---\n')
    assert not is_separator('# Heading')

def test_meta():
    """ test metadata parsting """

    k,v = parse_meta('foo: bar   \n')
    assert k== 'foo'
    assert v == 'bar'