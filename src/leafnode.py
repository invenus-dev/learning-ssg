from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        if not value:
            raise ValueError("value cannot be empty")
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if not self.tag:
            return self.value
        props_string = self.props_to_html()
        if(props_string != ""):
            props_string = " " + props_string            
        return f"<{self.tag}{props_string}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"