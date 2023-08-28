from .subview import SubView




class Spacer (SubView):
    def __init__(self) -> None:
        super().__init__()


        self.vdata.update({
            "name" : "Spacer"
        })