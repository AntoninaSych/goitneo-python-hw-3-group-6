def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            print(str(e))
        except KeyError:
            print("User not exist. Please provide valid data.")
        except IndexError:
            print("Please  check your input.")

    return inner
