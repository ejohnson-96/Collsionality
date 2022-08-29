from modules.core.loadsave import file_dir as fd
from modules.core.variables import char_man as cm


slash = fd.slash()


def enc(
        encount,
        valid_enc,
        error_files=False,
):
    path = fd.dir_parent()
    for i in range(len(path.split(slash)[-1])):
        path = cm.remove_end(path)

    enc.path = path
    enc.str_load = str(enc.path + "data" + slash + "load" + slash)
    enc.str_save = str(enc.path + "data" + slash + "save" + slash)
    enc.error_files_loaded = error_files

    enc.encounter = []
    if encount == 0:
        L = len(valid_enc)
        for i in range(L):
            enc.encounter.append('E' + str(int(valid_enc[i])))
    else:
        L = 1
        enc.encounter.append('E' + str(encount))

    enc.num_of_encs = L
    enc.encounter_names = []
    enc.encounter_errors = []

    for i in range(L):
        enc.encounter_names.append(enc.encounter[i] + '_protons.csv')
        enc.encounter_names.append(enc.encounter[i] + '_alphas.csv')
    if error_files:
        for i in range(L):
            enc.encounter_errors.append(enc.encounter[i] + '_proton_errors.csv')
            enc.encounter_errors.append(enc.encounter[i] + '_alpha_errors.csv')

    enc.sc_names = []
    enc.sc_names.append('PSP.csv')
    enc.sc_names.append('Wind_Orbit.csv')
    enc.sc_names.append('PSP_Orbit.csv')
    enc.sc_names.append('Wind_Outside_Range_Hour.csv')
    enc.sc_names.append('Wind_Outside_Range_Min.csv')
    enc.sc_names.append('Wind_Temps.csv')
    enc.sc_names.append('Wind_Thermal_Speeds.csv')

    enc.num_of_sc = len(enc.sc_names)
    if error_files:
        enc.num_files = len(enc.encounter_names) + len(enc.sc_names) + len(enc.encounter_errors)
    else:
        enc.num_files = len(enc.encounter_names) + len(enc.sc_names)

    return


