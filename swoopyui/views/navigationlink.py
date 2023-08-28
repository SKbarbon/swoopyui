from .subviewparent import SubViewParent
from .subview import SubView


class NavigationLink (SubViewParent):
    def __init__(self) -> None:
        super().__init__()

        self.vdata.update({
            "name" : "NavigationLink",
            "sub_views2": []
        })
    
    def add_to_destination (self, subviews:list):
        """Add new subview to the navigated destination."""
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