import unittest

from extractmarkdownlinks import extract_markdown_links

class TestExtractMarkdownLinks(unittest.TestCase):
  def test_extract_single_link(self):
    text = "Hello, [World](https://www.example.com)!"
    self.assertEqual(extract_markdown_links(text), [("World", "https://www.example.com",)])
  
  def test_extract_link_surrounded_by_text(self):
    text = "Hello, [World](https://www.example.com) World!"
    self.assertEqual(extract_markdown_links(text), [("World", "https://www.example.com",)])
  
  def test_extract_multiple_links(self):
    text = "Hello, [World](https://www.example.com) [World](https://www.example.com)!"
    self.assertEqual(extract_markdown_links(text), [("World", "https://www.example.com",), ("World", "https://www.example.com",)])
  
  def test_does_not_match_image(self):
    text = "this is just ![an image](https://www.example.com) which should not match"
    self.assertEqual(extract_markdown_links(text), [])