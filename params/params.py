import os


# root:		    [str] 
#               The full path to abidbot (e.g. where bin/, setup.sh, data_raw/ live)
#				| use the command "pwd" (print working directory)
root = ""

# visit_path:   [str]
#               Full path to the ~/.visit/ folder in your home directory
#               | "~/.visit/" should work but use full path just in case
visit_path = "~/.visit/"

# it:		    [int] in (0, inf)
#               The iteration step in the h5 data
#				| to check, do "module load hdf5" and go to one of the 3d_data folders
#				| and do "h5ls" on one of the .h5 files and check the step between
#				| subsequent values in the 'it' column
it = 

# dt:           [float] in (0, inf)
#               How much time in code units pass between each frame (each 'it' number in h5data is a frame)
#		        note: h5data is output less frequently than the other files; we can only make a frame if there exists h5data
#				| no sure fire way to get this since the way diagnostic files are output may change in the future
#				| at the moment i am writing this, the file bhns.mon is output at twice the frequency of h5data, so
#				| the difference between every other row in the time column is dt
dt = 

# M: 		    [float] in (0, inf)
#               The ADM mass at initial time(this is used to normalize time/length labels)
#				| found in the file "bhns.mon", there are one or multple columns (black holes and volume are separate)
#				| starting with M_ADM; the set M equal to the sum of these (just take the value of the first time)
M = 

# maxdensity:	[float] in (0, inf)
#               The maximum density at initial time (used to normalize density colorbar)
#               | found in the file "bhns.mon" in the 9th columm labeled "rho_b_max"
#               note: sometimes, the initial time isn't enough, so you may need to use the maximum value int he 9th column
maxdensity = 

# offset:		[int] in [0, inf)
#               Is 0 if you start from the 3d_data folder that has it=0
#				| if not, then take the first iteration number of the first 3d_data folder
#				| and divide by the iteration step "it" 
offset = 0
    
# time_offset:  [float] This parameter is rarely nonzero. time_offset is described by the following 
#			    relation
#				    t/M = ( (iteration number)*(dt)/(it) + (time_offset) )/M
#			    time_offset may be nonzero if there is regridding involved.
#			    If there has been regridding and the new run starts at iteration 0 this will 
#			    probably be nonzero
time_offset = 0.0

# numStars:		[int] in {1,2}
#               The number of stellar objects in our initial system (needed to determine where to center the camera when filming)
#				| e.g. neutron star is 1, binaries are 2
numStars=1






# don't change below (automated settings)
#####################################################################################################


# BH settings: looks in the Horizon folder to see how many black holes
# - for BHDisk, only bh1 exists
# - for BBH, the initial two black holes are bh1, bh2 and the final black hole is bh3
# - NOT SURE ABOUT NSNS and BHNS CASES YET
bhForms = True if os.path.exists(root + "/data_raw/Horizon/") else False
bh1 = False if len([f for f in os.listdir(root + "/data_raw/Horizon") if f.endswith(".ah1.gp")]) == 0 else True
bh2 = False if len([f for f in os.listdir(root + "/data_raw/Horizon") if f.endswith(".ah2.gp")]) == 0 else True
bh3 = False if len([f for f in os.listdir(root + "/data_raw/Horizon") if f.endswith(".ah3.gp")]) == 0 else True
bh_flags = [bh1, bh2, bh3]




params = [root, it, dt, M, maxdensity, offset, time_offset, numStars, bhForms, bh_flags]

