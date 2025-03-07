import unittest

from extractmarkdownimages import extract_markdown_images

class TestExtractMarkdownImages(unittest.TestCase):
  def test_extract_single_image(self):
    text = "![Alt text](/path/to/img.jpg)"
    self.assertEqual(extract_markdown_images(text), [("Alt text", "/path/to/img.jpg",)])

  def test_extract_image_surrounded_by_text(self):
    text = "Hello, ![Alt text](/path/to/img.jpg) World!"
    self.assertEqual(extract_markdown_images(text), [("Alt text", "/path/to/img.jpg",)])
  
  def test_extract_multiple_images(self):
    text = "![Alt text](/path/to/img1.jpg) ![Alt text](/path/to/img2.jpg)"
    self.assertEqual(extract_markdown_images(text), [("Alt text", "/path/to/img1.jpg",), ("Alt text", "/path/to/img2.jpg",)])

  def test_does_not_match_link(self):
    text = "this is just [a link](/path/to/img.jpg) which should not match"
    self.assertEqual(extract_markdown_images(text), [])