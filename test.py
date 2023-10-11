import swoopyui

def main (view:swoopyui.View):
    m = swoopyui.Menu("MyMenu")
    view.add(m)

    m.add([
        swoopyui.Text("Thats a menu")
    ])

swoopyui.app(target=main)