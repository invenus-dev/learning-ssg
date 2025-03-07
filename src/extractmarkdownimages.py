import re

def extract_markdown_images(text):
  regex = r"!\[([^\]\[]*)\]\(([^\)\()]*)\)"
  return re.findall(regex, text)
