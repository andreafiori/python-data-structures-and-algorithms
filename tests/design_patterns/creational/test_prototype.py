from python_design_patterns.design_patterns.creational.prototype import Document

class TestPrototype:
    def test_document_clone(self):
        original = Document(
            title="Original",
            content="This is the original content.",
            metadata={"author": "Alice", "version": 1}
        )
        cloned = original.clone()

        # Check that the clone is a new object
        assert cloned is not original

        # Check that the clone has the same attributes
        assert cloned.title == original.title
        assert cloned.content == original.content
        assert cloned.metadata == original.metadata

        # Modify the clone and ensure the original is unchanged
        cloned.title = "Cloned"
        cloned.metadata["version"] = 2
        assert original.title == "Original"
        assert original.metadata["version"] == 1

    def test_document_clone_is_deep_copy(self):
        original = Document(
            title="Original",
            content="This is the original content.",
            metadata={"author": "Alice", "version": 1}
        )
        cloned = original.clone()

        # Modify a mutable attribute in the clone
        cloned.metadata["author"] = "Bob"

        # Ensure the original's metadata is unchanged
        assert original.metadata["author"] == "Alice"
