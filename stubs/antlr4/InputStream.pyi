# Stubs for antlr4.InputStream (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
import unittest

class InputStream:
    name = ...  # type: str
    strdata = ...  # type: Any
    def __init__(self, data) -> None: ...
    @property
    def index(self): ...
    @property
    def size(self): ...
    def reset(self): ...
    def consume(self): ...
    def LA(self, offset): ...
    def LT(self, offset): ...
    def mark(self): ...
    def release(self, marker): ...
    def seek(self, _index): ...
    def getText(self, start, stop): ...

class TestInputStream(unittest.TestCase):
    def testStream(self): ...