import unittest

from textnode  import TextNode, TextType, text_node_to_html_node
from leafnode import LeafNode
        
class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("Hello, World!", TextType.BOLD)
        node2 = TextNode("Hello, World!", TextType.BOLD)
        self.assertEqual(node1, node2)

    def test_noteq_text(self):
        node1 = TextNode("Hello, World!", TextType.BOLD)
        node2 = TextNode("Hello, World World!", TextType.BOLD)
        self.assertNotEqual(node1, node2)
    
    def test_noteq2_type(self):
        node1 = TextNode("Hello, World!", TextType.BOLD)
        node2 = TextNode("Hello, World!", TextType.NORMAL)
        self.assertNotEqual(node1, node2)
    
    def test_noteq3_url(self):
        node1 = TextNode("Hello, World!", TextType.BOLD, "https://www.google.com")
        node2 = TextNode("Hello, World!", TextType.BOLD, "https://www.dash.com")
        self.assertNotEqual(node1, node2)

    def test_url_none(self):
        node1 = TextNode("Hello, World!", TextType.BOLD, "https://www.google.com")
        node2 = TextNode("Hello, World!", TextType.BOLD)
        self.assertNotEqual(node1, node2)

    def test_text_node_to_html_node_normal(self):
        node = text_node_to_html_node(TextNode("Hello, World!", TextType.NORMAL))
        self.assertEqual(node.to_html(), "Hello, World!")

    def test_text_node_to_html_node_bold(self):
        node = text_node_to_html_node(TextNode("Hello, World!", TextType.BOLD))
        self.assertEqual(node.to_html(), "<b>Hello, World!</b>")
    
    def test_text_node_to_html_node_code(self):
        node = text_node_to_html_node(TextNode("Hello, World!", TextType.CODE))
        self.assertEqual(node.to_html(), "<code>Hello, World!</code>")
    
    def test_text_node_to_html_node_link(self):
        node = text_node_to_html_node(TextNode("Hello, World!", TextType.LINK, "https://www.google.com"))
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Hello, World!</a>')

    def test_text_node_to_html_node_link_no_url(self):
        node = text_node_to_html_node(TextNode("Hello, World!", TextType.LINK))
        self.assertEqual(node.to_html(), "Hello, World!")
    
    def test_text_node_to_html_node_image(self):
        node = text_node_to_html_node(TextNode("Hello, World!", TextType.IMAGE, "https://www.google.com"))
        self.assertEqual(node.to_html(), '<img src="https://www.google.com" alt="Hello, World!"></img>')

        

if __name__ == "__main__":
    unittest.main()
        