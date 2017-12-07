import os
import tests.utils as utils
from .context import ASTParserFactory
from .context import ust
from .context import ParserFactory
from .context import GRAMMARS_PATH


def test_idl_syntax():
    """ IDL grammar smoke tests. """
    path = GRAMMARS_PATH + "/idl/examples/"
    parser = ParserFactory.create("idl")
    files = os.listdir(path)
    for file in files:
        fname = path + file
        tests = utils.get_tests(fname, "#begin", "#end")
        for text in tests:
            test = parser.check_syntax(text)
            if not test:
                print("File: " + file)
                print("Item: \n" + text)
                assert False


def test_basic_idl_ast():
    """ Very basic IDL visiting test """
    interface = """
        interface SQLEntity {
            database: str;
            ip: str;
    }
    """
    ast_parser = ASTParserFactory.create("idl")
    nodes = ast_parser.parse(interface)
    assert len(nodes) == 1
    assert nodes[0].name.name == "SQLEntity"
    assert nodes[0].node == "ClassDeclaration"
    assert nodes[0].parents == []
    assert nodes[0].fields[0].node == "FieldDeclaration"
    assert nodes[0].fields[0].name.name == "database"
    assert nodes[0].fields[1].node == "FieldDeclaration"
    assert nodes[0].fields[1].name.name == "ip"
    assert nodes[0].methods == []


def test_union_types_idl_ast():
    """ Test modifiers IDL visiting """
    interface = """
        interface foo {
            bar: str | int;
    }
    """
    ast_parser = ASTParserFactory.create("idl")
    nodes = ast_parser.parse(interface)
    assert len(nodes) == 1
    assert nodes[0].name.name == "foo"
    assert nodes[0].node == "ClassDeclaration"
    assert nodes[0].parents == []
    assert nodes[0].fields[0].node == "FieldDeclaration"
    assert nodes[0].fields[0].name.name == "bar"
    assert nodes[0].fields[0].type.node == "TypeReference"
    assert nodes[0].fields[0].type.type.node == "UnionType"
    assert nodes[0].fields[0].type.type.types[0].type == ust.SimpleType.STRING
    assert nodes[0].fields[0].type.type.types[1].type == ust.SimpleType.INTEGER


def test_tags_idl_ast():
    """ Test field tags IDL visiting """
    interface = """
        interface SQLEntity {
            database: str;
            f: String `species:"gopher" color:"blue"`;
    }
    """
    ast_parser = ASTParserFactory.create("idl")
    nodes = ast_parser.parse(interface)
    assert len(nodes) == 1
    assert nodes[0].name.name == "SQLEntity"
    assert nodes[0].node == "ClassDeclaration"
    assert nodes[0].parents == []
    assert nodes[0].fields[0].node == "FieldDeclaration"
    assert nodes[0].fields[0].name.name == "database"
    assert nodes[0].fields[1].node == "FieldDeclaration"
    assert nodes[0].fields[1].tags[0].name.name == "species"
    assert nodes[0].fields[1].tags[0].value == '"gopher"'
    assert nodes[0].fields[1].tags[1].name.name == "color"
    assert nodes[0].fields[1].tags[1].value == '"blue"'


def test_inheritance_idl_ast():
    """ Test inheritance IDL visiting """
    interface = """
        interface Node {
            type: "Node";
        }

        interface CommonStatement <: Node { 
            type: "CommonStatement";
        }

        interface ColumnName <: Primitive {
            type: "ColumnName";
            schema: Identifier | null;
            table: Identifier | null;
            column: Identifier;
        }
    """
    ast_parser = ASTParserFactory.create("idl")
    nodes = ast_parser.parse(interface)
    assert len(nodes) == 3
    assert nodes[0].name.name == "Node"
    assert nodes[0].node == "ClassDeclaration"
    assert nodes[0].parents == []
    assert nodes[0].fields[0].node == "FieldDeclaration"
    assert nodes[0].fields[0].name.name == "type"
    assert nodes[0].fields[0].modifiers == []
    assert nodes[0].methods == []
    assert nodes[1].name.name == "CommonStatement"
    assert nodes[1].node == "ClassDeclaration"
    assert nodes[1].parents[0].name == "Node"
    assert nodes[1].fields[0].node == "FieldDeclaration"
    assert nodes[1].fields[0].name.name == "type"
    assert nodes[1].fields[0].modifiers == []
    assert nodes[1].methods == []
    assert nodes[2].name.name == "ColumnName"
    assert nodes[2].node == "ClassDeclaration"
    assert nodes[2].parents[0].name == "Primitive"
    assert nodes[2].fields[0].node == "FieldDeclaration"
    assert nodes[2].fields[0].name.name == "type"
    assert nodes[2].fields[0].modifiers == []
    assert nodes[2].methods == []


