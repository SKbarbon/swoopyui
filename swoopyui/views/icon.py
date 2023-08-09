




class Icon (object):
    """
    The Icon view is actually an image that used for `systemName` images.

    To browse all the icons, please visit: https://developer.apple.com/sf-symbols/
    """
    def __init__(self, name:str, width:float=100, height:float=100, foreground_color:str="primery") -> None:
        self.__last_view_id = None # This is used becuase swiftUI will not know that this updated without it
        self.__id = None
        self.__mother_view = None
        self.__parent_view = None

        self.__name = name
        self.__width = width
        self.__height = height
        self.__foreground_color = foreground_color
    
    def get_dict_content (self):
        return {
            "last_view_id" : self.__last_view_id,
            "view_id" : self.__id,
            "vname" : "Icon",
            "image_name" : self.__name,
            "width" : self.__width,
            "height" : self.__height,
            "fgcolor" : self.__foreground_color
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
    

    @property
    def id (self):
        return self.__id
    
    @property
    def name (self):
        return self.__name
    
    @name.setter
    def name (self, value):
        if self.__mother_view == None:
            raise Exception("Cannot change the sub_view property while its not on the screen.")
        
        self.__name = value
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