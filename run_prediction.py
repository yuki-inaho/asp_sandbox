import toml
import shutil
import sys
import os
import glob
import re
import pdb
import numpy as np

files = glob.glob("./ext_fused_data/color_*")

save_path = './ext_result'
if not os.path.exists(save_path):
    os.mkdir(save_path)
else :
    shutil.rmtree(save_path)
    os.mkdir(save_path)

idxes = np.array([])
for file in files:
    pattern = '.*?(\d+).*'
    result = re.match(pattern, file)
    result_int = int(result.group(1))
    idxes = np.append(idxes, result_int)

idxes = np.sort(idxes)
max_idx = int(np.max(idxes)) 

home = os.environ['HOME']  


#for i in np.arange(max_idx + 1):
#        command =  home + "/catkin_ws/devel/lib/aspara_picker_universal_sensor/aspara_picker_universal_sensor" + " " + str(i)
#        os.system(command)
TOML_PATH = home + "/catkin_ws/src/aspara_picker_dual_zense/cfg/recognition_parameter.toml"

#idxes = [12,35,43,56,91,121,146,183,204,216,376,473,556,663,901,972]
#idxes = np.array(idxes)

#for i in idxes:
for i in np.array([4,13,30]):
    command =  home + "/catkin_ws/devel/lib/aspara_picker_dual_zense/aspara_picker_dual_zense" + " " + TOML_PATH + " " +  str(int(i))
    os.system(command)


