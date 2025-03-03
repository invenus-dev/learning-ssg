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
        self.assertEqual(node.tag, None)
        self.assertEqual(node.value, "Hello, World!")
        self.assertEqual(node.props, None)

    def test_text_node_to_html_node_bold(self):
        node = text_node_to_html_node(TextNode("Hello, World!", TextType.BOLD))
        self.assertEqual(node.tag, "b")
        self.assertEqual(node.value, "Hello, World!")
        self.assertEqual(node.props, None)
    
    def test_text_node_to_html_node_code(self):
        node = text_node_to_html_node(TextNode("Hello, World!", TextType.CODE))
        self.assertEqual(node.tag, "code")
        self.assertEqual(node.value, "Hello, World!")
        self.assertEqual(node.props, None)
    
    def test_text_node_to_html_node_link(self):
        node = text_node_to_html_node(TextNode("Hello, World!", TextType.LINK, "https://www.google.com"))
        self.assertEqual(node.tag, "a")
        self.assertEqual(node.value, "Hello, World!")
        self.assertEqual(node.props, {"href": "https://www.google.com"})

    def test_text_node_to_html_node_link_no_url(self):
        node = text_node_to_html_node(TextNode("Hello, World!", TextType.LINK))
        self.assertEqual(node.tag, None)
        self.assertEqual(node.value, "Hello, World!")
        self.assertEqual(node.props, None)        
    
    def test_text_node_to_html_node_image(self):
        node = text_node_to_html_node(TextNode("Hello, World!", TextType.IMAGE, "https://www.google.com"))
        self.assertEqual(node.tag, "img")
        self.assertEqual(node.value, "")
        self.assertEqual(node.props, {"src": "https://www.google.com", "alt": "Hello, World!"})

    def test_text_node_to_html_node_image_no_alt(self):
        node = text_node_to_html_node(TextNode("", TextType.IMAGE, "https://www.google.com"))
        self.assertEqual(node.tag, "img")
        self.assertEqual(node.value, "")
        self.assertEqual(node.props, {"src": "https://www.google.com", "alt": "Image"})
       

if __name__ == "__main__":
    unittest.main()
        