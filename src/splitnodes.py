from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.NORMAL:
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
                            new_nodes.append(TextNode(value, TextType.NORMAL))
                        else:
                            new_nodes.append(TextNode(value, text_type))                    
        else: 
            new_nodes.append(node)        
    return new_nodes