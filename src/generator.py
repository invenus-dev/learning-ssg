import re

from markdown2html import markdown_to_html_node

def extract_title(markdown_text):
  """Extract title from H1 from markdown file"""
  lines = markdown_text.split('\n')
  for i, line in enumerate(lines):
    if re.match(r'^# ', line):
      # Found an H1 header - extract just the text after the #
      return line.lstrip('# ').strip()  
  return None

def generate_page(from_path, template_path, dest_path):
  """Generate a page from a markdown file and a template"""
  print(f"Generating page from {from_path} using {template_path} to {dest_path}")
  
  # reads into variable
  with open(from_path, 'r') as f:
    markdown_text = f.read()
  with open(template_path, 'r') as f:
    template_text = f.read()
  
  html_node = markdown_to_html_node(markdown_text)
  title = extract_title(markdown_text)

  # replace the title in the template
  template_text = template_text.replace('{{ Title }}', title)
  # replace the body in the template
  template_text = template_text.replace('{{ Content }}', html_node.to_html())

  # write the generated page to the destination
  with open(dest_path, 'w') as f:
    f.write(template_text)
  
