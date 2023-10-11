# Menus
Swoopyui supports two kind of subview menu, the `Menu` and `ContextMenu` classes.

An example of a menu.
<img width="500" alt="Screenshot 2023-08-29 at 4 46 45 PM" src="https://miro.medium.com/v2/resize:fit:1096/format:webp/1*vOzJbA5PNgZpUV7BZ6LNkg.png">


The main difference between a `Menu` and `ContextMenu` is that the `Menu` contains a text label as a menu initializer, also it can be initialized by just a simple click at the label. The `ContextMenu` contains a customizeable subview as a label initializer, also to initialize the `ContextMenu`, you need to long-press it instead of just click.

## `Menu` properties
### `title`
Set the title of the menu label initializer.

## `Menu` methods
### `add(subviews:list)`
Add subviews to the menu childrens.

## `ContextMenu` methods
### `add(subviews:list)`
Add subviews to act like a `ContextMenu` initializer label.

### `add_to_context_menu(subviews:list)`
Add subviews to the `ContextMenu` childerns.