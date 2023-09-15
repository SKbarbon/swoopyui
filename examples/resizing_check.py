import swoopyui, time


def main (view:swoopyui.View):
    def on_resize (cls:swoopyui.GeometryReader):
        width_data_label.content = f"width: {cls.width}"
        height_data_label.content = f"height: {cls.height}"

        width_data_label.update()
        height_data_label.update()

    gm = swoopyui.GeometryReader(on_resize=on_resize)
    view.add(gm)

    width_data_label = swoopyui.Text(f"width: {gm.width}")
    height_data_label = swoopyui.Text(f"height: {gm.height}")

    gm.add([
        width_data_label,
        height_data_label
    ])

swoopyui.app(target=main)