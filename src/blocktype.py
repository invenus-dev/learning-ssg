import re
from enum import Enum

from parentnode import ParentNode

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    if re.search(r"^#{1,6}\s.*$", block, re.MULTILINE):
        return BlockType.HEADING
    
    if re.search(r"^`{3}.*\n[\s\S]*\n`{3}$", block, re.MULTILINE):
        return BlockType.CODE
    
    if re.search(r"^>.*$", block, re.MULTILINE):
        return BlockType.QUOTE
    
    lines = block.split("\n")    
    if all(re.search(r"^-\s+.*$", line) or line.strip() == "" for line in lines if line.strip()):
      return BlockType.UNORDERED_LIST
        
    if re.search(r"^1\.\s+.*$", lines[0]):
      is_ordered_list = True
      expected_number = 1      
      for line in lines:
        if not re.search(fr"^{expected_number}\.\s+.*$", line):
          is_ordered_list = False
          break                
        expected_number += 1            
      if is_ordered_list:
          return BlockType.ORDERED_LIST
      
    
    return BlockType.PARAGRAPH

def get_raw_content_from_block(blockType, block):
    if blockType == BlockType.HEADING:
        return block.strip("#").replace("\n", " ").strip()
    
    if blockType == BlockType.CODE:
        return block.strip("```").strip()
    
    if blockType == BlockType.QUOTE:
        return block.lstrip(">").replace("\n", " ").strip()
    
    # multiline blocks
    lines = block.split("\n")
    if blockType == BlockType.UNORDERED_LIST:
        return [line.lstrip("-").strip() for line in lines]
    
    if blockType == BlockType.ORDERED_LIST:
        return [line.lstrip("1234567890.").strip() for line in lines]
        
    return block.replace("\n", " ").strip()

def get_parent_node_from_block(blockType, block, children):
    if blockType == BlockType.HEADING:
        # determine heading level by counting initial #
        level = 0
        while block[level] == "#":
            level += 1
        if level > 0 and level <= 6:
            return ParentNode("h" + str(level), children)
        else:
            raise ValueError("Invalid heading level") 
    
    if blockType == BlockType.CODE:        
        return ParentNode("pre", children)

    if blockType == BlockType.QUOTE:
        return ParentNode("blockquote", children)
    
    if blockType == BlockType.UNORDERED_LIST:
        return ParentNode("ul", children)
    
    if blockType == BlockType.ORDERED_LIST:
        return ParentNode("ol", children)
    
    return ParentNode("p", children)

