from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if not self.tag:
            raise ValueError("tag cannot be empty")
        if not self.children:
            raise ValueError("children cannot be empty")        
        
        children_strings = []
        for child in self.children:
            children_strings.append(child.to_html())
        children_html = "".join(children_strings)

        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"
    
    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props})"