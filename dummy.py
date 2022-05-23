import constants as const
from core.variables import char_man as cm
from core.variables import string_man as sm
from system import fonts as font



ic = const.initialise_constants()

x = font.list_fonts()
y = x['name'][10]
print(y)





test = 'alpha beta 123 903!'
y = cm.nato_alphabet(test)
print(y)



