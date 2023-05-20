# swoopyui
A simple python library that allow you to build swiftUI apps using python.

## How does it work ?
This library works by running python and swift at the same time!. It start a python localhost at the background and run swiftUI app that show the fron-end by communicating with python back-end host. But you should NOT worry about all of that, becuase the library always making sure that everything stay easy, simple and pythonic.

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
- Find a way to pack this library into `.app`, and fix the problem with most of packing packages.
- Add a secure connection strategy between the host and client.

Thanks, good luck..