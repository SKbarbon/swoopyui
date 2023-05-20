from ..tools.on_action import on_view_action




class TextField (object):
    def __init__(self, text:str="", placeholder:str="", width=200, height=40, 
        foreground_color="primery", on_change=None, on_submit=None) -> None:
        self.__last_view_id = None # This is used becuase swiftUI will not know that this updated without it
        self.__id = None
        self.__mother_view = None
        self.__parent_view = None

        self.__text = text
        self.__placeholder = placeholder
        self.__width = width
        self.__height = height
        self.__foreground_color = foreground_color
        self.on_change = on_change
        self.on_submit = on_submit

    def get_dict_content (self):
        return {
            "last_view_id" : self.__last_view_id,
            "view_id" : self.__id,
            "vname" : "TextField",
            "text" : self.text,
            "placeholder" : self.placeholder,
            "width" : self.width,
            "height" : self.height,
            "fgcolor" : self.foreground_color
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


    def view_action (self, action_data):
        action_name = action_data['action_name']
        if action_name == "on_change":
            self.__text = action_data['text']
            on_view_action(self.on_change, [self])
        elif action_name == "on_submit":
            self.__text = action_data['text']
            on_view_action(self.on_submit, [self])

    @property
    def id (self):
        return self.__id
    
    @property
    def text (self):
        return self.__text
    
    @text.setter
    def text (self, value):
        if self.__mother_view == None:
            raise Exception("Cannot change the sub_view property while its not on the screen.")
        
        self.__text = value
        self.__id = self.__mother_view.get_new_view_id()
        self.__mother_view.update(self)
        self.__last_view_id = self.__id
    

    @property
    def placeholder (self):
        return self.__placeholder
    
    @placeholder.setter
    def placeholder (self, value):
        if self.__mother_view == None:
            raise Exception("Cannot change the sub_view property while its not on the screen.")
        
        self.__placeholder = value
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
    
    @property
    def foreground_color (self): return self.__foreground_color

    @foreground_color.setter
    def foreground_color (self, value):
        if self.__mother_view == None:
            raise Exception("Cannot change the sub_view property while its not on the screen.")
        
        self.__foreground_color = value
        self.__id = self.__mother_view.get_new_view_id()
        self.__mother_view.update(self)
        self.__last_view_id = self.__id