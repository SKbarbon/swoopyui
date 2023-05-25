# swoopyui
swoopyui is a python library that enable developers to easily build swiftUI apps in python. Its not need any swiftUI experience with no xcode require.

## How does it work ?
It works through two parts: a Python host for managing updates and a Swift client app for the front-end. The client app stays connected to the Python back-end to receive real-time front-end updates. With swoopyui, developers can build SwiftUI apps without worrying about Swift or Xcode, because everything is handled with just Python!.

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

Are you ok now 🙃 ? fine lets start:

- [The docs](https://github.com/SKbarbon/swoopyui/wiki)

## ⚠️ help and contribute wanted!!
Hi, read the docs, be master at this, it will be quick and easy..

I want help with:
- Supporting iOS, we need to support iOS and iPadOS, so if you can help with this.
- Add a secure connection strategy between the host and client.

Thanks, good luck..
