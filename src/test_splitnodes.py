import unittest

from splitnodes import split_nodes_delimiter
from textnode import TextNode, TextType

class TestSplitNodes(unittest.TestCase):
    def test_no_split(self):
        nodes = [TextNode("Hello, World!", TextType.NORMAL), TextNode("Other part", TextType.NORMAL)]
        new_nodes = split_nodes_delimiter(nodes, "*", TextType.BOLD)
        self.assertEqual(nodes, new_nodes)

    def test_split_bold(self):
        nodes = [TextNode("Hello, *World*!", TextType.NORMAL)]
        new_nodes = split_nodes_delimiter(nodes, "*", TextType.BOLD)
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0], TextNode("Hello, ", TextType.NORMAL)) 
        self.assertEqual(new_nodes[1], TextNode("World", TextType.BOLD))
        self.assertEqual(new_nodes[2], TextNode("!", TextType.NORMAL))
    
    def test_split_many_bolds(self):
        nodes = [TextNode("Hello, *World*! *How* are you?", TextType.NORMAL)]
        new_nodes = split_nodes_delimiter(nodes, "*", TextType.BOLD)
        self.assertEqual(len(new_nodes), 5)
        self.assertEqual(new_nodes[0], TextNode("Hello, ", TextType.NORMAL)) 
        self.assertEqual(new_nodes[1], TextNode("World", TextType.BOLD))
        self.assertEqual(new_nodes[2], TextNode("! ", TextType.NORMAL))
        self.assertEqual(new_nodes[3], TextNode("How", TextType.BOLD))
        self.assertEqual(new_nodes[4], TextNode(" are you?", TextType.NORMAL))
    
    def test_split_wrong_encapsulate(self):
        nodes = [TextNode("Hello, *World* there is *error!", TextType.NORMAL)]
        with self.assertRaises(ValueError):
            split_nodes_delimiter(nodes, "*", TextType.BOLD)
    
    def test_split_code(self):
        nodes = [TextNode("Hello, `World`!", TextType.NORMAL)]
        new_nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0], TextNode("Hello, ", TextType.NORMAL)) 
        self.assertEqual(new_nodes[1], TextNode("World", TextType.CODE))
        self.assertEqual(new_nodes[2], TextNode("!", TextType.NORMAL))