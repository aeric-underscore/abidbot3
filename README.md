abid bot automates the 3D visualization of numerical relativity simulation data using the VisIt command line interface
    it was originally created in the Illinois Relativity Group by Abid Khan in 2017, who took many existing scripts and 
    some new ones and combined them into a single workflow



abidbot3 is a substantial and much needed quality-of-life/ease-of-use update written by Eric Yu in 2023
    in addition to ease-of-use, abidbot3 is also written to be easier to update 
        (specific instructrions on how to add new functinality to abidbot3 are written later on in this file)

    some of the major specific changes are listed below:
    
    1. restructures the setup scripts to increase efficiency, decrease clutter, and to properly integrate many new/tacked-on features/code
        (a) splits the setup processes into three categories:
            (i) data processing that only needs to be done once for a fixed set of raw data (e.g. black hole, spin, h5data, setups)
            (ii) data processing that involves tinkering around with settings, which may need to be run multiple times (e.g. seeds)
            (iii) the first two steps (i) and (ii) populate folders with processed data files that are named by their frame (in accordance to h5data frames), this step creates the extras/ dir (used to be called xml/) and organizes them into the same structure as h5data/ so it is usable by VisIt

    2. adds a python class AbidBot that stores all the parameters 
        (a) can act as a "parameter dictionary" that is passed as an argument in python functions


MAKING CHANGES TO ABIDBOT3: so you have been asked to plot something in VisIt that abidbot3 doesn't support
    1. Figure out how to plot this new feature in the VisIt graphical interface.
        
    1. Do you need process simulation data, or even generate your own data, into a file format that is usable by VisIt (e.g. *.vtk, *.3d, *.txt)? If the answer is yes, then this process in itself is likely a nontrivial task.
        (a) Start looking at some of the existing plots types, along with VisIt documentation, for ideas about how to plot this feature in VisIt
        (b) 
       
