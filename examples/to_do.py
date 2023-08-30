import swoopyui



def main (view:swoopyui.View):
    def on_add_new_task (cls):
        task = tf.content
        scroll_view.add([swoopyui.Text(f"{task}")])
        tf.content = ""
        tf.update()
    
    nav = swoopyui.NavigationSplitView("To-do")
    view.add(nav)

    top_hsatck = swoopyui.HStack()
    nav.add([top_hsatck])

    tf = swoopyui.TextField("What is your next task?")
    top_hsatck.add([
        swoopyui.Text(" "),
        tf,
        swoopyui.ElevatedButton("+", on_click=on_add_new_task),
        swoopyui.Text(" ")
    ])

    scroll_view = swoopyui.ScrollView()
    nav.add([scroll_view])


swoopyui.app(target=main)