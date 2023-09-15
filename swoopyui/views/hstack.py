from .subviewparent import SubViewParent



class HStack (SubViewParent):
    """Align the subviews in a parent stack horizontaly."""
    def __init__(self, padding:int=0) -> None:
        super().__init__()

        self.padding : int = padding

        self.vdata.update({
            "name" : "HStack",
            "props" : {
                "padding" : self.padding
            }
        })
    
    def update (self):
        self.vdata.update({
            "props" : {
                "padding" : int(self.padding)
            }
        })
        super().update()