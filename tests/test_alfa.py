import os
import tests.utils as utils
from .context import ParserFactory
from .context import ASTParserFactory
from .context import alfaASTVisitor
from .context import GRAMMARS_PATH
from .context import alfaAST as ast

def test_alfa_syntax():
    """ ALFA grammar smoke tests. """
    path = GRAMMARS_PATH + "/alfa/examples/"
    parser = ParserFactory.create("alfa")
    files = os.listdir(path)
    for file in files:
        fname = path + file
        tests = utils.get_tests(fname, "#begin", "#end")
        for query in tests:
            if not parser.check_syntax(query):
                print("File: " + file)
                print("Query: \n" + query)
                assert False

   
def test_alfa_policy_ast():
    """ ALFA Policy smoke test. """
    policy = """
        namespace corp {
            policy medicalPolicy {
                target clause user.id == "admin"
                apply denyOverrides
                rule {
                    permit
                    target clause "admin" in user.roles and "admin" == user.id
                        clause Attributes.role in ["doctor", "director"] and Attributes.age > 18
                }
                rule aa { 
                    deny
                    target clause (Attributes.age == 18) AND (Attributes.age < 19)
                } 
                rule bb {
                    deny
                    target clause Attributes.role == "doctor" and Attributes.age > 18
                }
                rule cc {
                    deny
                    target clause true
                }
            }
        }    
    """
    # Native parsing.
    parser = ParserFactory.create("alfa")
    tree = parser.parse(policy)
    ast_visitor = alfaASTVisitor()
    nodes = ast_visitor.visit(tree)
    ns = nodes.body[0]

    assert isinstance(ns, ast.NameSpaceDeclaration)
    node = ns.body[0]

    assert isinstance(node, ast.PolicyDeclaration)
    assert node.name == "medicalPolicy"
    
    algorithm = node.algorithm
    assert isinstance(algorithm, ast.ApplyStatement)
    assert algorithm.value == "denyOverrides"

    rules = node.rules
    assert len(rules) == 4

    # Parsing using AST.
    ast_parser = ASTParserFactory.create("alfa")
    nodes = ast_parser.parse(policy)
    ns = nodes.body[0]
    assert isinstance(ns, ast.NameSpaceDeclaration)
    node = ns.body[0]

    assert isinstance(node, ast.PolicyDeclaration)
    assert node.name == "medicalPolicy"
    
    algorithm = node.algorithm
    assert isinstance(algorithm, ast.ApplyStatement)
    assert algorithm.value == "denyOverrides"

    body = node.rules
    assert len(body) == 4


def test_alfa_policyset_ast():
    """ ALFA PolicySet smoke test. """
    policy = """
        namespace corp {
            policySet topLevel {
                target clause Attributes.resource == "medical"
                apply denyOverrides
                medicalPolicy1
                policy printerPolicy {
                    target clause Attributes.resourceType == "medicalRecord"
                    apply denyOverrides
                    rule {
                        permit
                        target clause Attributes.role == "doctor"
                    }
                }
                medicalPolicy2
                medicalPolicy3
            }
        }
    """
    # Native parsing.
    parser = ParserFactory.create("alfa")
    tree = parser.parse(policy)
    ast_visitor = alfaASTVisitor()
    nodes = ast_visitor.visit(tree)
    ns = nodes.body[0]
    assert isinstance(ns, ast.NameSpaceDeclaration)
    node = ns.body[0]
    
    assert isinstance(node, ast.PolicySetDeclaration)
    assert node.name == "topLevel"
    
    algorithm = node.algorithm
    assert isinstance(algorithm, ast.ApplyStatement)
    assert algorithm.value == "denyOverrides"

    policysets = node.policysets
    assert len(policysets) == 0

    references = node.references
    assert len(references) == 3

    references[0] = "medicalPolicy1"
    references[1] = "medicalPolicy2"
    references[2] = "medicalPolicy3"

    policies = node.policies
    assert len(policies) == 1

    policy = policies[0]
    assert policy.name == "printerPolicy"
    assert isinstance(policy, ast.PolicyDeclaration)

def test_alfa_namespace_ast():
    """ ALFA Namespace smoke test. """
    policy = """
        namespace com {
            namespace corp { 
                export policy topLevel {
                    target clause Attributes.resource == "medical"
                    apply denyOverrides
                    rule {
                        permit
                        target clause Attributes.role == "doctor"
                    }
                }
            }    
        }    
    """
    # Native parsing.
    parser = ParserFactory.create("alfa")
    tree = parser.parse(policy)
    ast_visitor = alfaASTVisitor()
    nodes = ast_visitor.visit(tree)
    
    node = nodes.body[0]
    assert isinstance(node, ast.NameSpaceDeclaration)
    assert node.name == "com"
    assert len(node.body) == 1
    
    node = nodes.body[0].body[0]
    assert isinstance(node, ast.NameSpaceDeclaration)
    assert node.name == "corp"
    assert len(node.body) == 1
    
    node = nodes.body[0].body[0].body[0]
    assert node.name == "topLevel"
    assert node.modifiers[0].text == "export"
