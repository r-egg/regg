from typing import Literal
import re


# NOTE: ref: https://github.com/python/cpython/blob/main/Lib/sre_parse.py
class Regg:
    """
    This class achieves a random sampling from the domain defined by the regex

    args:
      - regex(str): A regular expression you wanna define as a domain
    """

    def __init__(self, regex: str):
        self._regex = regex
        self._parsed = re.sre_parse.parse(self._regex)
        print(self._parsed)

    def __str__(self):
        return f'<Regg regex: {self._regex}>'

    def __call__(self, mode: Literal['normal', 'abnormal'] = 'normal'):
        return 0  # FIXME: insert value generator here

    @property
    def regex(self):
        return self._regex


if __name__ == '__main__':
    regg = Regg('[0-9]')
    print(regg.regex)
    print(regg)
    print(regg())
