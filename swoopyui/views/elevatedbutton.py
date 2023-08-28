from .subview import SubView
from ..tools.on_action import on_view_action


class ElevatedButton (SubView):
    """A button with a text and background color."""
    def __init__(self, content:str, color:str="white", bgcolor:str="blue", width:int=80, height:int=40, corner_radius:int=12, on_click=None) -> None:
        super().__init__()

        self.content : str = content
        self.color : str = color
        self.bgcolor : str = bgcolor
        self.width : int = width
        self.height : int = height
        self.corner_radius : int = corner_radius
        self.on_click = on_click

        self.vdata.update({
            "name" : "ElevatedButton"
        })

        self.vdata['props'].update({
            "content" : self.content,
            "color" : self.color,
            "bgcolor" : self.bgcolor,
            "width" : self.width,
            "height" : self.height,
            "corner_radius" : self.corner_radius
        })
    

    def on_event (self, event_content:dict):
        if event_content['name'] == "on_click":
            on_view_action(self.on_click, [self])

    
    def update(self):
        self.vdata['props'].update({
            "content" : self.content,
            "color" : self.color,
            "bgcolor" : self.bgcolor,
            "width" : self.width,
            "height" : self.height,
            "corner_radius" : self.corner_radius
        })
        return super().update()