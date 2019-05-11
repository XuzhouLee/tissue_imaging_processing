# tissue_imaging_processing
"""
This project is the stage 1 for the tissue laser emission microscopy imaging processing and diagnosis.
###############################################
This batch of samples were lymphoma lymphoid tissue sections collected from 7 different patients.
There are 3 different levels of the diagnosis decision from pathologists:
1.Aggressive (Really BAD)
2.Indolent (Hard to Say)
3.Benign (GOOD)
These decisions are made based on the proliferation rate of tissue cells. Higher proliferation rate=====>More Aggressive.
(However, sometimes benign tissue has "proliferation core" (a cluster of high proliferation rate cells), but that's not a sign of aggressive tumor)
##################################################
There are several problems which influenced the imaging quality right now.
1.The 2D scanning of pump laser is achieved by tuning two mirrors. Therefore, the pump incident angle are various among the whole images.
2.During the process of fluorescent dye staining, the 5-micron-thick tissue sections may overlap and the overlapping area is non-sense for pathology analysis.
3.The tissue area (200-300 micron) along the boundary is abnormally brighter under fluorescence microscopy, which is meaningless for diagnosis.
#########################################################
Therefore, the aim for the phase 1 for this project is to automatically detect good observing sub-imaging areas to save the time of pathologists and researchers.
#===============================================================#
1.Standardlized the stimulated emission intensity
1.1 It can be summarized from the existing images.
1.2 We can use a homogenous fluoresence solution sample to caliberate it.
#=============================================================#
2.Detecting the texture of the overlapping area.
(Not quite clear yet)
#=============================================================#
3.Boundary detection algorithm of the fluorescence images
(Try different boundary detection to find out the best boundary cropping method)
#================================================================#

The expected result of this phase is:
######################################################################################################################
#Input scanning images=========>Standardlized========>Label the area is good with green=======>label overlapping with# #red=========>Label boundary area with yellow=======>From the green area extracting the sub images good for analysis #
######################################################################################################################
"""







"""
