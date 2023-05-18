





def run_the_target (target_function, function_args, app_class):
    try:
        target_function(*function_args)
    except Exception as e:
        app_class.set_for_the_next_update_get("error", {"error_describe":f"Error: {str(e)}"})
        raise Exception(e)