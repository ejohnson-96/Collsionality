from modules.core.loadsave import file_dir as fd
from modules.core.variables import string_man as sm, char_man as cm, num_man as nm


print(fd.slash())
slash = fd.slash()

valid_enc = [4,6,7]


def load_generate(
        encounter,
        radius,

):

    encounter = nm.valid_float(encounter)
    radius = nm.valid_float(radius)

    if radius > 3:
        raise ValueError(
            f"Error: The radial value {radius}, should be less than 2"
        )

    path = sm.jwos(sm.slash_check(fd.dir_parent()), 'data', slash, 'save', slash)

    if encounter == 0:
        enc = 'EA'
    else:
        enc = sm.jwos('E', str(encounter))

    fd.dir_make(enc, path)

    return sm.jwos(sm.jwos(path, enc, slash), str(radius), slash)


def enc_selector(

):
    print('Currently loaded encounters:', valid_enc, '\n')

    valid_full = ['f', 'full', 'ful', 'fu', 'ull', 'ff']
    valid_single = ['s', 'single', 'ss', 'sngle', 'sig', 'ingle',]

    h = 1
    while h > 0:
        data_set_input = input('Full data set or singular? (F/S)')
        data_set_input = cm.lower_all_letter(sm.valid_string(data_set_input))
        if data_set_input in valid_full:
            encounter = 0
            h = 0
        elif data_set_input in valid_single:
            g = 1
            while g > 0:
                enc_input = input('Please enter an encounter:')
                if sm.is_float(enc_input):
                    if float(enc_input) in valid_enc:
                        encounter = float(enc_input)
                        g = 0
                    elif enc_input == '':
                        print('Error: No input provided, please try again.')
                    else:
                        print(f'Error: The encounter provided {enc_input},'
                              ' does not have corresponding encounter '
                              'available.')
                else:
                    print(f'Error: Argument {enc_input} is not valid, '
                          f'str type is required, instead got type {type(enc_input)}.')
            h = 0
        else:
            print('Error: Please make a valid selection.')

    return encounter

