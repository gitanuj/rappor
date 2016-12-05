import hdf5_getters

h5 = hdf5_getters.open_h5_file_read("data/msd_summary_file.h5")
for i in range(hdf5_getters.get_num_songs(h5)):
	print(hdf5_getters.get_song_id(h5, i))
h5.close()
