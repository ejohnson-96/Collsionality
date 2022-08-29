from modules.core.loadsave import file_dir as fd
from modules.collisions.model import file_gen as fg


encounter = fg.enc_selector()

wind_radius = [0.1,0.3,1.0]
save_loc = []
for radius in wind_radius:
    save_loc.append(fg.load_generate(encounter, radius))
theta_save_loc = fd.dir_drop(fd.dir_drop(save_loc[0]))
print(save_loc[0], theta_save_loc)


solar, space, error = fg.data_import(encounter)
solar, space, error = fg.data_validate(solar, space, error)
solar, space, error = fg.data_resize(solar, space, error)

solar, psp_temps, wind_temps = fg.scalar_gen(solar, space)
solar, space, error, psp_temps, wind_temps = fg.file_combine(solar, space, error, psp_temps, wind_temps)

fg.save_files()

