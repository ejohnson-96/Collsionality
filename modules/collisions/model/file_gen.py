import numpy as np

from modules.core.loadsave import file_dir as fd
from modules.core.time import utilities as ut
from modules.core.variables import string_man as sm, char_man as cm, num_man as nm, arr_man as am

from modules.collisions.constants import enc
from modules.collisions.features import latlong as lat_lon
from modules.collisions.loadsave import loadsave as rw
from modules.collisions.model import scalar_gen as sc_gen

slash = fd.slash()

valid_enc = [4, 6, 7]
particles = rw.particles
t = 'time'


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
    path = sm.jwos(sm.slash_check(fd.dir_drop(fd.dir_parent())), 'data', slash, 'save', slash)

    if encounter == 0:
        enc = 'EA'
    else:
        enc = sm.jwos('E', str(int(encounter)))

    fd.dir_make(enc, path)

    return sm.jwos(sm.jwos(path, enc, slash), str(radius), slash)


def enc_selector(

):
    print('Currently loaded encounters:', valid_enc, '\n')

    valid_full = ['f', 'full', 'ful', 'fu', 'ull', 'ff']
    valid_single = ['s', 'single', 'ss', 'sngle', 'sig', 'ingle', ]

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

    return int(encounter)


def data_import(
        encounter,
        valid_encounters=valid_enc,
        error_files=False,
):
    enc(encounter, valid_encounters, error_files)
    print('\n')
    mm_data = rw.encounter_import(enc)
    sc_data = rw.sc_import(enc)

    if enc.error_files_loaded:
        error_data = rw.error_import(enc)
    else:
        error_data = None

    print('\nData import successful.\n')

    return mm_data, sc_data, error_data


def data_validate(
        solar,
        space,
        errors,
):
    for encounter in solar.keys():
        for particle in solar[encounter].keys():
            for key in solar[encounter][particle].keys():
                solar[encounter][particle][key] = am.valid_ent_num(solar[encounter][particle][key])

    if enc.error_files_loaded:
        for encounter in errors.keys():
            for particle in errors.keys():
                for key in space[encounter][particle].keys():
                    space[encounter][particle][key] = am.valid_ent_num(solar[encounter][particle][key])

    for encounter in space.keys():
        for particle in space[encounter].keys():
            for key in space[encounter][particle].keys():
                if key == 'EPOCH_yyyy-mm-ddThh:mm:ss.sssZ':
                    for i in range(len(space[encounter][particle]['EPOCH_yyyy-mm-ddThh:mm:ss.sssZ'])):
                        space[encounter][particle]['EPOCH_yyyy-mm-ddThh:mm:ss.sssZ'][i] = ut.datetime_format(
                            space[encounter][particle]['EPOCH_yyyy-mm-ddThh:mm:ss.sssZ'][i])
                    space[encounter][particle]['time'] = space[encounter][particle].pop(
                        'EPOCH_yyyy-mm-ddThh:mm:ss.sssZ')
                else:
                    space[encounter][particle][key] = am.valid_ent_num(space[encounter][particle][key])

    return solar, space, errors


def data_resize(
        solar_data,
        spc_data,
        error_data,
):
    for encounter in range(enc.num_of_encs):
        res = list(solar_data[enc.encounter[encounter]].keys())[0]
        t_ = solar_data[enc.encounter[encounter]][res][t]

        for y in solar_data[enc.encounter[encounter]].keys():
            xp = solar_data[enc.encounter[encounter]][y][t]
            for z in solar_data[enc.encounter[encounter]][y].keys():
                fp = solar_data[enc.encounter[encounter]][y][z]
                solar_data[enc.encounter[encounter]][y][z] = np.interp(t_, xp, fp)
                # mm_data[x][y][z] = np.resize(mm_data[x][y][z], min_len)

        if enc.error_files_loaded:
            for y in error_data[enc.encounter[encounter]].keys():
                xp = error_data[enc.encounter[encounter]][y][t]
                for z in error_data[enc.encounter[encounter]][y].keys():
                    fp = error_data[enc.encounter[encounter]][y][z]
                    error_data[enc.encounter[encounter]][y][z] = np.interp(t_, xp, fp)
                    # error_data[x][y][z] = np.resize(error_data[x][y][z], min_len)

        t_
        for y in spc_data[enc.encounter[encounter]].keys():
            xp = spc_data[enc.encounter[encounter]][y][t]
            for z in spc_data[enc.encounter[encounter]][y].keys():
                fp = spc_data[enc.encounter[encounter]][y][z]
                spc_data[enc.encounter[encounter]][y][z] = np.interp(t_, xp, fp)
                # sc_data[x][y][z] = np.resize(sc_data[x][y][z], min_len)

    return solar_data, spc_data, error_data


