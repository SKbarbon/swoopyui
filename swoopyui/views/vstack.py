from .subviewparent import SubViewParent



class VStack (SubViewParent):
    """Align the subviews in a parent stack verticaly."""
    def __init__(self) -> None:
        super().__init__()

        self.vdata.update({
            "name" : "VStack"
        })