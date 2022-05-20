from ..variables import string_man as sm
from PIL import Image

convert_message = 'File conversion complete.'

def png_jpg(
        file_name,
        loc,
):

    if not isinstance(loc, str):
        raise TypeError(
            "Error: Path location must be a string."
        )

    if not isinstance(file_name, str):
        raise TypeError(
            "Error: File name must be a string."
        )

    parent_path = sm.slash_check(loc)
    if file_name.endswith(".png"):
        pass
    else:
        sm.jwos(file_name, ".png")


    path = sm.jwos(parent_path, file_name)
    print(path, '8989')

    im = Image.open(path)
    target_name = sm.jwos(path,".jpg")
    rgb_im = im.convert('RGB')
    rgb_im.save(target_name)
    print(convert_message)

    return