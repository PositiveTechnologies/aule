# Stubs for antlr4.atn.PredictionMode (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from enum import Enum


class PredictionMode(Enum):
    SLL = ...  # type: int
    LL = ...  # type: int
    LL_EXACT_AMBIG_DETECTION = ...  # type: int
    @classmethod
    def hasSLLConflictTerminatingPrediction(cls, mode, configs): ...
    @classmethod
    def hasConfigInRuleStopState(cls, configs): ...
    @classmethod
    def allConfigsInRuleStopStates(cls, configs): ...
    @classmethod
    def resolvesToJustOneViableAlt(cls, altsets): ...
    @classmethod
    def allSubsetsConflict(cls, altsets): ...
    @classmethod
    def hasNonConflictingAltSet(cls, altsets): ...
    @classmethod
    def hasConflictingAltSet(cls, altsets): ...
    @classmethod
    def allSubsetsEqual(cls, altsets): ...
    @classmethod
    def getUniqueAlt(cls, altsets): ...
    @classmethod
    def getAlts(cls, altsets): ...
    @classmethod
    def getConflictingAltSubsets(cls, configs): ...
    @classmethod
    def getStateToAltMap(cls, configs): ...
    @classmethod
    def hasStateAssociatedWithOneAlt(cls, configs): ...
    @classmethod
    def getSingleViableAlt(cls, altsets): ...