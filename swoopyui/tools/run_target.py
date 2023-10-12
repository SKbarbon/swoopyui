import traceback, swoopyui





def run_the_target (target_function, function_args):
    try:
        target_function(*function_args)
    except Exception as e:
        client_view : swoopyui.View = function_args[0]
        client_view.push_error_message(str(e))
        traceback.print_exc()
        raise Exception(e)