import re

def extract_markdown_links(text):
  regex = r"(?<!!)\[([^\]\[]*)\]\(([^\)\()]*)\)"
  return re.findall(regex, text)