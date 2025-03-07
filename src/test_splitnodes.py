import unittest

from splitnodes import split_nodes_delimiter, split_nodes_image, split_nodes_link
from textnode import TextNode, TextType

class TestSplitNodes(unittest.TestCase):
    
    # split_nodes_delimiter
    def test_no_split(self):
        nodes = [TextNode("Hello, World!", TextType.TEXT), TextNode("Other part", TextType.TEXT)]
        new_nodes = split_nodes_delimiter(nodes, "*", TextType.BOLD)
        self.assertEqual(nodes, new_nodes)

    def test_split_bold(self):
        nodes = [TextNode("Hello, *World*!", TextType.TEXT)]
        new_nodes = split_nodes_delimiter(nodes, "*", TextType.BOLD)
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0], TextNode("Hello, ", TextType.TEXT)) 
        self.assertEqual(new_nodes[1], TextNode("World", TextType.BOLD))
        self.assertEqual(new_nodes[2], TextNode("!", TextType.TEXT))
    
    def test_split_many_bolds(self):
        nodes = [TextNode("Hello, *World*! *How* are you?", TextType.TEXT)]
        new_nodes = split_nodes_delimiter(nodes, "*", TextType.BOLD)
        self.assertEqual(len(new_nodes), 5)
        self.assertEqual(new_nodes[0], TextNode("Hello, ", TextType.TEXT)) 
        self.assertEqual(new_nodes[1], TextNode("World", TextType.BOLD))
        self.assertEqual(new_nodes[2], TextNode("! ", TextType.TEXT))
        self.assertEqual(new_nodes[3], TextNode("How", TextType.BOLD))
        self.assertEqual(new_nodes[4], TextNode(" are you?", TextType.TEXT))
    
    def test_split_wrong_encapsulate(self):
        nodes = [TextNode("Hello, *World* there is *error!", TextType.TEXT)]
        with self.assertRaises(ValueError):
            split_nodes_delimiter(nodes, "*", TextType.BOLD)
    
    def test_split_code(self):
        nodes = [TextNode("Hello, `World`!", TextType.TEXT)]
        new_nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0], TextNode("Hello, ", TextType.TEXT)) 
        self.assertEqual(new_nodes[1], TextNode("World", TextType.CODE))
        self.assertEqual(new_nodes[2], TextNode("!", TextType.TEXT))

    # split_nodes_image
    def test_split_images_solo_image(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_images_multiple_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![image 2](https://i.imgur) and another",
            TextType.TEXT,
        )

        new_nodes = split_nodes_image([node])
        
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("image 2", TextType.IMAGE, "https://i.imgur"),
                TextNode(" and another", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_images_no_images(self):
        node = TextNode(
            "This is text with an [link](https://i.imgur) and another",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual([node], new_nodes) 

    def test_split_image_with_bold_mixed(self):
        nodes = [
            TextNode("Hello ![image](https://imgur.com) World ", TextType.TEXT),
            TextNode("Something", TextType.BOLD),
        ]
        new_nodes = split_nodes_image(nodes)
        self.assertListEqual(
            [
                TextNode("Hello ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://imgur.com"),
                TextNode(" World ", TextType.TEXT),
                TextNode("Something", TextType.BOLD),
            ],
            new_nodes,
        )
    
    # split_nodes_link
    def test_split_links_solo_link(self):
        node = TextNode("This is text with a [link](https://i.imgur) and another", TextType.TEXT)        
        new_nodes = split_nodes_link([node])    
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://i.imgur"),
                TextNode(" and another", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_text_with_two_links(self):
        node = TextNode(
            "This is text with a [link](https://i.imgur) and another [link](https://i.imgur)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://i.imgur"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://i.imgur"),
            ],
            new_nodes,
        )
    
    def test_split_links_no_links(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur) and another",
            TextType.TEXT,
        )   

        new_nodes = split_nodes_link([node])
        self.assertListEqual([node], new_nodes)
        
    