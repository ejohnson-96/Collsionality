from modules.core.constants import initialise_constants
from modules.core.time import tictoc as stopwatch
from modules.core.variables import char_man as cm, bool_man as bm, num_man as nm, \
    string_man as sm
from modules.core.system import users as usr, fonts as font

stopwatch.start_time()
initialise_constants()

test_string = 'ahthsodASDjnvTksd 7823 sd 99aASFddf8!'

res = cm.capital_all_first_letter(test_string)
res = cm.nato_alphabet(res)

print(res)

pwd = usr.pwd_gen(18)
print(pwd)

z = font.font_list()
w = font.font_names()

print(w,z)

stopwatch.end_time()
