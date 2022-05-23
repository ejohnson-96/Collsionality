import constants as const
from core.variables import char_man as cm
from core.variables import string_man as sm
from system import fonts as font
from system import controller as ctrl



ic = const.initialise_constants()

x = font.list_fonts()
y = x['name'][10]
print(y)





test = 'fsfjflsj i09sdflkj'
y = cm.nato_alphabet(test, False)
print(y)




i = 0
north = 1
while i < 1:
    if north > 10:
        i = 1
    else:
        x = ctrl.user_input()
        ctrl.navigation(x, north)

print(north)


