from .subviewparent import SubViewParent
from ..tools.on_action import on_view_action


class Button (SubViewParent):
    """A button with subviews inside it"""
    def __init__(self, width:float=100, height:float=40, corner_radius:float=12, on_click=None) -> None:
        super().__init__()

        self.vdata.update({
            "name" : "Button"
        })

        self.width : float = width
        self.height : float = height
        self.corner_radius : float = corner_radius
        self.on_click = on_click

        self.vdata['props'].update({
            "width" : self.width,
            "height" : self.height,
            "corner_radius" : self.corner_radius
        })
    

    def on_event (self, event_content:dict):
        if event_content['name'] == "on_click":
            on_view_action(self.on_click, [self])

    def update(self):
        self.vdata['props'].update({
            "width" : self.width,
            "height" : self.height,
            "corner_radius" : self.corner_radius
        })
        return super().update()