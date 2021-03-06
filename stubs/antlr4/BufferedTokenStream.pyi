# Stubs for antlr4.BufferedTokenStream (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

Lexer = ...  # type: Any

class TokenStream: ...

class BufferedTokenStream(TokenStream):
    tokenSource = ...  # type: Any
    tokens = ...  # type: Any
    index = ...  # type: int
    fetchedEOF = ...  # type: bool
    def __init__(self, tokenSource) -> None: ...
    def mark(self): ...
    def release(self, marker): ...
    def reset(self): ...
    def seek(self, index): ...
    def get(self, index): ...
    def consume(self): ...
    def sync(self, i): ...
    def fetch(self, n): ...
    def getTokens(self, start, stop, types: Optional[Any] = ...): ...
    def LA(self, i): ...
    def LB(self, k): ...
    def LT(self, k): ...
    def adjustSeekIndex(self, i): ...
    def lazyInit(self): ...
    def setup(self): ...
    def setTokenSource(self, tokenSource): ...
    def nextTokenOnChannel(self, i, channel): ...
    def previousTokenOnChannel(self, i, channel): ...
    def getHiddenTokensToRight(self, tokenIndex, channel: int = ...): ...
    def getHiddenTokensToLeft(self, tokenIndex, channel: int = ...): ...
    def filterForChannel(self, left, right, channel): ...
    def getSourceName(self): ...
    def getText(self, interval: Optional[Any] = ...): ...
    def fill(self): ...
