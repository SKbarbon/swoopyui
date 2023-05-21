from swoopyui import app, View, Stack, VSTACK, Text


def main (view:View):
    v_satck = Stack (stack_type=VSTACK) # This is a stack with Virtecal axis.
    view.add(v_satck)

    v_satck.add(
        Text("Hi") # Add new view in it.
    )
    v_satck.update() # call update becuase we add new subviews.


app (main)