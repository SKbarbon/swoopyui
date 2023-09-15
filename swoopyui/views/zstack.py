from .subviewparent import SubViewParent



class ZStack (SubViewParent):
    """A view that overlays its subviews, aligning them in both axes."""
    def __init__(self, padding:int=0) -> None:
        super().__init__()

        self.padding : int = padding

        self.vdata.update({
            "name" : "ZStack",
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