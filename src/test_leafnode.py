import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_leaf_to_html_props(self):
        node = LeafNode("p", "Hello, world!", {"class": "container", "id": "main"})
        self.assertEqual(node.to_html(), '<p class="container" id="main">Hello, world!</p>')

    def test_leaf_to_html_link(self):
        node = LeafNode("a", "Google", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Google</a>')
    
    def test_handle_no_value(self):
        with self.assertRaises(ValueError):
            node = LeafNode("p", None)
            node.to_html()