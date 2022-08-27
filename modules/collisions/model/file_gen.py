from modules.core.loadsave import file_dir as fd
from modules.core.variables import string_man as sm, char_man as cm, num_man as nm

slash = fd.slash()


def load_generate(
        encounter,
        radius,

):

    encounter = nm.valid_float(encounter)
    radius = nm.valid_float(radius)

    parent_path = sm.slash_check(fd.dir_parent())
    path = sm.jwos(parent_path, 'data', slash, 'save', slash)

    if encounter == 0:
        enc = 'EA'
    else:
        enc = sm.jwos('E', str(encounter))
    print(enc, path)
    fd.dir_make(enc, path)

    path = sm.jwos(path, enc, slash)
    radius_dir = fd.dir_make(str(radius), path)

    return sm.jwos(path, str(radius), slash)




