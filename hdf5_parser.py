import hdf5_getters

h5 = hdf5_getters.open_h5_file_read("data/A/A/A/TRAAAAW128F429D538.h5")
duration = hdf5_getters.get_duration(h5)
print duration
h5.close()
