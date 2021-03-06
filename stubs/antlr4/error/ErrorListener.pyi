# Stubs for antlr4.error.ErrorListener (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

class ErrorListener:
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e): ...
    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs): ...
    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs): ...
    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs): ...

class ConsoleErrorListener(ErrorListener):
    INSTANCE = ...  # type: Any
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e): ...

class ProxyErrorListener(ErrorListener):
    delegates = ...  # type: Any
    def __init__(self, delegates) -> None: ...
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e): ...
    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs): ...
    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs): ...
    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs): ...
