import os
from params import root



atts = root + "/bin/visit_atts"

#################### View XML file and settings ####################
# https://visit-sphinx-github-user-manual.readthedocs.io/en/v3.0.0/gui_manual/MakingItPretty/View.html

# viewXML:              view xml file used by defaut if there aren't any view_*.xml files in the extras directory
viewXML = atts + "/view.xml"

# override_view_flag:   True or False
# viewNormal            | True: overrides settings in viewXML with the values below (which are enough to specify a view)
# viewUp                |   see the graphic (fig 9.41) at the above link for more details
# zoom                  |   viewNormal is the vector that points from toward the camera from the focus
#                       |       e.g. (0,1,0) = camera on +y axis, (0,0.5,0.5) = camera on line y=z 
#                       |   and viewUp is what is at the top of the image (usually leave as 0,0,1)
viewNormal = (0., 0.5, 0.5)
viewUp = (0., 0., 1.)
zoom = 500


#################### Volume and Isosurface XML files ####################

# rho_volXML:           volume attributes xml file used when plotting the density rho by default
#                       if there aren't any rho_vol_*.xml files in the extras directory
#                       | used when plotting rho as volume
rho_volXML = atts + "/rho_volume_file.xml"       

# rho_pseudoXML:        attributes xml files used when plotting the density rho using a
# rho_isoXML:           pseudocolor plot with the isosurface operator (faster than volume)
#                       these files are used by default if there aren't any rho_peusdo_*.xml 
#                       and/or rho_iso_*.xml files in the extras directory
#                       | used when plotting rho as iso
rho_pseudoXML = atts + "/rho_pseudo_file.xml"
rho_isoXML = atts + "/rho_iso_file.xml"


# bsqXML:               volume attributes xml file used when plotting b-squared-over-2-rho
#                       | used when plotting b^2/(2*rho) as volume
bsqXML = atts + "/bsq2r_volume_file.xml"

# bsq_pseudoXML:        attributes xml files used when plotting bsq2r using a
# bsq_isoXML:           pseudocolor plot with the isosurface operator (faster than volume)
#                       | used when plotting bsq2r as iso
bsq_pseudoXML = atts + "/bsq2r_pseudo_file.xml"
bsq_isoXML = atts + "/bsq2r_iso_file.xml"

###################################################################################


#################### Streamline integration settings and files ####################

# Paritcle Integration Settings
#               | list of XML files for integral curve attributes corresponding to the particle field plots
#               | maxStepLenghts and maxSteps (most commonly tinkered with) will override the values in the XML file
#               | | https://visit-sphinx-github-user-manual.readthedocs.io/en/stable/python_scripting/attributes.html#integralcurve-integralcurveattributes
# particleIntegrationXMLs:  [str list] file names in "bin/visit_atts/bfield_atts/"
# particleMaxStepLengths:   [float list] decreasing will make your field lines smoother (but shorter)
# particleMaxSteps:         [int list] increasing will make your field lines longer
particleIntegrationXMLs = ["stream_particle_0.xml", "stream_particle_1.xml", "stream_particle_2.xml"]
particleMaxStepLengths = [10., 10., 10.]
particleMaxSteps = [2000, 2000, 2000]

# particleColors:   [int-tuples list]
#                   list of colors corresponding to the particle field plots; sets the color of the field line
particleColors = [(0, 255, 0), (0, 255, 0), (0, 255, 0)]

# Grid Point Integration Settings
#               | each index corresponds to a black hole (supports up to three black holes)
#               | maxStepLenghts, maxSteps,  (most commonly tinkered with) and directions will override the values in the XML file
# gridIntegrationXMLs:  [str list] file names in "bin/visit_atts/bfield_atts/"
# gridMaxStepLengths:   [float list]  decreasing will make your field lines smoother (but shorter)
# gridMaxSteps:         [int list] increasing will make your field lines longer
# gridDirections:       [str-tuple list] specifies integration direction of the ring of points above and below the black hole (wrt its spin)
#                                    like ("above_direction", "below_direction")
#                                    try the different combinations of "Foward" and "Backward" until it looks good
gridIntegrationXMLs = ["stream_grid_0.xml", "stream_grid_1.xml", "stream_grid_2.xml"]
gridMaxStepLengths = [10., 10., 10.]
gridMaxSteps = [2000, 2000, 2000]
gridDirections = [("Forward", "Backward"), ("Forward", "Backward"), ("Forward", "Backward")]

