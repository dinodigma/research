import os
import sys
import glob



### Error Handling ###
def args_error(a):
    print "Error: Given %s arguments; Expected 1" % (str(len(a) - 1))
    sys.exit()

def subscan_error(s):
    print "Error: Subject scan %s does not exist" % (s)
    sys.exit()
    


args = sys.argv

if len(args) != 2:
    args_error(args)

subscan = args[1]

print "Now viewing: %s" % (subscan)

os.chdir("/home/jagust/graph/data/mri1.5/rest/freesurfer/%s" % (subscan))

t_one = "mri/T1.mgz"
mask ="mri/brainmask.mgz"
aseg = "mri/aseg.mgz:colormap=lut:opacity=0.2"
lhwhite = "-f surf/lh.white:edgecolor=blue"
lhpial = "surf/lh.pial:edgecolor=red"
rhwhite = "surf/rh.white:edgecolor=blue"
rhpial = "surf/rh.pial:edgecolor=red"

os.system("freeview -v %s %s %s %s %s %s %s" % (t_one, mask, aseg, lhwhite, lhpial, rhwhite, rhpial))

