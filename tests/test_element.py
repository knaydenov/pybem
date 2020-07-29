from unittest import TestCase
from pybem import Element, Block


class ElementTest(TestCase):
    def setUp(self) -> None:
        self.block = Block('block')
        self.element = Element('elem', self.block)

    def test_get_block_returns_valid_block(self):
        self.assertEqual(self.element.get_block(), self.block)

    def test_set_block_sets_block(self):
        new_block = Block('new_block')
        self.element.set_block(new_block)
        self.assertEqual(self.element.get_block(), new_block)

    def test_get_base_class_returns_valid_string(self):
        self.assertEqual('block__elem', self.element.get_base_class())
