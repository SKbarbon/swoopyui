from .subviewparent import SubViewParent




class ScrollingTabView (SubViewParent):
    """A scrolling tabview for multi-page on scroll"""
    def __init__(self) -> None:
        super().__init__()


        self.vdata.update({
            "name" : "ScrollingTabView"
        })
    
    def navigate_to_subview (self, subview_id:int):
        if self.main_view != None:
            self.main_view.subview_reverse_event({
                "action" : "tabview_selection",
                "parent_id" : self.id,
                "subview_id" : subview_id
            })