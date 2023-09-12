# `Text`
A view that displays one or more lines of read-only text.

## properties

1. `content`
The string content of the text.

```python
# Append it as argument
myText = swoopyui.Text(content="Hi")

# Edit it as argument
myText.content = "Hello, world"

# update the properties
myText.update()
```

2. `color`
The color of the text.


3. `size`
The font size number of the text.