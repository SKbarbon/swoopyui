from .subview import SubView
from ..tools.on_action import on_view_action



class LabeledButton (SubView):
    """
    A standard button with a label for user interface items, consisting of an icon with a title.
    
    You can browse all the available icons on:
    [Apple SF symbols](https://developer.apple.com/sf-symbols/)
    """
    def __init__(self, content:str="Hello, label!", icon_name:str="globe.europe.africa", color:str="primery", icon_color:str="primery", size:int=18, icon_size:int=18, on_click=None) -> None:
        super().__init__()

        self.content : str = content
        self.icon_name : str = icon_name
        self.color : str = color
        self.icon_color : str = icon_color
        self.size : int = size
        self.icon_size : int = icon_size
        self.on_click = on_click

        self.vdata.update({
            "name" : "LabeledButton",
            "props" : {
                "content" : self.content,
                "icon_name" : self.icon_name,
                "color" : self.color,
                "icon_color" : self.icon_color,
                "size" : self.size,
                "icon_size" : self.icon_size
            }
        })
    
    def on_event (self, event_content:dict):
        if event_content['name'] == "on_click":
            on_view_action(self.on_click, [self])
    
    def update(self):
        self.vdata.update({
            "name" : "LabeledButton",
            "props" : {
                "content" : self.content,
                "icon_name" : self.icon_name,
                "color" : self.color,
                "icon_color" : self.icon_color,
                "size" : self.size,
                "icon_size" : self.icon_size
            }
        })
        return super().update()