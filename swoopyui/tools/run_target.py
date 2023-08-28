import traceback





def run_the_target (target_function, function_args):
    try:
        target_function(*function_args)
    except Exception as e:
        traceback.print_exc()
        raise Exception(e)