import numpy as np

t = 'time'


def scalar_velocity(
        solar,
):
    for encounter in solar.keys():
        h = 0
        for particle in solar[encounter].keys():
            solar[encounter][particle]['v_mag'] = []
            L = len(solar[encounter][particle][t])
            if h == 0:
                x, y, z = 'vp1_x', 'vp1_y', 'vp1_z'
            elif h == 1:
                x, y, z = 'va_x', 'va_y', 'va_z'
            else:
                raise ValueError(
                    f"Error: Argument {h}, does not have a particle."
                )

            for i in range(L):
                arg_ = (solar[encounter][particle][x][i]) ** 2 + (
                    solar[encounter][particle][y][i]) ** 2 + (
                           solar[encounter][particle][z][i]) ** 2
                if arg_ < 0:
                    arg_ = 0
                solar[encounter][particle]['v_mag'].append(np.sqrt(arg_))
            h = h + 1

    return solar


def scalar_temps(
        solar,
        space,
):
    psp_res = {}
    wind_res = {}

    for encounter in solar.keys():
        x, y = temp_generate(solar[encounter], space[encounter])
        psp_res[encounter] = x
        wind_res[encounter] = y

    return psp_res, wind_res


def temp_generate(
        solar_encounter,
        spc_encounter,
        noise=False
):
    factor = 11604

    psp_result = {}
    psp_result_keys = ['proton_scalar_temp_1', 'proton_scalar_temp_2',
                       'alpha_scalar_temp', 'theta_ap', 'dens_ap',
                       'proton_perpar', 'alpha_perpar', 'proton_1_k', 'alpha_k', 'time',
                       'proton_R', 'alpha_R', ]
    wind_result = {}
    wind_result_keys = ['wind_alpha_scalar_temp', 'wind_proton_scalar_temp', 'wind_theta']

    file_val = []
    for file in solar_encounter.keys():
        file_val.append(file)
    p = file_val[0]
    a = file_val[1]

    L = len(solar_encounter[p][t])

    for res_key in psp_result_keys:
        psp_result[res_key] = np.zeros(L)

    for res_key in wind_result_keys:
        wind_result[res_key] = np.zeros(L)

    for i in range(L):
        psp_result['proton_scalar_temp_1'][i] = (
                (2 * solar_encounter[p]['Tperp1'][i] + solar_encounter[p]['Trat1'][
                    i]) / 3)
        psp_result['proton_scalar_temp_2'][i] = (
                (2 * solar_encounter[p]['Tperp2'][i] + solar_encounter[p]['Trat2'][
                    i]) / 3)
        psp_result['proton_1_k'][i] = (psp_result['proton_scalar_temp_1'][i] * factor)

        if solar_encounter[p]['Trat1'][i] == 0:
            psp_result['proton_perpar'][i] = float('Nan')
        else:
            psp_result['proton_perpar'][i] = (solar_encounter[p]['Tperp1'][i] / \
                                              solar_encounter[p]['Trat1'][i])

        if solar_encounter[p]['Trat1'][i] == 0:
            psp_result['proton_R'][i] = float('Nan')
        else:
            psp_result['proton_R'][i] = (
                    solar_encounter[p]['Tperp1'][i] / solar_encounter[p]['Trat1'][i])

        psp_result['alpha_scalar_temp'][i] = ((2 * solar_encounter[a]['Ta_perp'][i] +
                                               solar_encounter[a]['Trat'][i]) / 3)
        psp_result['alpha_k'][i] = (psp_result['alpha_scalar_temp'][i] * factor)

        if solar_encounter[a]['Trat'][i] == 0:
            psp_result['alpha_perpar'][i] = float('Nan')
        else:
            psp_result['alpha_perpar'][i] = (solar_encounter[a]['Ta_perp'][i] / \
                                         solar_encounter[a]['Trat'][i])

        if solar_encounter[a]['Trat'][i] == 0:
            psp_result['alpha_R'][i] = float('Nan')
        else:
            psp_result['alpha_R'][i] = (
                solar_encounter[a]['Ta_perp'][i] / solar_encounter[a]['Trat'][i])

        if solar_encounter[p]['np1'][i] == 0:
            psp_result['dens_ap'][i] = 0
        else:
            psp_result['dens_ap'][i] = (
                    solar_encounter[a]['na'][i] / solar_encounter[p]['np1'][i])

        wind = spc_encounter['Wind_Temps.csv']

        if spc_encounter['Wind_Temps.csv']['TEMP_ALPHA_S/C_eV'][i] == 0:
            wind_result['wind_alpha_scalar_temp'][i] = float('Nan')
        else:
            wind_result['wind_alpha_scalar_temp'][i] = spc_encounter['Wind_Temps.csv']['TEMP_ALPHA_S/C_eV'][i]


        if wind['TEMP_PROTN_S/C_eV'][i] == 0:
            wind_result['wind_proton_scalar_temp'][i] = float('Nan')
            wind_result['wind_theta'][i] = float('Nan')
        else:
            wind_result['wind_proton_scalar_temp'][i] = (wind['TEMP_PROTN_S/C_eV'][i])
            wind_result['wind_theta'][i] = (
                wind['TEMP_ALPHA_S/C_eV'][i] / wind['TEMP_PROTN_S/C_eV'][i])

    return psp_result, wind_result


def noise_gen(

):
    if psp_result['proton_scalar_temp_1'][i] == 0:
        psp_result['theta_ap'][i] = 0
    else:
        alpha_noise = random.randint(0, 15) / 100
        proton_noise = random.randint(0, 7) / 100
        val = random.random()
        if val > 0.5:
            alpha_noise = alpha_noise + 1
            proton_noise = proton_noise + 1
        else:
            alpha_noise = 1 - alpha_noise
            proton_noise = 1 - proton_noise

        psp_result['theta_ap'][i] = (psp_result['alpha_scalar_temp'][i] / \
                                     psp_result['proton_scalar_temp_1'][i])

        return
