import unittest

from textnode import TextNode, TextType


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
        node2 = TextNode("Hello, World!", TextType.TEXT)
        self.assertNotEqual(node1, node2)

    def test_noteq3_url(self):
        node1 = TextNode("Hello, World!", TextType.BOLD, "https://www.google.com")
        node2 = TextNode("Hello, World!", TextType.BOLD, "https://www.dash.com")
        self.assertNotEqual(node1, node2)

    def test_url_none(self):
        node1 = TextNode("Hello, World!", TextType.BOLD, "https://www.google.com")
        node2 = TextNode("Hello, World!", TextType.BOLD)
        self.assertNotEqual(node1, node2)


if __name__ == "__main__":
    unittest.main()
