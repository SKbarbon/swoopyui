




class ScrollView (object):
    """
    A scrollable view.

    The `scroll_to_view_id` property is used to make the scrollview auto-scroll into a
    specific subview using its `id`.

    The `scroll_mode` property used to set a scroll stack mode, put `v` as Vertical, or `h` as Horizontal.
    """
    def __init__(self, scroll_to_view_id:int=None, scroll_mode:str="v") -> None:
        self.__last_view_id = None # This is used becuase swiftUI will not know that this updated without it
        self.__id = None
        self.__mother_view = None
        self.__parent_view = None

        self.__scroll_to_view_id = scroll_to_view_id
        self.__scroll_mode = scroll_mode
        self.__subviews = []
    

    def get_dict_content (self):
        all_sub_views = []
        for sv in self.__subviews:
            all_sub_views.append(sv.get_dict_content())
        return {
            "last_view_id" : self.__last_view_id,
            "view_id" : self.__id,
            "vname" : "ScrollView",
            "scroll_to_view_id" : self.__scroll_to_view_id,
            "scroll_mode" : self.__scroll_mode,
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
        """Add a new subview to be inside this StackView."""
        if self.__mother_view == None:
            raise Exception("Cannot add sub-views while this view not have an active mother view.")
        
        for subv in sub_view:
            subv.respown (new_id=self.__mother_view.get_new_view_id(), mother_view=self.__mother_view, parent=self)
            self.__mother_view.sub_views_history.append(subv)
            self.__subviews.append(subv)
    

    def update (self):
        """Update the StackView, You mostly wont use it, except after `.add` function."""
        self.__id = self.__mother_view.get_new_view_id()
        self.__mother_view.update(self)
        self.__last_view_id = self.__id

        self.__parent_view.update()
    

    @property
    def id (self):
        return self.__id
    

    @property
    def scroll_to_view_id (self):
        return self.__scroll_to_view_id
    
    @scroll_to_view_id.setter
    def scroll_to_view_id (self, value:int):
        if self.__mother_view == None:
            raise Exception("Cannot change the sub_view property while its not on the screen.")
        
        self.__scroll_to_view_id = value
        self.__id = self.__mother_view.get_new_view_id()
        self.__mother_view.update(self)
        self.__last_view_id = self.__id
    

    @property
    def scroll_mode (self):
        return self.__scroll_mode
    
    @scroll_mode.setter
    def scroll_mode (self, value):
        if self.__mother_view == None:
            raise Exception("Cannot change the sub_view property while its not on the screen.")
        
        self.__scroll_mode = value
        self.__id = self.__mother_view.get_new_view_id()
        self.__mother_view.update(self)
        self.__last_view_id = self.__id