def test_modifiers_idl_ast():
    """ Test modifiers IDL visiting """
    interface = """
        interface foo {
            private static bar: str;
    }
    """
    ast_parser = ASTParserFactory.create("idl")
    nodes = ast_parser.parse(interface)
    assert len(nodes) == 1
    assert nodes[0].name.name == "foo"
    assert nodes[0].node == "ClassDeclaration"
    assert nodes[0].parents == []
    assert nodes[0].fields[0].node == "FieldDeclaration"
    assert nodes[0].fields[0].name.name == "bar"
    assert nodes[0].fields[0].modifiers[0] == ust.Modifier.PRIVATE
    assert nodes[0].fields[0].modifiers[1] == ust.Modifier.STATIC
    assert nodes[0].fields[0].type.node == "TypeReference"
    assert nodes[0].fields[0].type.type == ust.SimpleType.STRING


def test_enum_idl_ast():
    """ Test modifiers IDL visiting """
    enum = """
        enum foo {
            a = "A";
            b = "B";
    }
    """
    ast_parser = ASTParserFactory.create("idl")
    nodes = ast_parser.parse(enum)
    assert len(nodes) == 1
    assert nodes[0].name.name == "foo"
    assert nodes[0].node == "EnumDeclaration"
    assert len(nodes[0].members) == 2
    assert nodes[0].members[0].node == "EnumMember"
    assert nodes[0].members[0].name.node == "Identifier"
    assert nodes[0].members[0].name.name == "a"
    assert nodes[0].members[0].value == "\"A\""
    assert nodes[0].members[1].node == "EnumMember"
    assert nodes[0].members[1].name.node == "Identifier"
    assert nodes[0].members[1].name.name == "b"
    assert nodes[0].members[1].value == "\"B\""


def test_annotations_idl_ast():
    """ Test interface annotations IDL visiting """
    interface = """
        [annotation]
        interface foo {
            bar: str;
        }
        """
    ast_parser = ASTParserFactory.create("idl")
    nodes = ast_parser.parse(interface)
    assert len(nodes) == 1
    assert nodes[0].name.name == "foo"
    assert nodes[0].node == "ClassDeclaration"
    assert nodes[0].parents == []
    assert nodes[0].fields[0].node == "FieldDeclaration"
    assert nodes[0].fields[0].name.name == "bar"
    assert nodes[0].fields[0].type.node == "TypeReference"
    assert nodes[0].fields[0].type.type == ust.SimpleType.STRING
    assert len(nodes[0].annotations) == 1
    assert nodes[0].annotations[0].node == "ClassAnnotation"
    assert nodes[0].annotations[0].value == "annotation"

    interface = """
        [easy][hard=annotation]
        interface foo {
            bar: str;
        }
        """
    ast_parser = ASTParserFactory.create("idl")
    nodes = ast_parser.parse(interface)
    assert len(nodes) == 1
    assert nodes[0].name.name == "foo"
    assert nodes[0].node == "ClassDeclaration"
    assert nodes[0].parents == []
    assert nodes[0].fields[0].node == "FieldDeclaration"
    assert nodes[0].fields[0].name.name == "bar"
    assert nodes[0].fields[0].type.node == "TypeReference"
    assert nodes[0].fields[0].type.type == ust.SimpleType.STRING
    assert len(nodes[0].annotations) == 2
    assert nodes[0].annotations[0].node == "ClassAnnotation"
    assert nodes[0].annotations[0].value == "easy"
    assert nodes[0].annotations[1].node == "ClassAnnotation"
    assert nodes[0].annotations[1].value == "hard=annotation"

