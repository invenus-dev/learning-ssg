from leafnode import LeafNode
from splitnodes import split_nodes_delimiter, split_nodes_image, split_nodes_link
from textnode import TextNode, TextType


def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    if text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    if text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    if text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    if text_node.text_type == TextType.LINK:
        if not text_node.url:
            return LeafNode(None, text_node.text)
        return LeafNode("a", text_node.text, {"href": text_node.url})
    if text_node.text_type == TextType.IMAGE:
        alt = text_node.text
        if not alt:
            alt = "Image"
        if not text_node.url:
            return LeafNode(None, alt)
        return LeafNode("img", None, {"src": text_node.url, "alt": alt})
    raise ValueError("Unknown text type")


def text_to_textnodes(text):
    start_node = TextNode(text, TextType.TEXT)
    nodes = split_nodes_delimiter([start_node], "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes

def markdown_to_blocks(markdown):
    lines = markdown.split("\n")
    if len(lines) == 0:
        return []
    final_blocks = []
    new_block_list = []
    prev_line = None    
    line = None
        
    def lines_to_final_block(lines):
        return "\n".join(lines).strip()

    for i in range(0, len(lines)):
        line = lines[i].strip()        
        if line != "":                        
            if i > 0 and prev_line == "" and len(new_block_list) > 0:
                final_blocks.append(lines_to_final_block(new_block_list))
                new_block_list = []
            new_block_list.append(line)
        prev_line = line    
    if len(new_block_list) > 0:
        final_blocks.append(lines_to_final_block(new_block_list))    
    return final_blocks
    
