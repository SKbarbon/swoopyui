import swoopyui

def main (view:swoopyui.View):
    def on_c (cls:swoopyui.ElevatedButton):
        print("Here!")
        testing_label.content = str("No its two!")
        testing_label.update()
    
    nav = swoopyui.NavigationStack("Try effect!")
    view.add(nav)

    nl = swoopyui.NavigationLink()
    nav.add([nl])

    nl.add([
        swoopyui.Text("Go to testing page!")
    ])

    testing_label = swoopyui.Text("One?")
    vt = swoopyui.VStack()
    nl.add_to_destination([vt])

    vt.add([
        testing_label,
        swoopyui.ElevatedButton("Change", on_click=on_c)
    ])

    nl.update()