def temp_gen(
        solar,
        space,
):
    return sc_gen.scalar_temps(solar, space)


def speed_gen(
        solar,
):
    return sc_gen.scalar_velocity(solar)


def scalar_gen(
        solar,
        space,
):
    solar = speed_gen(solar)
    psp_temps, wind_temps = temp_gen(solar, space)
    print('Generating velocity magnitudes and temperature file... \n')
    return solar, psp_temps, wind_temps


def file_combine(
        solar,
        space,
        error,
        psp,
        wind,
):
    # Generate file and/or combine files (remember to do the scalar temp files)
    print('Generating data file... \n')
    solar_data = {}
    errors = {}
    spc_data = {}
    psp_scalar_temps = {}
    wind_scalar_temps = {}

    particle_list = rw.particles

    for particle in particle_list:
        solar_data[particle] = {}
        errors[particle] = {}

    for key in psp.keys():
        for value in psp[key].keys():
            psp_scalar_temps[value] = []

    for key in wind.keys():
        for value in wind[key].keys():
            wind_scalar_temps[value] = []

    for key in psp_scalar_temps.keys():
        for encounter in psp.keys():
            for i in range(len(psp[encounter][key])):
                psp_scalar_temps[key].append(psp[encounter][key][i])

    for key in wind_scalar_temps.keys():
        for encounter in wind.keys():
            for i in range(len(wind[encounter][key])):
                wind_scalar_temps[key].append(wind[encounter][key][i])

    for x in range(1):
        encounter = enc.encounter[x]
        for y in range(1):
            for particle in particle_list:
                indx = particle_list.index(particle)
                if nm.is_even(indx):
                    arg_x_ = 0
                elif nm.is_odd(indx):
                    arg_x_ = 1
                for z in solar[encounter][enc.encounter_names[2 * x + arg_x_]].keys():
                    solar_data[particle][z] = []

        if enc.error_files_loaded:
            for y in range(1):
                for particle in particle_list:
                    indx = particle_list.index(particle)
                    if nm.is_even((indx)):
                        arg_x_ = 0
                    else:
                        arg_x_ = 1
                    for z in error[encounter][
                        enc.encounter_errors[2 * x + arg_x_]].keys():
                        errors[particle][z] = []

        for y in range(len(enc.sc_names)):
            spc_data[enc.sc_names[y]] = {}
            for z in space[encounter][enc.sc_names[y]].keys():
                spc_data[enc.sc_names[y]][z] = []

    for encounter in solar.keys():
        for particle in solar[encounter].keys():
            x = particle[3:]
            x = x[:len(x) - 5]
            for z in solar_data[x].keys():
                for w in range(
                        len(solar[encounter][particle][z])):
                    solar_data[x][z].append(
                        solar[encounter][particle][z][w])

            if enc.error_files_loaded:
                for z in error[x].keys():
                    for w in range(
                            len(error[encounter][particle][
                                    z])):
                        errors[x][z].append(
                            error[encounter][particle][z][
                                w])

        for y in enc.sc_names:
            for z in spc_data[y].keys():
                for w in range(len(space[encounter][y][z])):
                    spc_data[y][z].append(space[encounter][y][z][w])

    return solar, space, errors, psp, wind


def save_files(
        solar,
        space,
        error,
        psp,
        wind,
):


    return


def scrub(
        solar_data,
        errors,
        spc_data,
        error_files=False,
):
    solar_data, errors, spc_data = scrub.scrub_data(solar_data, errors, spc_data, error_files)
    return solar_data, errors, spc_data


def lat_long(
        space,
):
    space[enc.sc_names[2]] = lat_lon.latlong_psp(space[enc.sc_names[2]])
    space[enc.sc_names[1]] = lat_lon.latlong_wind(space[enc.sc_names[1]])

    return space


def generate_theta(
        solar_data,
        spc_data,
        psp_scalar_temps,
        wind_scalar_temps,
        wind_radius,
        theta_ap_0,
        save_loc,
):

    theta_ap_final = theta_ap.make_theta_vals(solar_data, spc_data, psp_scalar_temps,
                                              wind_radius)

    theta = {'0.1 - 0.2': theta_ap_0, str(wind_radius): theta_ap_final}

    print(save_loc)
    file_names = ['theta_i.txt', 'theta_f.txt', 'wind_theta.txt']
    temp_files = [theta['0.1 - 0.2'], theta[str(wind_radius)],
                  wind_scalar_temps['wind_theta']]

    if len(file_names) != len(temp_files):
        warnings.warn("Warning: File save system has unequal lengths.")
    else:
        for i in range(len(file_names)):
            loc = sm.jwos(save_loc, file_names[i])
            np.savetxt(loc, temp_files[i])

    return