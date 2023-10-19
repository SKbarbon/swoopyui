import swoopyui, time


def main (view:swoopyui.View):
    def on_c (cls:swoopyui.TextField):
        t.content = str(tf.content)
        t.update()
    t = swoopyui.Text("")
    view.add(t)

    tf = swoopyui.TextField("Name", on_change=on_c)
    view.add(tf)

swoopyui.app(target=main)