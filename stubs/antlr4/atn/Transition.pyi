# Stubs for antlr4.atn.Transition (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from antlr4.atn.ATNState import *

ATNState = ...  # type: Any
RuleStartState = ...  # type: Any

class Transition:
    EPSILON = ...  # type: int
    RANGE = ...  # type: int
    RULE = ...  # type: int
    PREDICATE = ...  # type: int
    ATOM = ...  # type: int
    ACTION = ...  # type: int
    SET = ...  # type: int
    NOT_SET = ...  # type: int
    WILDCARD = ...  # type: int
    PRECEDENCE = ...  # type: int
    serializationNames = ...  # type: Any
    serializationTypes = ...  # type: Any
    target = ...  # type: Any
    isEpsilon = ...  # type: bool
    label = ...  # type: Any
    def __init__(self, target) -> None: ...

class AtomTransition(Transition):
    label_ = ...  # type: Any
    label = ...  # type: Any
    serializationType = ...  # type: Any
    def __init__(self, target, label) -> None: ...
    def makeLabel(self): ...
    def matches(self, symbol, minVocabSymbol, maxVocabSymbol): ...

class RuleTransition(Transition):
    ruleIndex = ...  # type: Any
    precedence = ...  # type: Any
    followState = ...  # type: Any
    serializationType = ...  # type: Any
    isEpsilon = ...  # type: bool
    def __init__(self, ruleStart, ruleIndex, precedence, followState) -> None: ...
    def matches(self, symbol, minVocabSymbol, maxVocabSymbol): ...

class EpsilonTransition(Transition):
    serializationType = ...  # type: Any
    isEpsilon = ...  # type: bool
    outermostPrecedenceReturn = ...  # type: Any
    def __init__(self, target, outermostPrecedenceReturn: int = ...) -> None: ...
    def matches(self, symbol, minVocabSymbol, maxVocabSymbol): ...

class RangeTransition(Transition):
    serializationType = ...  # type: Any
    start = ...  # type: Any
    stop = ...  # type: Any
    label = ...  # type: Any
    def __init__(self, target, start, stop) -> None: ...
    def makeLabel(self): ...
    def matches(self, symbol, minVocabSymbol, maxVocabSymbol): ...

class AbstractPredicateTransition(Transition):
    def __init__(self, target) -> None: ...

class PredicateTransition(AbstractPredicateTransition):
    serializationType = ...  # type: Any
    ruleIndex = ...  # type: Any
    predIndex = ...  # type: Any
    isCtxDependent = ...  # type: Any
    isEpsilon = ...  # type: bool
    def __init__(self, target, ruleIndex, predIndex, isCtxDependent) -> None: ...
    def matches(self, symbol, minVocabSymbol, maxVocabSymbol): ...
    def getPredicate(self): ...

class ActionTransition(Transition):
    serializationType = ...  # type: Any
    ruleIndex = ...  # type: Any
    actionIndex = ...  # type: Any
    isCtxDependent = ...  # type: Any
    isEpsilon = ...  # type: bool
    def __init__(self, target, ruleIndex, actionIndex: int = ..., isCtxDependent: bool = ...) -> None: ...
    def matches(self, symbol, minVocabSymbol, maxVocabSymbol): ...

class SetTransition(Transition):
    serializationType = ...  # type: Any
    label = ...  # type: Any
    def __init__(self, target, set) -> None: ...
    def matches(self, symbol, minVocabSymbol, maxVocabSymbol): ...

class NotSetTransition(SetTransition):
    serializationType = ...  # type: Any
    def __init__(self, target, set) -> None: ...
    def matches(self, symbol, minVocabSymbol, maxVocabSymbol): ...

class WildcardTransition(Transition):
    serializationType = ...  # type: Any
    def __init__(self, target) -> None: ...
    def matches(self, symbol, minVocabSymbol, maxVocabSymbol): ...

class PrecedencePredicateTransition(AbstractPredicateTransition):
    serializationType = ...  # type: Any
    precedence = ...  # type: Any
    isEpsilon = ...  # type: bool
    def __init__(self, target, precedence) -> None: ...
    def matches(self, symbol, minVocabSymbol, maxVocabSymbol): ...
    def getPredicate(self): ...