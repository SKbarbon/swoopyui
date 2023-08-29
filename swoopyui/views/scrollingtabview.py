from .subviewparent import SubViewParent




class ScrollingTabView (SubViewParent):
    """A scrolling tabview for multi-page on scroll"""
    def __init__(self) -> None:
        super().__init__()


        self.vdata.update({
            "name" : "ScrollingTabView"
        })