# gridColors:   [int-tuples list]
#                   list of colors corresponding to the grid point field plots; sets the color of the field line
gridColors = [(255, 255, 255), (255, 255, 255), (255, 255, 255)]

#################################################################################

#################### Velocity Vector Plot files and settings ####################
# because the numerical relativity grid is finer closer to the compact object
# we might want to use use different vector plots close to and far from the black hole
# | vec1: the default velocity vector plot
# | vec2: the velocity vector plot near the compact object

# vec1XML:          vector attributes xml files used when plotting velocity with vector fields
# vec2XML:          size parameters (make sure scaleByMagnitude is true and autoScale is false)
#                   | scale, headSize: changes size of entire vector and just the head
vec1XML = atts + "/vec1.xml"
vec2XML = atts + "/vec2.xml"

# nVectors1:        nVectors in vector attributes
# nVectors2:        | increase/decrease to increaes/decrease the number of vectors 
#                   | this OVERRIDES the nVectors in the XML file
nVectors1 = 2000
nVectors2 = 100

# follow_bsq2r_flag:    True or False
# min_bsq2r_val:        | True: only plots vectors where log(bsq2r) is greater than min_bsq2r_val
# min_vel_magnitude:    | False: only plots vectors that have magnitude greater than min_vel_magnitude
follow_bsq2r_flag = True
min_bsq2r_val = -0.5
min_vel_magnitude = 0.5

# vec1_cylinder_flag:   True or False
# vec1_cylidner_r:      | True: adds a cylinder operator with radius vec1_cylinder_r 
#                       |       (automatically tilts if spin.vtk files are present, otherwise is along z axis)
vec1_cylinder_flag = True
vec1_cylinder_r = 0.5

# vec2_flag:            True or False
#                       | False: only vec1 is plotted and near/far from compact object is not distinguished
#                       | True: vec1 only plots vectors outside a sphere of radius vec1_sphere_r
#                       |       vec2 only plots vectors inside a sphere of radius vec2_sphere_r
vec2_flag = False
vec1_sphere_r = 0.2
vec2_sphere_r = 0.2

#################################################################################

######################### Spin Vector files and settings ########################
# spinvecXML:          vector attributes xml files used when plotting spin vectors for black holes (only bhs for now)
# spinvec_color:        | all black holes will use this spinvecXML 
#                       | spinvec_color [int tuple for RGB] will OVERRIDE the color in spinvecXML 
spinvecXML = atts + "/spinvec.xml"
spinvec_color = (255, 255, 0)

# spinvec_scale1:       allows the scale of the spin vector to be set differently for the three black holes (OVERRIDES XML)
# spinvec_scale2:       | for more than one black hole, scaling factor for BHs should be proportional to 
# spinvec_scale3:       | some function of the black hole mass (instead of just the spin magnitude)
#                       | ask someone for the exact function and update this description pls :)
spinvec_scale1 = 100
spinvec_scale2 = 100
spinvec_scale3 = 100

#################################################################################


viewSettings = [viewXML, override_view_flag, viewNormal, viewUp, zoom]
volIsoSettings = [rho_volXML, rho_pseudoXML, rho_isoXML, bsqXML, bsq_pseudoXML, bsq_isoXML]
particleLineSettings = [particleIntegrationXMLs, particleMaxStepLengths, particleMaxSteps, particleColors]
gridLineSettings = [gridIntegrationXMLs, gridMaxStepLengths, gridMaxSteps, gridDirections, gridColors]
velocitySettings = [vec1XML, vec2XML, nVectors1, nVectors2, follow_bsq2r_flag, min_bsq2r_val, min_vel_magnitude, 
                    vec1_cylinder_flag, vec1_cylidner_r, vec2_flag, vec1_sphere_r, vec2_sphere_r]
spinvecSettings = [spinvecXML, spinvec_color, spinvec_scale1, spinvec_scale2, spinvec_scale3]

params_run = [viewSettings, volIsoSettings, particleLineSettings, gridLineSettings, velocitySettings, spinvecSettings]