# Navigations
The navigations offers a way to navigate through a hierarchy of views, transitioning from one view to another based on user actions. swoopyui support two navigation classes, `NavigationSplitView` and `NavigationStack`. They are similar at the usage but they can be used for different purposes and different scenarios..

## Peek
1. NavigationSplitView.

It provides a column of stack, main column and the details column. The new navigated page will be opened in the details column.

<img width="500" alt="Screenshot 2023-08-29 at 4 46 45 PM" src="https://www.appcoda.com/wp-content/uploads/2022/08/swiftui-splitview-twocolumn.png">


2. NavigationStack

Its provides a single stack of the navigationview. The new navigated page will be opened on top of the main column. It supports most of apple platforms.

<img width="200" alt="Screenshot 2023-08-29 at 4 46 45 PM" src="https://miro.medium.com/v2/resize:fit:660/format:webp/1*0rpggzWWD-PSTPkbIpR7Aw.png">

## usage
The uasge is very simple, this is an example of how you may use it:

```python
import swoopyui

def main (view:swoopyui.View):
    nav = swoopyui.NavigationSplitView(
        title="My Navigation!"
    )
    view.add(nav)

    nav.add([
        swoopyui.Text("A text in a nav!")
    ])

swoopyui.app(target=main)
```

## open sub page
To make the user navigate to a new page from your navigation view, use [NavigationLink](https://github.com/SKbarbon/swoopyui/blob/main/docs/The%20roadmap/views/navigations.md) class.

## properties
### title
The title of the main column of the navigation.

Support: All navigations.

### detail_title
The title of the detail column of the `NavigationSplitView`.

Support: `NavigationSplitView` only.


## methods
### function: `add_to_toolbar(subviews:list)`

Use this function to add a list of subviews in the toolbar of the navigation.

Support: All navigations.

### function: `add_to_detail_toolbar(subviews:list)`

Use this function to add a list of subviews to the details column page of the `NavigationSplitView`.

Support: NavigationSplitView only.

### function: `add(subviews:list)`
Use this function to add a list of subviews to the main column of the navigation.

Support: All navigations.

### function: `add_to_detail(subviews:list)`
Use this function to add a list of subviews to the details column page of the `NavigationSplitView` class.

Support: NavigationSplitView only.