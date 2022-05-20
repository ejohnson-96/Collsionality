import os
import ctypes
import random
import string

def is_user_admin(

):
    try:
        res = (os.getuid() == 0)
    except AttributeError:
        res = ctypes.windll.shell32.IsUserAnAdmin() != 0
    return res


def list_users(

):

    return

def pwd_gen(
        len=16,
):
    min = 8

    if not isinstance(len, int):
        raise TypeError(
            "Error: Argument must be an integer."
        )

    if len < min:
        raise ValueError(
            f"Error: Integer must be greater than {min} characters."
        )
    else:
        characters = string.ascii_letters + string.punctuation  + string.digits
        password =  "".join(random.choice(characters) for x in range(random.randint(min, len)))

    return password
