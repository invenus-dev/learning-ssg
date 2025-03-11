import re
import os

from markdown2html import markdown_to_html_node

def extract_title(markdown_text):
  """Extract title from H1 from markdown file"""
  lines = markdown_text.split('\n')
  for i, line in enumerate(lines):
    if re.match(r'^# ', line):
      # Found an H1 header - extract just the text after the #
      return line.lstrip('# ').strip()  
  return None

def generate_page(from_path, template_path, dest_path, basepath):
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
  # replace basepath instances in the template
  template_text = template_text.replace('href="/', f'href="{basepath}')
  template_text = template_text.replace('src="/', f'src="{basepath}')

  # write the generated page to the destination
  # create directory if not exists
  dest_dir = '/'.join(dest_path.split('/')[:-1])
  os.makedirs(dest_dir, exist_ok=True)
  
  with open(dest_path, 'w') as f:
    f.write(template_text)
  
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
  """Generate all pages in a directory and its subdirectories"""
  entries = os.listdir(dir_path_content)
  for entry in entries:
    full_path = os.path.join(dir_path_content, entry)
    if os.path.isdir(full_path):
      # Recurse into the directory
      full_dest_path = os.path.join(dest_dir_path, entry)
      generate_pages_recursive(full_path, template_path, full_dest_path, basepath)
    elif entry.endswith('.md'):
      # Generate the page
      dest_path = os.path.join(dest_dir_path, entry.replace('.md', '.html'))      
      generate_page(full_path, template_path, dest_path, basepath)