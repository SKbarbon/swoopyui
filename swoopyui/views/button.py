from ..tools.on_action import on_view_action





class Button (object):
    """A button object. A view that make an action per click."""
    def __init__(self, text="", on_click=None, background_color="blue", width=250, height=40) -> None:
        self.__last_view_id = None # This is used becuase swiftUI will not know that this updated without it
        self.__id = None
        self.__mother_view = None
        self.__parent_view = None

        self.__text = text
        self.__width = width
        self.__height = height
        self.on_click = on_click
        self.__subviews = []
    
    def get_dict_content (self):
        all_sub_views = []
        for sv in self.__subviews:
            all_sub_views.append(sv.get_dict_content())
        return {
            "last_view_id" : self.__last_view_id,
            "view_id" : self.__id,
            "vname" : "Button",
            "text" : self.__text,
            "width" : self.__width,
            "height" : self.__height,
            "sub_views" : all_sub_views
        }
    
    def respown (self, new_id=None, mother_view=None, parent=None):
        if new_id == None: return
        if mother_view == None: return
        if parent == None: return

        if self.__id == None:
            self.__id = new_id
            self.__last_view_id = new_id
        
        if self.__mother_view == None:
            self.__mother_view = mother_view
        
        if self.__parent_view == None:
            self.__parent_view = parent
    
    def add (self, *sub_view):
        """Add new subviews to present the button. If there is no subviews the `text` will be used."""
        if self.__mother_view == None:
            raise Exception("Cannot add sub-views while this view not have an active mother view.")
        
        for subv in sub_view:
            subv.respown (new_id=self.__mother_view.get_new_view_id(), mother_view=self.__mother_view, parent=self)
            self.__mother_view.sub_views_history.append(subv)
            self.__subviews.append(subv)
        self.__id = self.__mother_view.get_new_view_id()
        self.__mother_view.update(self)
        self.__last_view_id = self.__id
    
    def view_action (self, action_data):
        action_name = action_data["action_name"]
        if action_name == "on_click":
            on_view_action(self.on_click, [self])
    
    def update (self):
        self.__id = self.__mother_view.get_new_view_id()
        self.__mother_view.update(self)
        self.__last_view_id = self.__id
        
        self.__parent_view.update()
    
    @property
    def id (self):
        return self.__id
    
    @property
    def text (self): return self.__text

    @text.setter
    def text (self, value):
        if self.__mother_view == None:
            raise Exception("Cannot change the sub_view property while its not on the screen.")
        
        self.__text = value
        self.__id = self.__mother_view.get_new_view_id()
        self.__mother_view.update(self)
        self.__last_view_id = self.__id
    

    @property
    def width (self):
        return self.__width
    
    @width.setter
    def width (self, value):
        if self.__mother_view == None:
            raise Exception("Cannot change the sub_view property while its not on the screen.")
        
        if not isinstance(value, float) or not isinstance(value, int):
            raise ValueError(f"width must be a number")
        self.__width = value
        self.__id = self.__mother_view.get_new_view_id()
        self.__mother_view.update(self)
        self.__last_view_id = self.__id
    

    @property
    def height (self):
        return self.__height
    
    @height.setter
    def height (self, value):
        if self.__mother_view == None:
            raise Exception("Cannot change the sub_view property while its not on the screen.")
        
        if not isinstance(value, float) or not isinstance(value, int):
            raise ValueError(f"height must be a number")
        self.__height = value
        self.__id = self.__mother_view.get_new_view_id()
        self.__mother_view.update(self)
        self.__last_view_id = self.__id