import unittest

from generator import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_basic_h1(self):
        """Test basic H1 extraction with single-line header"""
        markdown = "# Title 1\nContent\n\n# Title 2\nMore content"
        expected = "Title 1"
        self.assertEqual(extract_title(markdown), expected)

    def test_multiline_h1(self):
        """Test extraction of multi-line H1 header"""
        markdown = """# Title that spans
multiple lines
and continues here

Some regular content

# Another title
with multiple lines"""
        expected = "Title that spans"
        self.assertEqual(extract_title(markdown), expected)

    def test_mixed_headers(self):
        """Test with mixed header levels"""
        markdown = """# Main title
Content

## Subtitle
More content

# Second main title
More text
### Subsubtitle"""
        expected = "Main title"
        self.assertEqual(extract_title(markdown), expected)

    def test_edge_cases(self):
        """Test edge cases"""
        # Empty string
        self.assertIsNone(extract_title(""))

        # No H1 headers
        markdown = "Content\n## H2 header\nMore content"
        self.assertIsNone(extract_title(markdown))

        # H1 at end of file without newline
        markdown = "Content\n# Final H1"
        self.assertEqual(extract_title(markdown), "Final H1")

    def test_h1_with_special_chars(self):
        """Test H1 with special characters and formatting"""
        markdown = """# Title with *italic* and **bold**
Content

# Title with [link](https://example.com)
More content"""
        expected = "Title with *italic* and **bold**"
        self.assertEqual(extract_title(markdown), expected)

    def test_indented_headers(self):
        """Test with indented headers (which shouldn't be treated as headers in proper markdown)"""
        markdown = """# Real H1
Content

  # Indented text, not a header
More content"""
        expected = "Real H1"
        self.assertEqual(extract_title(markdown), expected)

if __name__ == '__main__':
    unittest.main()