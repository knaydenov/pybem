from unittest import TestCase
from pybem import Block, Element


class BlockTest(TestCase):
    def setUp(self) -> None:
        self.block = Block('block')

    def test_get_base_class_returns_valid_string(self):
        self.assertEqual('block', self.block.get_base_class())

    def test_create_element_returns_valid_element(self):
        element = self.block.create_element('elem')
        self.assertIsInstance(element, Element)
        self.assertEqual(element.get_name(), 'elem')
