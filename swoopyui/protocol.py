from .views.subview import SubView



class onAddNewSubViewRequest:
    def __init__(self, subview:SubView) -> None:
        if subview.parent_view == None: return

        to_id = ""
        if subview.parent_view == subview.main_view:
            to_id = "main"
        else:
            to_id = str(subview.parent_view.id)

        self.raw = {
            "action" : "add_subview",
            "to_id" : to_id,
            "subview_data" : subview.vdata
        }


class onUpdateSubviewProps:
    def __init__(self, subview:SubView) -> None:
        self.raw = {
            "action" : "update_subview",
            "subview_data" : subview.vdata
        }
    