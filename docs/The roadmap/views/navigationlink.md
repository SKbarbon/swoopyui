# NavigationLink
NavigationLink is a subview that provides a way to navigate to a new page. Its a tool that user control it.

Note: `NavigationLink` does not do its job outside of a [`Navigation`](https://github.com/SKbarbon/swoopyui/blob/main/docs/The%20roadmap/views/navigations.md).

## methods
#### `.add(subviews:list)`
Add a list of subviews to act as a label of the navigationlink.


#### `.add_to_destination(subviews:list)`
Add a list of subviews to the destination page that the user will navigate to.

**`Note`**: Its highly recomended to not put all of your subviews directly in the NavigationLink using the this `add_to_destination` method. Instead, add your subviews to another subview such as VStack then add the VStack to the navigationlink. If you not, maybe you will face issues where the navigationlink does not updating the subviews after you push an update event. Example:
```python
import swoopyui

def main (view:swoopyui.View):
    # ... your app logic ...

    # Create an Instance of the NavigationLink
    subpage_link = swoopyui.NavigationLink()
    nav.add([subpage_link])

    # make the label of your NavigationLink
    subpage_link.add([
        swoopyui.Text("Go to page2!")
    ])

    # build your page2
    vstack = swoopyui.VStack()
    subpage_link.add_to_destination([vstack])

    vstack.add([
        swoopyui.Text("Welcome to page2!")
    ])
```