from .subviewparent import SubViewParent
from .subview import SubView



class NavigationStack (SubViewParent):
    """A view that displays a root view and enables you 
    to present additional views over the root view."""
    def __init__(self, title:str="") -> None:
        super().__init__()

        self.title : str = title


        self.vdata.update({
            "name" : "NavigationStack"
        })

        self.vdata['props'].update({
            "title" : title
        })
    
    def update(self):
        self.vdata['props'].update({
            "title" : self.title
        })
        return super().update()

    def add_to_toolbar (self, subviews:list):
        """Add a subview to the navigation toolbar"""
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