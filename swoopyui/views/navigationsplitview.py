from .subviewparent import SubViewParent
from .subview import SubView



class NavigationSplitView (SubViewParent):
    """A view that presents views in two or three columns, where selections in 
    leading columns control presentations in subsequent columns."""
    def __init__(self, title:str="", detail_title:str="") -> None:
        super().__init__()

        self.title : str = title
        self.detail_title : str = detail_title

        self.vdata.update({
            "name" : "NavigationSplitView",
            "sub_views2" : [],
            "sub_views3" : [],
            "sub_views4" : []
        })

        self.vdata['props'].update({
            "title" : title,
            "detail_title" : detail_title
        })
    
    def add_to_detail (self, subviews:list):
        """Add new subview to the second column of the navigationview."""
        if self.parent_view == None or self.main_view == None: return

        for subview in subviews:
            subview.respown(
                new_id=self.main_view.get_new_subview_id(),
                update_id=self.main_view.get_new_subview_update_id(),
                parent_view=self,
                main_view=self.main_view
            )
            self.subviews.append(subview)
            self.vdata['sub_views2'].append(subview.vdata)
            self.main_view.add_to_subviews_history(subview)
        self.update()
    
    def add_to_toolbar (self, subviews:list):
        """Add subviews in toolbar."""
        if self.parent_view == None or self.main_view == None: return

        for subview in subviews:
            subview.respown(
                new_id=self.main_view.get_new_subview_id(),
                update_id=self.main_view.get_new_subview_update_id(),
                parent_view=self,
                main_view=self.main_view
            )
            self.subviews.append(subview)
            self.vdata['sub_views3'].append(subview.vdata)
            self.main_view.add_to_subviews_history(subview)
        self.update()
    

    def add_to_detail_toolbar (self, subviews:list):
        """Add to detail page toolbar."""
        if self.parent_view == None or self.main_view == None: return

        for subview in subviews:
            subview.respown(
                new_id=self.main_view.get_new_subview_id(),
                update_id=self.main_view.get_new_subview_update_id(),
                parent_view=self,
                main_view=self.main_view
            )
            self.subviews.append(subview)
            self.vdata['sub_views4'].append(subview.vdata)
            self.main_view.add_to_subviews_history(subview)
        self.update()
    
    def update(self):
        self.vdata['props'].update({
            "title" : self.title,
            "detail_title" : self.detail_title
        })
        return super().update()