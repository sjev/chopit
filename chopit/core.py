"""
core functionality for *chopit*

"""
from typing import Tuple

from pathlib import Path
import yaml


def is_separator(line: str) -> bool:
    """ check if line is a separator """
    if line.strip() == '---':
        return True

    return False

def parse_meta(line: str) -> Tuple:
    """ parse key-value tuple"""

    parts = line.strip().split(':')
    return (parts[0].strip(),parts[1].strip())


class MD_Parser:
    """
    parser for markdown files.
    extracts blocks and parses them with Jijja2
    """

    def __init__(self, cfg_file: Path):
        """[summary]

        Args:
            cfg_file (Path): path to config file
        """

        self._root = cfg_file.parent
        self._cfg = yaml.load(cfg_file.open(), Loader=yaml.FullLoader)

    def parse_section(self,section:str)-> list:
        """parse section of cfg file

        Args:
            section (str): section name, for example 'index'.
        """

        with open(self._root / self._cfg[section]['content'], 'r', encoding='utf-8') as fid:
            lines = fid.readlines()

        blocks = []

        in_meta = False # are we parsing metadata?

        for line in lines:


            if is_separator(line):

                if in_meta: # exiting block
                    blocks.append(data)

                else: # entering block
                    data = {'content':''}

                in_meta = not in_meta
                continue

            if in_meta:
                k,v = parse_meta(line)
                data[k] = v

            if 'data' not in locals(): # wait until first meta is parsed
                continue

            else:
                data['content'] += line

        return blocks







