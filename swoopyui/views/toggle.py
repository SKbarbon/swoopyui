from .subview import SubView
from ..tools.on_action import on_view_action



class Toggle (SubView):
    """A control that toggles between on and off states."""
    def __init__(self, content:str="", active:bool=False, with_no_labels:bool=False, on_change=None) -> None:
        super().__init__()

        self.content : str = content
        self.active : bool = active
        self.with_no_labels : bool = with_no_labels

        self.on_change = on_change

        self.vdata.update({
            "name" : "Toggle",
            "props" : {
                "content" : self.content,
                "activated" : self.active,
                "with_no_labels" : self.with_no_labels
            }
        })
    

    def on_event (self, event_content:dict):
        if event_content['name'] == "on_change":
            self.active = bool(event_content['active'])
            self.vdata['props']['activated'] = bool(event_content['active'])
            on_view_action(self.on_change, [self])
    

    def update(self):
        self.vdata.update({
            "props" : {
                "content" : self.content,
                "activated" : self.active,
                "with_no_labels" : self.with_no_labels
            }
        })
        return super().update()