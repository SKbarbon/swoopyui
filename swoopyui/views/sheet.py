from .subviewparent import SubViewParent



class Sheet (SubViewParent):
    """A """
    def __init__(self, presented:bool=False) -> None:
        super().__init__()

        self.presented = presented

        self.vdata.update({
            "name" : "Sheet",
            "props" : {
                "presented" : presented
            }
        })
    

    def update(self):
        self.vdata.update({
            "name" : "Sheet",
            "props" : {
                "presented" : self.presented
            }
        })
        return super().update()