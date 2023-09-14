<img src="https://github.com/SKbarbon/swoopyui/assets/86029286/625fe4b3-095d-4369-b04d-0319537a7dfc" alt="drawing" width="120"/>

# swoopyui
swoopyui is a python library that enable developers to easily build swiftUI apps only in python. Its not need any swiftUI experience.

| Platforms   | Support     |
| ----------- | ----------- |
| MacOS       |     ✅      |
| MacOS(Designed for iPad)  |     ✅      |
| iOS & iPadOS|     ✅      |
| AppleTV     |     🚧      |
| AppleVision  |     🚧      |
| AppleVision(Designed for iPad)  |     ✅      |

## installation
Enter this on terminal to install this package:

```zsh
pip install swoopyui --upgrade
```


## usage and examples
To make sure that you are not OVERTHINKING about the ease of this, Check this simple `hello, world` app:

```python
from swoopyui import View, Text, app

def main (view:View):
    view.add(Text("Hello, world!"))

app(target=main)
```

Start with this learning-roadmap:
- [Simple `swoopyui` app](https://github.com/SKbarbon/swoopyui/blob/main/docs/The%20roadmap/simple_app.md)
- [Subviews](https://github.com/SKbarbon/swoopyui/blob/main/docs/The%20roadmap/subviews.md)
- [Preview and test](https://github.com/SKbarbon/swoopyui/blob/main/docs/swoopyui_preview.md)
- [Publishing and Packaging](https://github.com/SKbarbon/swoopyui/blob/main/docs/publish_to_standalone_app.md)

## Publishing and previewing
1. Previewing

During the development, you want to real-time check your app to see how its behaves and look. Swoopyui porovide a very awesome way to preview and test your app before the development. 
In macOS, soon as you run your python script, you will get a swoopyui window with latest script changes.

For testing in iOS and other platforms, you can check this page: [swoopyui preview](https://github.com/SKbarbon/swoopyui/blob/main/docs/swoopyui_preview.md).

2. Publishing

You can deploy and publish your swoopyui project into iOS, iPadOS, macOS and visionOS. To read more about publishing your swoopyui script into a standalone application, read this page: [swoopyui publishing](https://github.com/SKbarbon/swoopyui/blob/main/docs/publish_to_standalone_app.md).

## ⚠️ help and contribute wanted!!
- A Secure connection strategy.

Thanks, good luck..
