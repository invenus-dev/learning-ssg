import unittest

from markdown2html import markdown_to_html_node

class TestMarkdown2HTML(unittest.TestCase):
  def test_simple_doc(self):
      md = """
# Hello, World!
      
This is **bolded** paragraph
text in a p
tag here

## Hello Subheading
Another line of text

This is another paragraph with _italic_ text and `code` here

"""
      node = markdown_to_html_node(md)
      html = node.to_html()

      self.assertEqual(
        html,
        "<div><h1>Hello, World!</h1><p>This is <b>bolded</b> paragraph text in a p tag here</p><h2>Hello Subheading Another line of text</h2><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
      )
  
  def test_codeblock(self):
    md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""
    node = markdown_to_html_node(md)
    html = node.to_html()

    self.assertEqual(
      html,
      "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff</code></pre></div>",
    )

  def test_list(self):
    md = """
- This here is a list
- Second item **in the list** and else

1. This is an ordered list with _some_ nested content
2. And so on
""" 
    node = markdown_to_html_node(md)
    html = node.to_html()

    self.assertEqual(
      html,
      "<div><ul><li>This here is a list</li><li>Second item <b>in the list</b> and else</li></ul><ol><li>This is an ordered list with <i>some</i> nested content</li><li>And so on</li></ol></div>",
    )
  
  def test_images_links(self):
    md = """
## Image test

Some image here ![alt text](https://www.google.com) and a link [here](https://www.google.com)
"""

    node = markdown_to_html_node(md)
    html = node.to_html()

    self.assertEqual(
      html,
      "<div><h2>Image test</h2><p>Some image here <img src=\"https://www.google.com\" alt=\"alt text\" /> and a link <a href=\"https://www.google.com\">here</a></p></div>",
    )