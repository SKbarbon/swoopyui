# swoopyui
swoopyui is a python library that enable developers to easily build swiftUI apps only in python. Its not need any swiftUI experience.

| Platforms   | Support     |
| ----------- | ----------- |
| MacOS       |     ✅      |
| iOS & iPadOS|     ✅      |
| AppleTV     |     🚧      |
| AppleVision  |     ✅      |

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

app(target=main, base_name=__name__)
```

Are you ok now 🙃 ? Lets start with the docs:

- [The docs](https://github.com/SKbarbon/swoopyui/wiki)

## Publishing
1. Using xcode.

You can use the xcode project template to publish to iOS, iPadOS, Mac (Designed for iPad) and Apple Vision (Designed for iPad) all of that by one project.
Follow the guidelines here: [soon]()

2. Using pyinstaller (For mac only).

You can use this approach for faster publishing, but its not recomended becuase swoopyui does not fully support it, thats why it will work but so much slower at the starting.
## ⚠️ help and contribute wanted!!
- A Secure connection strategy.

Thanks, good luck..
