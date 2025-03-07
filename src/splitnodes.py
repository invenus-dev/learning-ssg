from textnode import TextNode, TextType
from extractmarkdownimages import extract_markdown_images
from extractmarkdownlinks import extract_markdown_links

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            # find any delimiter enveloped text and extract it
            parts = node.text.split(delimiter)
            if len(parts) == 1:
                new_nodes.append(node)
            else:
                # even number of parts is wrong
                if len(parts) % 2 == 0:
                    raise ValueError("Invalid delimiter count")
                else:
                    # add the first part as a normal text node
                    for i, value in enumerate(parts):
                        if i % 2 == 0:
                            new_nodes.append(TextNode(value, TextType.TEXT))
                        else:
                            new_nodes.append(TextNode(value, text_type))                    
        else: 
            new_nodes.append(node)        
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        images = extract_markdown_images(original_text)
        if not images:
            new_nodes.append(old_node)
            continue        
        for image in images:                
            image_alt = image[0]
            image_path = image[1]
            sections = original_text.split(f"![{image_alt}]({image_path})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid image detected")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_path))
            original_text = sections[1]                            
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))        
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        links = extract_markdown_links(original_text)
        if not links:
            new_nodes.append(old_node)
            continue        
        for link in links:                
            link_text = link[0]
            link_url = link[1]
            sections = original_text.split(f"[{link_text}]({link_url})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid link detected")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(link_text, TextType.LINK, link_url))
            original_text = sections[1]                            
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))        
    return new_nodes