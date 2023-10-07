from .subview import SubView




class SubViewParent (SubView):
    """The `SubViewParent` is a subview that have the abiliy to add another subviews inside it."""
    def __init__(self) -> None:
        super().__init__()

        self.subviews = []
        self.vdata.update({
            "sub_views" : [],
            "sub_views2" : [],
            "sub_views3" : [],
            "sub_views4" : []
        })
    

    def add (self, subviews:list):
        """Add a new subview to this view."""
        if self.parent_view == None or self.main_view == None: return

        for subview in subviews:
            subview.respown(
                new_id=self.main_view.get_new_subview_id(),
                update_id=self.main_view.get_new_subview_update_id(),
                parent_view=self,
                main_view=self.main_view
            )
            self.subviews.append(subview)
            self.vdata['sub_views'].append(subview.vdata)

            self.main_view.add_to_subviews_history(subview)
        self.update()
    


    def replace_subview_by_subviewclass (self, subview_class:SubView, new_subview_class:SubView):
        """"""
        pass


    def update(self):
        return super().update()