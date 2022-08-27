from modules.core.loadsave import file_dir as fd
from modules.core.variables import string_man as sm, char_man as cm, num_man as nm

slash = fd.slash()


def load_generate(
        encounter,
        radius,

):

    encounter = nm.valid_int(encounter)

    parent_path = sm.slash_check(fd.dir_parent())
    parent_path = cm.remove_end(parent_path)
    name = fd.dir_name(parent_path)

    l = len(name) + 1

    for i in range(l):
        parent_path = cm.remove_end(parent_path)

    path = sm.jwos(parent_path, slash, 'data', slash, 'save', slash)

    if encounter == 0:
        enc = 'EA'
    else:
        enc = sm.jwos('E', str(encounter))

    fd.dir_make(enc, path)

    path = sm.jwos(path, enc, slash)
    radius_dir = fd.dir_make(str(radius), path)

    return sm.jwos(path, str(radius), slash)



enc = 6
radius = 4

x = load_generate(enc, radius)
print(x)
