from ..tools.on_action import on_view_action


class NavigationSplitView (object):
    """
    A view that presents views in two or three columns, where selections in leading columns control presentations in subsequent columns.
    """
    def __init__(self, title:str="", support_content:bool=False, content_title:str="", detail_view_title:str="") -> None:
        self.__last_view_id = None # This is used becuase swiftUI will not know that this updated without it
        self.__id = None
        self.__parent_view = None
        self.__mother_view = None

        self.__title = title
        self.detail_view_title =  detail_view_title
        self.support_content = support_content
        self.content_title = content_title

        self.__subviews = []
        self.__detailviews = []
        self.__contentviews = []
    
    def get_dict_content (self):
        all_sub_views = []
        all_detail_views = []
        all_content_views = []
        for sv in self.__subviews:
            all_sub_views.append(sv.get_dict_content())
        
        for detv in self.__detailviews:
            all_detail_views.append(detv.get_dict_content())
        
        for conv in self.__contentviews:
            all_content_views.append(conv.get_dict_content())
        return {
            "last_view_id" : self.__last_view_id,
            "view_id" : self.__id,
            "vname" : "NavigationSplitView",
            "title" : self.__title,
            "sub_views" : all_sub_views,
            "support_navigationsplitview_content" : self.support_content,
            "detail_views" : all_detail_views,
            "content_views" : all_content_views,
            "detail_view_title" : self.detail_view_title,
            "navigationsplitview_content_title" : self.content_title
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
        """Add a new subview to be inside this NavigationStack."""
        if self.__mother_view == None:
            raise Exception("Cannot add sub-views while this view not have an active mother view.")
        
        for subv in sub_view:
            subv.respown (new_id=self.__mother_view.get_new_view_id(), mother_view=self.__mother_view, parent=self)
            self.__mother_view.sub_views_history.append(subv)
            self.__subviews.append(subv)
    
    def add_content_view (self, *content_view):
        """If `support_content = True`, then you can use this function to add new views to the content section"""
        if self.__mother_view == None:
            raise Exception("Cannot add sub-views while this view not have an active mother view.")
        
        for conv in content_view:
            conv.respown (new_id=self.__mother_view.get_new_view_id(), mother_view=self.__mother_view, parent=self)
            self.__mother_view.sub_views_history.append(conv)
            self.__contentviews.append(conv)
    
    def add_detail_view (self, *detail_view):
        """Add a subview to the detailt section"""
        if self.__mother_view == None:
            raise Exception("Cannot add sub-views while this view not have an active mother view.")
        
        for detv in detail_view:
            detv.respown (new_id=self.__mother_view.get_new_view_id(), mother_view=self.__mother_view, parent=self)
            self.__mother_view.sub_views_history.append(detv)
            self.__detailviews.append(detv)
    
    def view_action (self, action_data):
        action_name = action_data['action_name']
        if action_name == "on_appear":
            on_view_action(self.on_appear, [self])
    
    def update (self):
        self.__id = self.__mother_view.get_new_view_id()
        self.__mother_view.update(self)
        self.__last_view_id = self.__id

        self.__parent_view.update()
    
    @property
    def id (self):
        return self.__id
    
    @property
    def title (self): return self.__title

    @title.setter
    def title (self, value):
        if self.__mother_view == None:
            raise Exception("Cannot change the sub_view property while its not on the screen.")
        
        self.__title = value
        self.__id = self.__mother_view.get_new_view_id()
        self.__mother_view.update(self)
        self.__last_view_id = self.__id