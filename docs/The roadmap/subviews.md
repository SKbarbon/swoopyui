# swoopyui subviews
swoopyui support many of swiftUI views, here we call it also `subview`.

## Subview typs
- parent-subview: A subview that can also be a parent for another subview/subviews. Like `VStack` and `ScrollView`.
- subview: A view that can be ambded into a parent.

## updating subview properties
When you edit a subview properties, you must call the `update` function of the prop. For example:
```python
myText.color = "red"
myText.update()
```

## all swoopyui subviews
Here is a list of all swoopyui subviews:
- [`Text`](https://github.com/SKbarbon/swoopyui/blob/main/docs/The%20roadmap/views/Texts.md)
- [`Buttons`](https://github.com/SKbarbon/swoopyui/blob/main/docs/The%20roadmap/views/Buttons.md)
- [`Navigations`](https://github.com/SKbarbon/swoopyui/blob/main/docs/The%20roadmap/views/navigations.md)
- [`Stacks`](https://github.com/SKbarbon/swoopyui/blob/main/docs/The%20roadmap/views/stacks.md)
- [`NavigationLink`](https://github.com/SKbarbon/swoopyui/blob/main/docs/The%20roadmap/views/navigationlink.md)
- [`Menus`](https://github.com/SKbarbon/swoopyui/blob/main/docs/The%20roadmap/views/menus.md)

## To be documented
- [`List`](#to-be-documented)
- [`TextField`](#to-be-documented)
- [`Toggle`](#to-be-documented)
- [`VideoPlayer`](#to-be-documented)
- [`ScrollView`](#to-be-documented)
- [`ScrollingTabView`](#to-be-documented)
- [`Label`](#to-be-documented)
- [`Icon`](#to-be-documented)