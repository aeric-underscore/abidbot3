import os


class AbidBot: 
    # The AbidBot class (new to abidbot3) serves as a way to organize all the parameters floating around in Abid Bot for the python scripts
    #   so that python functions can take an instance of AbidBot as an argument to access all the parameters; 
    
    def __init__(self, params, params_run, params_fields, params_gw):
        # the arguments of __init__() are bash files (strings of absolute paths) that live in abidbot/params/
        #   each of these files defines and exports bash variables
        #   then the bash variables are each assigned a "property" in AbidBot
        #
        # UPDATING ABIDBOT:
        #   if there is some change you want to make that requires a new parameter
        #       (such as a new type of Visit plot with its associated boolean flag and xml file)
        #   then add the bash parameters to the appropriate params file
        #       or create a new params file and add it as an argument to __init__()
        #       and to add it as an argument to all the python files
        #   then add respective lines in __init__() as well as in __str__()
        self.p = self.ParamsBot(params)             
        self.r = self.RunBot(params_run)
        self.b = self.BFieldBot(params_fields)
        self.gw = self.GWBot(params_gw)

    def __str__(self):
        return f"""############ PARAMS ############
                   \n{self.p}\n\n
                   ############# RUN ##############
                   \n{self.r}\n\n
                   ############ BFIELD ############
                   \n{self.b}\n\n
                   ############## GW ##############
                   \n{self.gw}\n"""
    
    class ParamsBot:
        def __init__(self, params):  #params = [root, it, dt, M, maxdensity, offset, time_offset, numStars, bhForms, bh_flags]
            self.p.root = str(params[0])
            self.p.it = int(params[1])
            self.p.dt = float(params[2])
            self.p.M = float(params[3])
            self.p.maxdensity = float(params[4])
            self.p.offset = int(params[5])
            self.p.time_offset = float(params[6])
            self.p.numStars = int(params[7])

            self.p.bhForms = bool(params[8])
            bh_flags = params[9]
            self.p.bh1 = bool(bh_flags[0])
            self.p.bh2 = bool(bh_flags[1])
            self.p.bh3 = bool(bh_flags[2])

        def __str__(self):
            return f'helo i am params bot'

    class RunBot:
        def __init__(self, params_run):
            self.params = params_run
        
        def __str__(self):
            return f'helo i am run bot'

    class BFieldBot:
        def __init__(self, params_fields):
            self.params = params_fields

        def __str__(self):
            return f'helo i am b-field bot'


    class GWBot:
        def __init__(self, params_gw):
            self.root = str(params_gw[0])
            self.test_flag = bool(params_gw[1])
            self.update_lookup = bool(params_gw[2])
            self.files_per_folder = int(params_gw[3])
            
            # # # unpack psi4_params # # #
            psi4_params = params_gw[4]
            self.psi4_dir = str(psi4_params[0]); self.psi4_num = int(psi4_params[1])
            self.psi4_f = str(psi4_params[2]); self.psi4_f_sorted = str(psi4_params[3])

            # # # unpack grid_params # # #
            grid_params = params_gw[5]
            self.xy_max_3D = float(grid_params[0]); self.xy_num_3D = int(grid_params[1])
            self.z_min_3D = float(grid_params[2]); self.z_max_3D = float(grid_params[3]); self.z_num_3D = int(grid_params[4])
            self.xy_max_2D = float(grid_params[5]); self.xy_num_2D = int(grid_params[6])
            self.phi_1D = float(grid_params[7]); self.theta_1D = float(grid_params[8])

            # # # unpack simulation_params # # #
            sim_params = params_gw[6]
            self.M_ADM = float(sim_params[0]); self.cutoff_w = float(sim_params[1]); self.r_areal = float(sim_params[2]); self.gw_dt = float(sim_params[3])
            self.num_modes = int(sim_params[4]); self.num_times = int(sim_params[5])
            self.plot_all_modes = bool(sim_params[6]); self.modes_to_plot = sim_params[7]

            
            self.all_times = bool(params_gw[7])
            self.start_time = int(params_gw[8])
            self.end_time = int(params_gw[9])
            self.bin_dir = str(params_gw[10])

            # # # unpack test_gw_params # # #
            test_params = params_gw[11]
            self.test_num_times = int(test_params[0]); self.test_dt = float(test_params[1]); self.test_kind = int(test_params[2])
            self.test_R = float(test_params[3]); self.test_M = float(test_params[4]); self.test_Om = float(test_params[5])


            self.threeD_flag = params_gw[12]

        def __str__(self):
            return f'root (str):      {self.root}\ntest_flag (bool):        {self.test_flag}\nM_ADM (float):        {self.M_ADM}'






