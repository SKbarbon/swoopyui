




class AnimatedView (object):
    """A container that presents rows of data arranged in a single column, optionally providing the ability to select one or more members."""
    def __init__(self, resizeable:bool=False, width:float|int=150, height:float|int=150) -> None:
        self.__last_view_id = None # This is used becuase swiftUI will not know that this updated without it
        self.__id = None
        self.__parent_view = None
        self.__mother_view = None

        self.__subviews = []
        self.__resizeable = resizeable
        self.__width = width
        self.__height = height
    
    def get_dict_content (self):
        all_sub_views = []
        for sv in self.__subviews:
            all_sub_views.append(sv.get_dict_content())
        return {
            "last_view_id" : self.__last_view_id,
            "view_id" : self.__id,
            "vname" : "AnimatedView",
            "sub_views" : all_sub_views,
            "resizeable" : self.resizeable,
            "width" : self.width,
            "height" : self.height
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
        if self.__mother_view == None:
            raise Exception("Cannot add sub-views while this view not have an active mother view.")
        
        for subv in sub_view:
            subv.respown (new_id=self.__mother_view.get_new_view_id(), mother_view=self.__mother_view, parent=self)
            self.__mother_view.sub_views_history.append(subv)
            self.__subviews.append(subv)
    

    def update (self):
        self.__id = self.__mother_view.get_new_view_id()
        self.__mother_view.update(self)
        self.__last_view_id = self.__id

        self.__parent_view.update()
    
    @property
    def id (self):
        return self.__id
    
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