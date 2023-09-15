from .subviewparent import SubViewParent
from ..tools.on_action import on_view_action


class GeometryReader (SubViewParent):
    """A container view that defines its content as a 
    function of its own size and coordinate space.
    
    You can use this to get the frame size (width & height) and check resizing event.
    """
    def __init__(self, on_resize=None) -> None:
        super().__init__()

        self.__width = None
        self.__height = None

        self.on_resize = on_resize

        self.vdata.update({
            "name" : "GeometryReaderView"
        })
    

    def on_event (self, event_content:dict):
        if event_content['name'] == "on_resize":
            self.__width = int(event_content['width'])
            self.__height = int(event_content['height'])
            on_view_action(self.on_resize, [self])

    @property
    def width (self):
        return self.__width
    
    @property
    def height (self):
        return self.__height