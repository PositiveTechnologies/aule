/*
A minimalist ALFA grammar for DBFW PoC.
*/

parser grammar alfaParser;

options { tokenVocab=alfaLexer; }

root
    : nameSpaceDeclaration* EOF
    ;

nameSpaceDeclaration
    : NAMESPACE nameSpaceId=ID '{' nameSpaceBody* '}'
    ;

nameSpaceBody
    : policySetDeclaration
    | policyDeclaration
    | nameSpaceDeclaration
    ;

policySetDeclaration
    : EXPORT? POLICYSET policySetId=ID '{' targetStatement? applyStatement policySetBody* '}'
    ;

policySetBody
    : ID 
    | policyDeclaration 
    | policySetDeclaration
    ;

policyDeclaration
    : EXPORT? POLICY policyId=ID '{' targetStatement? applyStatement ruleDeclaration* '}'
    ;

applyStatement
    : APPLY algorithm = (PEMIT_OVERRIDES | DENY_OVERRIDES | FIRST_APPLICABLE | PERMIT_UNLESS_DENY | DENY_UNLESS_PERMIT | ONLY_ONE_APPLICABLE )
    ;

ruleDeclaration
    : RULE ruleId=ID? '{' effectStatement targetStatement? '}'
    ;

effectStatement
    : PERMIT | DENY
    ;

targetStatement
    : TARGET (CLAUSE targetExpression)+
    ;

targetExpression
    : unaryOperator targetExpression                          #targetUnaryExpression
    | targetExpression logicalOperator targetExpression       #targetLogicalExpression
    | targetPrimitive                                         #targetPrimitive
    | anyExpression                                           #targetAnyExpression
    | booleanLiteral                                          #targetBooleanExpression
    | OPEN_PAREN targetExpression CLOSE_PAREN                 #targetParenthesisExpression
    ;

targetPrimitive
    : attributeAccessExpression binaryOperator attributeValue #targetPrimitiveBinary 
    | attributeAccessExpression setOperator   arrayExpression #targetPrimitiveSet
    ;

unaryOperator
    : NOT
    ;

binaryOperator
    : EQUALS | NOT_EQUALS | LESS_THAN | MORE_THAN | LESS_EQUAL | GREAT_EQUAL
    ;
    
logicalOperator
    : OR | AND
    ;

setOperator
   : IN | SUBSET | SUBSETEQ
   ;

anyExpression
    : ANY (attributeAccessExpression | arrayExpression) IN (attributeAccessExpression | arrayExpression)
    ;

attributeAccessExpression
    : attributeAccessExpression '.' ID
    | ID
    ;

attributeValue
    : literal
    ;

arrayExpression
    : '[' literal (',' literal)* ']'
    ;

literal:
    INT 
    | STRING 
    | boolean_literal
    ;

booleanLiteral:
    TRUE 
    | FALSE
    ;
