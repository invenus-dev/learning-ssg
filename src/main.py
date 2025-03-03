from textnode import TextNode, TextType

def main():
    node = TextNode("Hello, World!", TextType.LINK, "https://www.google.com")
    print(node)

main()