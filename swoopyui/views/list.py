from .subviewparent import SubViewParent



class List (SubViewParent):
    """Align the subviews in a parent stack verticaly."""
    def __init__(self) -> None:
        super().__init__()

        self.vdata.update({
            "name" : "TheListView"
        })