from .subviewparent import SubViewParent



class HStack (SubViewParent):
    """Align the subviews in a parent stack horizontaly."""
    def __init__(self) -> None:
        super().__init__()

        self.vdata.update({
            "name" : "HStack"
        })