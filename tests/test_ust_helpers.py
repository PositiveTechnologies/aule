from .context import ust


def test_field_by_name_direct():
    classes = [
        ust.ClassDeclaration(
            name=ust.Identifier("Foo"),
            fields=[
                ust.FieldDeclaration(
                    name=ust.Identifier("foo_field"),
                    type=ust.TypeReference(ust.SimpleType.STRING)
                )
            ]
        ),
        ust.ClassDeclaration(
            name=ust.Identifier("Bar"),
            fields=[
                ust.FieldDeclaration(
                    name=ust.Identifier("bar_field"),
                    type=ust.TypeReference(ust.SimpleType.FLOAT)
                )
            ]
        )
    ]
    cls_reference = ust.helpers.ClassesReference(classes)

    assert cls_reference.get_field(classes[0], "non_existent") is None
    assert cls_reference.get_field(classes[0], "bar_field") is None
    assert isinstance(cls_reference.get_field(classes[0], "foo_field"), ust.FieldDeclaration)
    assert cls_reference.get_field(classes[0], "foo_field").type.type == ust.SimpleType.STRING

    assert cls_reference.get_field(classes[1], "non_existent") is None
    assert cls_reference.get_field(classes[1], "foo_field") is None
    assert isinstance(cls_reference.get_field(classes[1], "bar_field"), ust.FieldDeclaration)
    assert cls_reference.get_field(classes[1], "bar_field").type.type == ust.SimpleType.FLOAT


def test_field_by_name_inheritance():
    classes = [
        ust.ClassDeclaration(
            name=ust.Identifier("Foo"),
            fields=[
                ust.FieldDeclaration(
                    name=ust.Identifier("foo_field"),
                    type=ust.TypeReference(ust.SimpleType.STRING)
                )
            ]
        ),
        ust.ClassDeclaration(
            name=ust.Identifier("Dummy"),
            parents=[
                ust.Identifier("Foo")
            ],
        ),
        ust.ClassDeclaration(
            name=ust.Identifier("Bar"),
            parents=[
                ust.Identifier("Dummy")
            ],
            fields=[
                ust.FieldDeclaration(
                    name=ust.Identifier("bar_field"),
                    type=ust.TypeReference(ust.SimpleType.FLOAT)
                )
            ]
        )
    ]
    cls_reference = ust.helpers.ClassesReference(classes)
    assert isinstance(cls_reference.get_field(classes[2], "bar_field"), ust.FieldDeclaration)
    assert cls_reference.get_field(classes[2], "bar_field").type.type == ust.SimpleType.FLOAT
    assert isinstance(cls_reference.get_field(classes[2], "foo_field"), ust.FieldDeclaration)
    assert cls_reference.get_field(classes[2], "foo_field").type.type == ust.SimpleType.STRING


def test_multiple_not_conflicting_parents():
    classes = [
        ust.ClassDeclaration(
            name=ust.Identifier("Foo"),
            fields=[
                ust.FieldDeclaration(
                    name=ust.Identifier("foo_field"),
                    type=ust.TypeReference(ust.SimpleType.STRING)
                )
            ]
        ),
        ust.ClassDeclaration(
            name=ust.Identifier("Dummy"),
            fields=[
                ust.FieldDeclaration(
                    name=ust.Identifier("dummy_field"),
                    type=ust.TypeReference(ust.SimpleType.INTEGER)
                )
            ]
        ),
        ust.ClassDeclaration(
            name=ust.Identifier("Bar"),
            parents=[
                ust.Identifier("Foo"),
                ust.Identifier("Dummy")
            ],
            fields=[
                ust.FieldDeclaration(
                    name=ust.Identifier("bar_field"),
                    type=ust.TypeReference(ust.SimpleType.FLOAT)
                )
            ]
        )
    ]
    cls_reference = ust.helpers.ClassesReference(classes)
    assert isinstance(cls_reference.get_field(classes[2], "bar_field"), ust.FieldDeclaration)
    assert cls_reference.get_field(classes[2], "bar_field").type.type == ust.SimpleType.FLOAT
    assert isinstance(cls_reference.get_field(classes[2], "foo_field"), ust.FieldDeclaration)
    assert cls_reference.get_field(classes[2], "foo_field").type.type == ust.SimpleType.STRING
    assert isinstance(cls_reference.get_field(classes[2], "dummy_field"), ust.FieldDeclaration)
    assert cls_reference.get_field(classes[2], "dummy_field").type.type == ust.SimpleType.INTEGER