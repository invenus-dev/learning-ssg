import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("div", "Hello, World!", None, {"class": "container", "id": "main"})
        self.assertEqual(node.props_to_html(), ' class="container" id="main"')
    
    def test_none_props_to_html(self):
        node = HTMLNode("div", "Hello, World!", None, None)
        self.assertEqual(node.props_to_html(), '')

    def test_empty_props_to_html(self):
        node = HTMLNode("div", "Hello, World!", None, {})
        self.assertEqual(node.props_to_html(), '')
