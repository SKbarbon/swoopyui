from .subview import SubView
from ..tools.on_action import on_view_action



class TextField (SubView):
    def __init__(self, placeholder:str="", content:str="", resizeable:bool=False, width:int=100, height:int=40, color:str="primery", on_change=None) -> None:
        super().__init__()

        self.placeholder = placeholder
        self.content : str = content
        self.resizeable : bool = resizeable
        self.width : int = width
        self.height : int = height
        self.color : int = color
        self.on_change = on_change

        self.vdata.update({
            "name" : "TextField",
            "props" : {
                "content" : self.content,
                "placeholder" : self.placeholder,
                "resizeable" : self.resizeable,
                "width" : width,
                "height" : height,
                "color" : self.color
            }
        })
    
    
    def on_event (self, event_content:dict):
        if event_content['name'] == "on_change":
            self.content = str(event_content['content'])
            self.vdata['props']['content'] = str(event_content['content'])
            on_view_action(self.on_change, [self])

    def update (self):
        self.vdata.update({
            "name" : "TextField",
            "props" : {
                "content" : self.content,
                "placeholder" : self.placeholder,
                "resizeable" : self.resizeable,
                "width" : self.width,
                "height" : self.height,
                "color" : self.color
            }
        })
        super().update()