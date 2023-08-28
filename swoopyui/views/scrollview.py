from .subviewparent import SubViewParent



ScrollModeVertical = "vertical"
ScrollModeHorizontal = "horizontal"


class ScrollView (SubViewParent):
    """"""
    def __init__(self, scrollMode:ScrollModeVertical="vertical") -> None:
        super().__init__()

        self.scrollMode = scrollMode

        self.vdata.update({
            "name" : "ScrollView"
        })

        self.vdata['props'].update({
            "scrollMode" : self.scrollMode
        })
    

    def update(self):
        self.vdata['props'].update({
            "scrollMode" : self.scrollMode
        })
        return super().update()