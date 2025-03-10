import re
from enum import Enum

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