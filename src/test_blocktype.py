import unittest

from blocktype import BlockType, block_to_block_type

class TestBlockType(unittest.TestCase):
    def test_block_to_block_type_heading(self):
        block = "# Hello, World!"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
    
    def test_block_to_block_type_heading6(self):
        block = "###### Hello, World!"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
    
    def test_block_to_block_type_wrong_heading(self):
        block = "####### Hello, World!"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_block_to_block_type_heading_multiline(self):
        block = "# Hello, World!\nBze Bold"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

    def test_block_to_block_type_code_multiline(self):
        block = "```python\nprint('Hello, World!')\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    def test_block_to_block_type_quote(self):
        block = "> Hello, World!"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
    
    def test_block_to_block_type_quote_multiline(self):
        block = "> Hello, World!\nSome. split"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
  
    def test_block_to_block_type_unordered_list(self):
        block = "- Hello, World!"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)
    
    def test_block_to_block_type_unordered_list_multiline(self):
        block = "- Hello, World!\n- Bingo, mod!"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)

    def test_block_to_block_type_ordered_list(self):
        block = "1. Hello, World!\n2. Hello, World 2!"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)
    
    def test_block_to_block_type_ordered_list_wrong(self):
        block = "1. Hello, World!\n3. Hello, World 2!"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_block_to_block_type_paragraph(self):
        block = "Hello, World!"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)