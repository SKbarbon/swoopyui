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

Start with this roadmap:
- Simple `swoopyui` app.

## Publishing
1. Using xcode.

You can use the xcode project template to publish to iOS, iPadOS, Mac (Designed for iPad) and Apple Vision (Designed for iPad) all of that by one project.
Follow the guidelines here: [soon]()
## ⚠️ help and contribute wanted!!
- A Secure connection strategy.

Thanks, good luck..
