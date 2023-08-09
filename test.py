import swoopyui


def main (view:swoopyui.View):
    nav = swoopyui.NavigationSplitView(title="I am nav")
    view.add(nav)

    list_of_nav = swoopyui.List()
    nav.add(list_of_nav)

    for i in range(4):
        nl = swoopyui.NavigationLink("Hi", is_presented=False)
        list_of_nav.add(nl)
        nl.add_skin_view(swoopyui.Text("Hi"))
        nl.add(swoopyui.Text(f"Number {i}"))
    
    hstack = swoopyui.Stack(swoopyui.HSTACK)
    nav.add_detail_view(hstack)
    hstack.add(
        swoopyui.Icon("globe", width=30, height=30, foreground_color="red"),
        swoopyui.Text("Helooo!")
    )
    
    nav.update()


swoopyui.app(target=main)