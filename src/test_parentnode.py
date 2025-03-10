import unittest

from parentnode import ParentNode
from leafnode   import LeafNode

class TestParentNode(unittest.TestCase):
    def test_parent_to_html(self):
        node = ParentNode("p", [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ])
        self.assertEqual(
            node.to_html(), 
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        )
    
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        ) 
    
    def test_to_html_with_props(self):
        child_node = LeafNode("span", "child", {"class": "container"})
        parent_node = ParentNode("div", [child_node], {"id": "main"})
        self.assertEqual(
            parent_node.to_html(),
            '<div id="main"><span class="container">child</span></div>',
        )
    
    def test_handling_no_children(self):
        with self.assertRaises(ValueError):
            node = ParentNode("p", [])
            node.to_html()
    
    def test_handling_no_tag(self):
        with self.assertRaises(ValueError):
            node = ParentNode(None, [LeafNode("b", "Bold text")])
            node.to_html()
    
    def test_handling_empty_string_tag(self):
        with self.assertRaises(ValueError):
            node = ParentNode("", [LeafNode("b", "Bold text")])
            node.to_html()
    
    