from core.constants import initialise_constants
from core.time import tictoc as stopwatch
from core.variables import char_man as cm
from core.variables import string_man as sm

stopwatch.start_time()
initialise_constants()


test_string = 'this is a test string lets see if this works'

res = cm.capital_all_letter(test_string)

print(res)


stopwatch.end_time()