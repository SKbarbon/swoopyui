import swoopyui


def main (view:swoopyui.View):
    def vc(cls):
        tt.content = "Yeaaaah!"
        tt.update()
    nav = swoopyui.NavigationStack("I am styack!")
    view.add(nav)

    nl = swoopyui.NavigationLink()
    nav.add([
        swoopyui.Text("GG"),
        nl
    ])

    nl.add([swoopyui.Text("Go to dest!")])
    tt = swoopyui.Text("I am in dist!")

    vstk = swoopyui.VStack()
    nl.add_to_destination([vstk])

    vstk.add([
        tt,
        swoopyui.TextButton("Change that dear!", on_click=vc)
    ])

swoopyui.app(target=main, for_preview=True)