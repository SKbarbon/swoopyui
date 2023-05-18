





class View (object):
    def __init__(self, app) -> None:
        self.__app = app
        self.__next_id = 0

        # View props

    def update (self):
        pass

    def add (self, view):
        view.respown (self.__next_id)
        self.__next_id = self.__next_id + 1
        action_content = {
            "new_view_content" : view.get_dict_content()
        }
        self.__app.set_for_the_next_update_get (action_name="add_view", action_content=action_content)