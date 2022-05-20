import constants as const
from core.variables import char_man as cm
from core.variables import string_man as sm
from core.rw import file_converter as fc
from core.rw import file_dir as fd


ic = const.initialise_constants()


parent = fd.dir_path()
file = cm.remove_end(sm.jwos('core','\\'))

path = sm.jwos(sm.slash_check(parent),file)

print(path, 'sdfs')

fc.png_jpg(file, path)


