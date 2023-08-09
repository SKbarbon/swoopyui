import swoopyui


def main (view:swoopyui.View):
    def on_hover (cls:swoopyui.Text, obj):
        if obj['state'] == 'true':
            cls.foreground_color = "red"
        else:
            cls.foreground_color = "white"
    scrollview = swoopyui.ScrollView()
    view.add(scrollview)

    for i in range(100):
        scrollview.add(swoopyui.Text(f"{i}", on_hover=on_hover))
    scrollview.update()

swoopyui.app(target=main)