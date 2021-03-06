# Stubs for antlr4.Token (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

class Token:
    INVALID_TYPE = ...  # type: int
    EPSILON = ...  # type: int
    MIN_USER_TOKEN_TYPE = ...  # type: int
    EOF = ...  # type: int
    DEFAULT_CHANNEL = ...  # type: int
    HIDDEN_CHANNEL = ...  # type: int
    source = ...  # type: Any
    type = ...  # type: Any
    channel = ...  # type: Any
    start = ...  # type: Any
    stop = ...  # type: Any
    tokenIndex = ...  # type: Any
    line = ...  # type: Any
    column = ...  # type: Any
    def __init__(self) -> None: ...
    @property
    def text(self): ...
    @text.setter
    def text(self, text): ...
    def getTokenSource(self): ...
    def getInputStream(self): ...

class CommonToken(Token):
    EMPTY_SOURCE = ...  # type: Any
    source = ...  # type: Any
    type = ...  # type: Any
    channel = ...  # type: Any
    start = ...  # type: Any
    stop = ...  # type: Any
    tokenIndex = ...  # type: int
    line = ...  # type: Any
    column = ...  # type: Any
    def __init__(self, source: Any = ..., type: Optional[Any] = ..., channel: Any = ..., start: int = ..., stop: int = ...) -> None: ...
    def clone(self): ...
    @property
    def text(self): ...
    @text.setter
    def text(self, text): ...
