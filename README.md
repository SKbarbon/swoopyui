<img src="https://github.com/SKbarbon/swoopyui/assets/86029286/625fe4b3-095d-4369-b04d-0319537a7dfc" alt="drawing" width="120"/>
Project is NOT under maintenance anymore. I started the project for fun. And I do NOT plan to continue the work any time soon.
# swoopyui
swoopyui is a Python library that enable developers to easily build SwiftUI apps in pure Python. No SwiftUI experience is required.

| Platforms   | Support     |
| ----------- | ----------- |
| MacOS       |     ✅      |
| MacOS (Designed for iPad)  |     ✅      |
| iOS & iPadOS|     ✅      |
| Apple TV     |     🚧      |
| Apple Vision  |     🚧      |
| Apple Vision (Designed for iPad)  |     ✅      |

## Installation
Install the package:

```zsh
pip install swoopyui --upgrade
```


## Usage and Examples
swoopyui is extremely easy and has a minimal learning curve. Check out this simple `hello, world` app:

```python
from swoopyui import View, Text, app

def main (view:View):
    view.add(Text("Hello, world!"))

app(target=main)
```

Learning resources:
- [Simple `swoopyui` app](https://github.com/SKbarbon/swoopyui/blob/main/docs/The%20roadmap/simple_app.md)
- [Subviews](https://github.com/SKbarbon/swoopyui/blob/main/docs/The%20roadmap/subviews.md)
- [Preview and test](https://github.com/SKbarbon/swoopyui/blob/main/docs/swoopyui_preview.md)
- [Publishing and Packaging](https://github.com/SKbarbon/swoopyui/blob/main/docs/publish_to_standalone_app.md)

**For using `swoopyui` on a non-Mac device, check this [page](https://github.com/SKbarbon/swoopyui/blob/main/docs/developing_on_nonmac.md)**

## Publishing and Previewing
1. Previewing

During the development, you want to check your app in real-time to see how its behaves and look. swoopyui porovide a very awesome way to preview and test your app during and after the development.
In macOS, as soon as you run your Python script, you will get a swoopyui window with latest script changes.

For testing in iOS and other platforms, you can check this page: [swoopyui preview](https://github.com/SKbarbon/swoopyui/blob/main/docs/swoopyui_preview.md).

2. Publishing

You can deploy and publish your swoopyui project into iOS, iPadOS, macOS and visionOS applications. To read more about publishing your swoopyui script into a standalone application, read this page: [swoopyui publishing](https://github.com/SKbarbon/swoopyui/blob/main/docs/publish_to_standalone_app.md).
