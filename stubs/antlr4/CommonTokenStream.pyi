# Stubs for antlr4.CommonTokenStream (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from antlr4.BufferedTokenStream import BufferedTokenStream

class CommonTokenStream(BufferedTokenStream):
    channel = ...  # type: Any
    def __init__(self, lexer, channel: Any = ...) -> None: ...
    def adjustSeekIndex(self, i): ...
    def LB(self, k): ...
    def LT(self, k): ...
    def getNumberOfOnChannelTokens(self): ...
