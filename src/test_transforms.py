import unittest

from transforms import text_to_textnodes, text_node_to_html_node, markdown_to_blocks
from textnode import TextNode, TextType


class TestTransforms(unittest.TestCase):
    def test_text_node_to_html_node_normal(self):
        node = text_node_to_html_node(TextNode("Hello, World!", TextType.TEXT))
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
        node = text_node_to_html_node(
            TextNode("Hello, World!", TextType.LINK, "https://www.google.com")
        )
        self.assertEqual(node.tag, "a")
        self.assertEqual(node.value, "Hello, World!")
        self.assertEqual(node.props, {"href": "https://www.google.com"})

    def test_text_node_to_html_node_link_no_url(self):
        node = text_node_to_html_node(TextNode("Hello, World!", TextType.LINK))
        self.assertEqual(node.tag, None)
        self.assertEqual(node.value, "Hello, World!")
        self.assertEqual(node.props, None)

    def test_text_node_to_html_node_image(self):
        node = text_node_to_html_node(
            TextNode("Hello, World!", TextType.IMAGE, "https://www.google.com")
        )
        self.assertEqual(node.tag, "img")
        self.assertEqual(node.value, "")
        self.assertEqual(
            node.props, {"src": "https://www.google.com", "alt": "Hello, World!"}
        )

    def test_text_node_to_html_node_image_no_alt(self):
        node = text_node_to_html_node(
            TextNode("", TextType.IMAGE, "https://www.google.com")
        )
        self.assertEqual(node.tag, "img")
        self.assertEqual(node.value, "")
        self.assertEqual(node.props, {"src": "https://www.google.com", "alt": "Image"})

    def test_text_to_textnodes(self):
        original_text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(original_text)

        self.assertListEqual(
            nodes,
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode(
                    "obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"
                ),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
        )

    def test_text_to_textnodes_empty_text(self):
        nodes = text_to_textnodes("")
        self.assertListEqual(nodes, [TextNode("", TextType.TEXT)])

    def test_text_to_textnodes_text_with_wrong_encapsulation(self):
        with self.assertRaises(ValueError):
            original_text = "This is **text with an _italic_ word and a `code block`"
            text_to_textnodes(original_text)

    def test_text_to_textnodes_text_with_nested(self):
        original_text = "This is **text _with an_ italic** word"
        nodes = text_to_textnodes(original_text)
        self.assertListEqual(
            nodes,
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text _with an_ italic", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
            ],
        )

    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_more_emptylines(self):
        md = """
This is **bolded** paragraph


This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line



- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
