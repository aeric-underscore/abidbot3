import sys, os
sys.path.append(os.path.join(sys.path[0],'params'))
from params import params
from params_run import params_run
from params_field import params_field
from params_gw import params_gw


class AbidBot: 
    # The AbidBot class (new to abidbot3) serves as a way to organize all the parameters floating around in Abid Bot for the python scripts
    #   so that python functions can take an instance of AbidBot as an argument to access all the parameters; 
    
    def __init__(self, params, params_run, params_field, params_gw):
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
        self.b = self.BFieldBot(params_field)
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
            self.unpack_generalSettings(params[0])
            self.unpack_bhSettings(params[1])

        def unpack_generalSettings(self, generalSettings):
            self.root, self.visit_path, self.it, self.dt, self.M, \
                self.maxdensity, self.offset, self.time_offset, self.numStars \
                = generalSettings 
        def unpack_bhSettings(self, bhSettings):
            self.bhForms, self.bh1, self.bh2, self.bh3 \
                = bhSettings

        def __str__(self):
            return f'helo i am params bot'

    class RunBot:
        def __init__(self, params_run):
            self.unpack_viewSettings(params_run[0])
            self.unpack_volIsoSettings(params_run[1])
            self.unpack_particleLineSettings(params_run[2])
            self.unpack_gridLineSettings(params_run[3])
            self.unpack_velocitySettings(params_run[4])
            self.unpack_spinvecSettings(params_run[5])
        
        def unpack_viewSettings(self, viewSettings):
            self.viewXML, self.override_view_flag, \
                self.viewNormal, self.viewUp, self.zoom \
                = viewSettings
        def unpack_volIsoSettings(self, volIsoSettings):
            self.rho_volXML, self.rho_pseudoXML, self.rho_isoXML, \
                self.bsqXML, self.bsq_pseudoXML, self.bsq_isoXML \
                = volIsoSettings
        def unpack_particleLineSettings(self, particleLineSettings):
            self.particleIntegrationXMLs, self.particleMaxStepLengths, \
                self.particleMaxSteps, self.particleColors \
                = particleLineSettings
        def unpack_gridLineSettings(self, gridLineSettings):
            self.gridIntegrationXMLs, self.gridMaxStepLengths, \
                self.gridMaxSteps, self.gridDirections, self.gridColors \
                = gridLineSettings
        def unpack_velocitySettings(self, velocitySettings):
            self.vec1XML, self.vec2XML, self.nVectors1, self.nVectors2, \
                self.follow_bsq2r_flag, self. min_bsq2r_val, self.min_vel_magnitude, \
                self.vec1_cylinder_flag, self.vec1_cylidner_r, self.vec2_flag, \
                self.vec1_sphere_r, self.vec2_sphere_r \
                = velocitySettings
        def unpack_spinvecSettings(self, spinvecSettings):
            self.spinvecXML, self.spinvec_color, \
                self.spinvec_scale1, self.spinvec_scale2, self.spinvec_scale3 \
                = spinvecSettings 
        
        def __str__(self):
            return f'helo i am run bot'

    class BFieldBot:
        def __init__(self, params_field):
            self.unpack_generalParticleSettings(params_field[0])
            self.unpack_particleMakerSettings(params_field[1])
            self.unpack_gridMakerSettings(params_field[2])

        def unpack_generalParticleSettings(self, generalParticleSettings):
            self.useParticleTracer, self.firstTime, self.particleFlags, \
                self.useCustomParticleSeeds, self.customSeedTXTs \
                = generalParticleSettings
        def unpack_particleMakerSettings(self, particleMakerSettings):
            self.particleCenters, self.particleNormVecs, self.particlePairs, \
                self.particleNumSeeds, self.particleOffsets \
                = particleMakerSettings
        def unpack_gridMakerSettings(self, gridMakerSettings):
            self.bh_rs, self.gridPairs, self.gridNumSteps, self.gridOffsets \
                = gridMakerSettings

        def __str__(self):
            return f'helo i am b-field bot'


    class GWBot:
        def __init__(self, params_gw):
            self.unpack_generalGWSettings(params_gw[0])
            self.unpack_psi4Settings(params_gw[1])
            self.unpack_gridSettings(params_gw[2])
            self.unpack_simulationSettings(params_gw[3])
            self.unpack_testGWSettings(params_gw[4])

        def unpack_generalGWSettings(self, generalGWSettings):
            self.root, self.test_flag, self.update_lookup, self.files_per_folder, \
                self.threeD_flag, self.all_times, self.start_time, self.end_time \
                = generalGWSettings
        def unpack_psi4Settings(self, psi4Settings):
            self.psi4_dir, self.psi4_num, self.psi4_f, \
                self.psi4_f_sorted, self.bin_dir \
                = psi4Settings
        def unpack_gridSettings(self, gridSettings):
            self.xy_max_3D, self.xy_num_3D, self.z_min_3D, self.z_max_3D, self.z_num_3D, \
                self.xy_max_2D, self.xy_num_2D, self.phi_1D, self.theta_1D \
                = gridSettings
        def unpack_simulationSettings(self, simulationSettings):
            self.M_ADM, self.cutoff_w, self.r_areal, self.gw_dt, self.num_modes, \
                self.num_times, self.plot_all_modes, self.modes_to_plot \
                = simulationSettings
        def unpack_testGWSettings(self, testGWSettings):
            self.test_num_times, self.test_dt, self.test_kind, \
                self.test_R, self.test_M, self.test_Om \
                = testGWSettings


        

        def __str__(self):
            return f'root (str):      {self.root}\ntest_flag (bool):        {self.test_flag}\nM_ADM (float):        {self.M_ADM}'





a = AbidBot(params, params_run, params_field, params_gw)
