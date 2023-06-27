import os
from params import root

########## Volume and Isosurface XML files ##########

atts = root + "/bin/visit_atts"

# rho_volXML:       volume attributes xml file used when plotting the density rho
#                   | used when plotting rho as volume
rho_volXML = atts + "/rho_volume_file.xml"       

# rho_pseudoXML:    attributes xml files used when plotting the density rho using a
# rho_isoXML:       pseudocolor plot with the isosurface operator (faster than volume)
#                   | used when plotting rho as iso
rho_pseudoXML = atts + "/rho_pseudo_file.xml"
rho_isoXML = atts + "/rho_iso_file.xml"


# bsqXML:           volume attributes xml file used when plotting b-squared-over-2-rho
#                   | used when plotting b^2/(2*rho) as volume
bsqXML = atts + "/bsq2r_volume_file.xml"

# bsq_pseudoXML:    attributes xml files used when plotting bsq2r using a
# bsq_isoXML:       pseudocolor plot with the isosurface operator (faster than volume)
#                   | used when plotting bsq2r as iso
bsq_pseudoXML = atts + "/bsq2r_pseudo_file.xml"
bsq_isoXML = atts + "/bsq2r_iso_file.xml"


# vec1XML:          vector attributes xml files used when plotting velocity with vector fields
# vec2XML:          | because the numerical relativity grid is finer closer to the compact object
#                   | we use different vector plots close to and far from the black hole
#                   | VEC2: veloctiy 