from unittest import TestCase
from pybem import Node


class NodeImpl(Node):
    def get_base_class(self):
        return self.get_name()


class NodeTest(TestCase):
    def setUp(self) -> None:
        self.node = NodeImpl('node')

    def test_get_name_returns_valid_value(self):
        self.assertEqual(self.node.get_name(), 'node')

    def test_set_name_sets_valid_value(self):
        self.node.set_name('other')
        self.assertEqual(self.node.get_name(), 'other')

    def test_set_modifiers_sets_valid_modifiers(self):
        self.node.set_modifiers({'a': 1, 'b': True, 'c': False, 'd': 'string'})
        self.assertEqual({'a': 1, 'b': True, 'c': False, 'd': 'string'}, self.node.get_modifiers())

    def test_get_modifier_returns_valid_value(self):
        self.node.set_modifiers({'a': 1, 'b': True, 'c': False, 'd': 'string'})
        self.assertEqual(self.node.get_modifier('a'), 1)
        self.assertEqual(self.node.get_modifier('b'), True)
        self.assertEqual(self.node.get_modifier('c'), False)
        self.assertEqual(self.node.get_modifier('d'), 'string')

    def test_get_modifier_returns_valid_default_value(self):
        self.node.set_modifiers({'a': 1, 'b': True, 'c': False, 'd': 'string'})
        self.assertEqual(self.node.get_modifier('e'), None)
        self.assertEqual(self.node.get_modifier('e', False), False)
        self.assertEqual(self.node.get_modifier('e', 'hello'), 'hello')

    def test_add_modifier_adds_valid_value(self):
        self.node.add_modifier('a', 'hello')
        self.assertEqual(self.node.get_modifier('a'), 'hello')

        self.node.add_modifier('a',)
        self.assertEqual(self.node.get_modifier('a'), True)

    def test_has_modifier_returns_valid_value(self):
        self.node.set_modifiers({'a': 1, 'b': True, 'c': False, 'd': 'string'})
        
        self.assertTrue(self.node.has_modifier('a'))
        self.assertTrue(self.node.has_modifier('b'))
        self.assertTrue(self.node.has_modifier('c'))
        self.assertTrue(self.node.has_modifier('d'))
        self.assertFalse(self.node.has_modifier('e'))
        self.assertFalse(self.node.has_modifier('f'))

    def test_remove_modifier_removes_modifier(self):
        self.node.set_modifiers({'a': 1, 'b': True, 'c': False, 'd': 'string'})
        self.assertEqual(self.node.get_modifiers(), {'a': 1, 'b': True, 'c': False, 'd': 'string'})

        self.node.remove_modifier('a')
        self.assertEqual(self.node.get_modifiers(), {'b': True, 'c': False, 'd': 'string'})

        self.node.remove_modifier('c')
        self.assertEqual(self.node.get_modifiers(), {'b': True, 'd': 'string'})

        self.node.remove_modifier('not_exists')
        self.assertEqual(self.node.get_modifiers(), {'b': True, 'd': 'string'})

    # TODO: Add tests for methods beginning from 'remove_modifier'

    def test_build_classes(self):
        header = NodeImpl('header')
        header.add_modifier('sticky')
        header.add_modifier('color', 'red')
        header.add_modifier('width', 10)
        header.add_class('with-helper')

        card = NodeImpl('card')
        card.add_modifier('border', 'thin')
        card.add_class('js-anchor')
        card.add_class('js-anchor')  # Duplicate class

        header.add_mix(card)

        self.assertEqual(str(header), 'header header--sticky header--color_red header--width_10 with-helper card card--border_thin js-anchor')





