

class WebView (object):
    """
    A view that adds a web page to your view.

    Its custom WebView built using the github package:

    https://github.com/danielsaidi/WebViewKit.git
    """
    def __init__(self, value:str, resizeable:bool=False, width:float|int=150, height:float|int=150) -> None:
        self.__last_view_id = None # This is used becuase swiftUI will not know that this updated without it
        self.__id = None
        self.__mother_view = None
        self.__parent_view = None

        self.__value = value
        self.__resizeable = resizeable
        self.__width = width
        self.__height = height
    

    def get_dict_content (self):
        return {
            "last_view_id" : self.__last_view_id,
            "view_id" : self.__id,
            "vname" : "WebView",
            "value" : self.__value,
            "resizeable" : self.__resizeable,
            "width" : self.__width,
            "height" : self.__height
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
        if action_name == "on_hover":
            hover_state = action_data['hover_state']
            # on_view_action(self.on_hover, [self, {"state":hover_state}])
    
    @property
    def id (self):
        return self.__id

    @property
    def value (self): return self.__value

    @value.setter
    def value (self, value):
        if self.__mother_view == None:
            raise Exception("Cannot change the sub_view property while its not on the screen.")
        
        self.__value = value
        self.__id = self.__mother_view.get_new_view_id()
        self.__mother_view.update(self)
        self.__last_view_id = self.__id
    
    @property
    def resizeable(self): return self.__resizeable

    @resizeable.setter
    def resizeable(self, value):
        if self.__mother_view == None:
            raise Exception("Cannot change the sub_view property while its not on the screen.")
        
        self.__resizeable = value
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
        
        try:
            int(value)
        except:
            raise ValueError(f"height must be a number")
        
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
        
        try:
            int(value)
        except:
            raise ValueError(f"height must be a number")
        
        self.__height = value
        self.__id = self.__mother_view.get_new_view_id()
        self.__mother_view.update(self)
        self.__last_view_id = self.__id