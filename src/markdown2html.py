from blocktype import BlockType, block_to_block_type, get_parent_node_from_block, get_raw_content_from_block
from leafnode import LeafNode
from parentnode import ParentNode
from transforms import markdown_to_blocks, text_node_to_html_node, text_to_textnodes

def get_child_nodes_from_block(block_type, block):
    raw_block = get_raw_content_from_block(block_type, block)

    if isinstance(raw_block, str):
        if block_type == BlockType.CODE:
          return [ParentNode("code", [LeafNode(None, raw_block, None)])]        
        else:
          text_nodes = text_to_textnodes(raw_block)
          return [text_node_to_html_node(text_node) for text_node in text_nodes]
    elif isinstance(raw_block, list):
        if block_type in [BlockType.ORDERED_LIST, BlockType.UNORDERED_LIST]:
            html_nodes = []
            for raw_block_item in raw_block:              
              html_nodes.append(ParentNode("li", [text_node_to_html_node(text_node) for text_node in text_to_textnodes(raw_block_item)]))
            return html_nodes
    else:
        raise ValueError("Invalid raw block data")

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    parent_nodes = []  

    for block in blocks:
        block_type = block_to_block_type(block)
        child_nodes = get_child_nodes_from_block(block_type, block)        
        parent_node = get_parent_node_from_block(block_type, block, child_nodes)
        parent_nodes.append(parent_node)
        
    return ParentNode("div", parent_nodes)