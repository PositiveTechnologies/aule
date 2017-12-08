from aule.generated.alfaAST import *
from aule.generated.alfaParserVisitor import alfaParserVisitor


class alfaASTVisitor(alfaParserVisitor):

    def visitApplyStatement(self, ctx):
        return ApplyStatement(ctx.algorithm.text)

    def visitEffectStatement(self, ctx):
        return EffectStatement(ctx.getText())

    def visitRulelist(self, ctx):
        return self.visitChildren(ctx)

    def visitAttributeAccessExpression(self, ctx):
        if not ctx.attributeAccessExpression():
            return Identifier(ctx.ID().getText())
        return AttributeAccessExpression(self.visit(ctx.attributeAccessExpression()), ctx.ID().getText())

    def visitAttributeValue(self, ctx):
        text = ctx.getText()
        if text.lower() == "true" or text.lower() == "false":
            return LiteralBoolean(text.lower())
        elif text[0] == '"':
            return LiteralString(text)
        else:
            return LiteralNumeric(text)

    def visitArrayExpression(self, ctx):
        elements = []
        e = None
        i = 0
        while ctx.literal(i):
            text = str(ctx.literal(i).getText())
            if text[0] in ['"', "'"]:
                e = LiteralString(text)
            else:
                e = LiteralNumeric(text)
            elements.append(e)
            i += 1
        return ArrayExpression(elements)

    def visitBinaryOperator(self, ctx):
        return ctx.getText()

    def visitSetOperator(self, ctx):
        return ctx.getText().lower()

    def visitLogicalOperator(self, ctx):
        return ctx.getText().lower()

    def visitTargetStatement(self, ctx):
        clauses = []
        i = 0
        while ctx.targetExpression(i):
            clauses.append(self.visit(ctx.targetExpression(i)))
            i += 1
        return TargetStatement(clauses)

    def visitTargetLogicalExpression(self, ctx):
        left = self.visit(ctx.targetExpression(0))
        right = self.visit(ctx.targetExpression(1))
        operator = ctx.logicalOperator().getText().lower()
        return LogicalExpression(operator, left, right)

    def visitTargetUnaryExpression(self, ctx):
        left = self.visit(ctx.targetExpression())
        return UnaryExpression("not", left)

    def visitBooleanExpression(self, ctx):
        return LiteralBoolean(ctx.getText().lower())

    def visitTargetPrimitiveBinary(self, ctx):
        left = self.visit(ctx.targetAtom(0))
        right = self.visit(ctx.targetAtom(1))
        operator = self.visit(ctx.binaryOperator())
        return BinaryExpression(operator, left, right)

    def visitTargetPrimitiveSet(self, ctx):
        left = self.visit(ctx.targetAtom())
        right = self.visit(ctx.arrayExpression())
        operator = self.visit(ctx.setOperator())
        return BinaryExpression(operator, left, right)

    def visitTargetPrimitiveIn(self, ctx):
        left = self.visit(ctx.attributeValue())
        right = self.visit(ctx.attributeAccessExpression())
        return BinaryExpression("in", left, right)

    def visitTargetAtom(self, ctx):
        return self.visit(ctx.children[0])

    def visitTargetAnyExpression(self, ctx):
        left = self.visit(ctx.children[0].children[1])
        right = self.visit(ctx.children[0].children[3])
        return AnyExpression(left, right)

    def visitTargetBooleanExpression(self, ctx):
        return LiteralBoolean(ctx.getText().lower())

    def visitTargetParenthesisExpression(self, ctx):
        return self.visit(ctx.targetExpression())

    def visitTargetArrayExpression(self, ctx):
        return self.visit(ctx.arrayExpression())

    def visitTargetAtributeAccessExpression(self, ctx):
        return self.visit(ctx.attributeAccessExpression())

    def visitTargetAtributeValueExpression(self, ctx):
        return self.visit(ctx.attributeValue())

    def visitRuleDeclaration(self, ctx):
        rule_id = None
        target = None
        events = []

        if ctx.ruleId:
            rule_id = ctx.ruleId.text

        effect = self.visit(ctx.effectStatement())

        if ctx.targetStatement():
            target = self.visit(ctx.targetStatement())

        return RuleDeclaration(rule_id, effect, target)

    def visitPolicySetBody(self, ctx):
        if ctx.ID():
            return str(ctx.ID().getText())
        if ctx.policySetDeclaration():
            return self.visit(ctx.policySetDeclaration())
        if ctx.policyDeclaration():
            return self.visit(ctx.policyDeclaration())
    
    def visitPolicySetDeclaration(self, ctx):
        name = None
        target = None
        references = []
        policies = []
        policysets = []
        modifiers = []

        if ctx.EXPORT():
            modifiers.append(ExportKeyword("export"))

        if ctx.policySetId:
            name = ctx.policySetId.text

        algorithm = self.visit(ctx.applyStatement())
        
        if ctx.targetStatement():
            target = self.visit(ctx.targetStatement())

        i = 0
        while ctx.policySetBody(i):
            result = self.visit(ctx.policySetBody(i))
            if type(result) == str:
                references.append(result)
            elif isinstance(result, PolicyDeclaration):
                policies.append(result)
            elif isinstance(result, PolicySetDeclaration):
                policysets.append(result)
            else:
                raise ValueError("Unknown node type")
            i += 1

        node = PolicySetDeclaration(name, algorithm, target, references, policies, policysets, modifiers)
        return node

    def visitPolicyDeclaration(self, ctx):
        name = None
        target = None
        rules = []
        modifiers = []

        if ctx.EXPORT():
            modifiers.append(ExportKeyword("export"))

        if ctx.policyId:
            name = ctx.policyId.text

        algorithm = self.visit(ctx.applyStatement())
        
        if ctx.targetStatement():
            target = self.visit(ctx.targetStatement())

        i = 0
        while ctx.ruleDeclaration(i):
            rules.append(self.visit(ctx.ruleDeclaration(i)))
            i += 1

        node = PolicyDeclaration(name, algorithm, target, rules, modifiers)
        return node

    def visitNameSpaceBody(self, ctx):
        if ctx.policyDeclaration():
            return self.visit(ctx.policyDeclaration())
        if ctx.policySetDeclaration():
            return self.visit(ctx.policySetDeclaration())
        if ctx.nameSpaceDeclaration():
            return self.visit(ctx.nameSpaceDeclaration())

    def visitNameSpaceDeclaration(self, ctx):
        name = ctx.ID().getText()
        body = []
        i = 0
        while ctx.nameSpaceBody(i):
            body.append(self.visit(ctx.nameSpaceBody(i)))
            i += 1
        return NameSpaceDeclaration(name, body)

    def visitRoot(self, ctx):
        body = []
        i = 0
        while ctx.nameSpaceDeclaration(i):
            body.append(self.visit(ctx.nameSpaceDeclaration(i)))
            i += 1
        return Script(body)
