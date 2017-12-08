# Generated from alfaParser.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .alfaParser import alfaParser
else:
    from alfaParser import alfaParser

# This class defines a complete generic visitor for a parse tree produced by alfaParser.

class alfaParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by alfaParser#root.
    def visitRoot(self, ctx:alfaParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by alfaParser#nameSpaceDeclaration.
    def visitNameSpaceDeclaration(self, ctx:alfaParser.NameSpaceDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by alfaParser#nameSpaceBody.
    def visitNameSpaceBody(self, ctx:alfaParser.NameSpaceBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by alfaParser#policySetDeclaration.
    def visitPolicySetDeclaration(self, ctx:alfaParser.PolicySetDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by alfaParser#policySetBody.
    def visitPolicySetBody(self, ctx:alfaParser.PolicySetBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by alfaParser#policyDeclaration.
    def visitPolicyDeclaration(self, ctx:alfaParser.PolicyDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by alfaParser#applyStatement.
    def visitApplyStatement(self, ctx:alfaParser.ApplyStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by alfaParser#ruleDeclaration.
    def visitRuleDeclaration(self, ctx:alfaParser.RuleDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by alfaParser#effectStatement.
    def visitEffectStatement(self, ctx:alfaParser.EffectStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by alfaParser#targetStatement.
    def visitTargetStatement(self, ctx:alfaParser.TargetStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by alfaParser#targetPrimitiveExpression.
    def visitTargetPrimitiveExpression(self, ctx:alfaParser.TargetPrimitiveExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by alfaParser#targetAnyExpression.
    def visitTargetAnyExpression(self, ctx:alfaParser.TargetAnyExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by alfaParser#targetLogicalExpression.
    def visitTargetLogicalExpression(self, ctx:alfaParser.TargetLogicalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by alfaParser#targetParenthesisExpression.
    def visitTargetParenthesisExpression(self, ctx:alfaParser.TargetParenthesisExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by alfaParser#targetUnaryExpression.
    def visitTargetUnaryExpression(self, ctx:alfaParser.TargetUnaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by alfaParser#targetBooleanExpression.
    def visitTargetBooleanExpression(self, ctx:alfaParser.TargetBooleanExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by alfaParser#targetPrimitiveBinary.
    def visitTargetPrimitiveBinary(self, ctx:alfaParser.TargetPrimitiveBinaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by alfaParser#targetPrimitiveSet.
    def visitTargetPrimitiveSet(self, ctx:alfaParser.TargetPrimitiveSetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by alfaParser#targetPrimitiveIn.
    def visitTargetPrimitiveIn(self, ctx:alfaParser.TargetPrimitiveInContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by alfaParser#targetAtom.
    def visitTargetAtom(self, ctx:alfaParser.TargetAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by alfaParser#unaryOperator.
    def visitUnaryOperator(self, ctx:alfaParser.UnaryOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by alfaParser#binaryOperator.
    def visitBinaryOperator(self, ctx:alfaParser.BinaryOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by alfaParser#logicalOperator.
    def visitLogicalOperator(self, ctx:alfaParser.LogicalOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by alfaParser#setOperator.
    def visitSetOperator(self, ctx:alfaParser.SetOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by alfaParser#anyExpression.
    def visitAnyExpression(self, ctx:alfaParser.AnyExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by alfaParser#attributeAccessExpression.
    def visitAttributeAccessExpression(self, ctx:alfaParser.AttributeAccessExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by alfaParser#attributeValue.
    def visitAttributeValue(self, ctx:alfaParser.AttributeValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by alfaParser#arrayExpression.
    def visitArrayExpression(self, ctx:alfaParser.ArrayExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by alfaParser#literal.
    def visitLiteral(self, ctx:alfaParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by alfaParser#booleanLiteral.
    def visitBooleanLiteral(self, ctx:alfaParser.BooleanLiteralContext):
        return self.visitChildren(ctx)



del alfaParser