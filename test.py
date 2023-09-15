import swoopyui

def main (view:swoopyui.View):
    swoopyui.NavigationStack()
    nav = swoopyui.NavigationSplitView(
        title="My Navigation!"
    )
    view.add(nav)

    nav.add([
        swoopyui.Text("A text in a nav!")
    ])

swoopyui.app(target=main)