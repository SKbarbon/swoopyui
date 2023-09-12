from ..tools.on_action import on_view_action
from .subview import SubView


class TextButton (SubView):
    """A button with a text only."""
    def __init__(self, content:str, on_click=None) -> None:
        super().__init__()

        self.content : str = content
        self.on_click = on_click

        self.vdata.update({
            "name" : "TextButton",
            "props" : {
                "content" : self.content
            }
        })
    

    def on_event (self, event_content:dict):
        if event_content['name'] == "on_click":
            on_view_action(self.on_click, [self])
    

    def update(self):
        self.vdata.update({
            "name" : "TextButton",
            "props" : {
                "content" : self.content
            }
        })
        return super().update()