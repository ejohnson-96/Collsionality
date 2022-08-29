import numpy as np
import pandas as pd

from modules.core.loadsave import file_dir as fd

slash = fd.slash()

p = 'proton'
a = 'alpha'
particles = [p, a]


def encounter_import(
        enc,
):
    files = {}

    for i in range(enc.num_of_encs):
        print('Data File: ' + enc.encounter[i])
        files[enc.encounter[i]] = {}
        for j in range(2):
            val = str(enc.encounter[i] + slash + enc.encounter_names[j + 2 * i])
            files[enc.encounter[i]][enc.encounter_names[j + 2 * i]] = file_import(
                enc.str_load + val)
    return files

    return files


def error_import(
        enc,
):
    files = {}

    i = 0
    if enc.error_files_loaded:
        for encounter in range(enc.num_of_encs):
            print('Error File: ' + enc.encounter[encounter])
            files[enc.enc.encounter[encounter]] = {}
            for j in range(2):
                val = str(enc.encounter[encounter]) + slash + enc.encounter_errors[encounter + j + i]
                files[enc.encounter[encounter]][enc.encounter_errors[j + i]] = file_import(enc.str_load + val)
        i = i + 1
    else:
        raise ValueError(
            'Error: Tried to load error files when constant indicates none are present.'
        )

    return files


def sc_import(
        enc
):
    files = {}

    for i in range(enc.num_of_encs):
        print('Spacecraft File: ' + enc.encounter[i])
        files[enc.encounter[i]] = {}
        for key in enc.sc_names:
            val = str(enc.encounter[i] + slash + 'Position' + slash + key)
            files[enc.encounter[i]][key] = file_import(enc.str_load + val)

    return files


def file_import(
        location,
):
    if fd.file_exists(location):
        result = {}
        data = pd.read_csv(location)
        for key in data.keys():
            new_key = key.replace('+AF8-', '_')
            result[new_key] = np.array(data[key])

        return result
