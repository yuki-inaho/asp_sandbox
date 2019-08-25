import numpy as np
import pandas as pd
import glob
import os

import sys
try:
    import cv2
except:
    sys.path.remove("/opt/ros/kinetic/lib/python2.7/dist-packages")
    import cv2

import re
import os
import glob
import pdb
import numpy as np
import pandas as pd
import shutil

DIR_NAME = "./ball/right/"
OUT_DIR_NAME = "./ball_renamed/right/"

#後でタイムスタンプ処理加える事

_files = glob.glob(DIR_NAME + "color_*.jpg")
total_file_num = len(_files)
max_idx_num = total_file_num

color_img_files = glob.glob(DIR_NAME + "color_*.jpg")
color_img_files = np.sort(color_img_files)
depth_img_files = glob.glob(DIR_NAME + "depth_*.png")
depth_img_files = np.sort(depth_img_files)
depth_color_img_files = glob.glob(DIR_NAME + "depth_color_*.jpg")
depth_color_img_files = np.sort(depth_color_img_files)
ir_img_files = glob.glob(DIR_NAME + "ir_*.png")
ir_img_files = np.sort(ir_img_files)


file_count = 0
for i in np.arange(max_idx_num):
    color_img_name_full = color_img_files[i]
    depth_img_name_full = depth_img_files[i]
    depth_color_img_name_full = depth_color_img_files[i]
    ir_img_name_full = ir_img_files[i]
    #ファイルが正常にソートされているか確認

    color_img_name = os.path.basename(color_img_name_full)
    #pattern = '.*?(\d+)\D+(\d+).*' //with_timestamp
    pattern = '.*?(\d+).*?(\d+).*'
    result = re.search(pattern, color_img_name)
    zfill_idx = result.group(1)
    time_stamp = result.group(2)

    if(zfill_idx == '0000'): continue

    #time_stamp = result.group(2)

    '''
    color_save_path = save_path + "/color_%06d_" %(file_count*5) + time_stamp + ".jpg"
    depth_save_path = save_path + "/depth_%06d_" %(file_count*5) + time_stamp + ".png"
    depth_color_save_path = save_path + "/depth_color_%06d_" %(file_count*5) + time_stamp + ".jpg"
    pcd_path = save_path + "/point_%06d_" %(file_count*5) + time_stamp + ".pcd"
    '''

    color_save_path = OUT_DIR_NAME + "color_%04d" %(file_count) + ".jpg"
    depth_save_path = OUT_DIR_NAME + "depth_%04d" %(file_count) + ".png"
    depth_color_save_path = OUT_DIR_NAME + "depth_color_%04d" %(file_count) + ".jpg"
    ir_save_path = OUT_DIR_NAME + "ir_%04d" %(file_count) + ".png"

    shutil.copyfile(color_img_name_full ,color_save_path)
    shutil.copyfile(depth_img_name_full ,depth_save_path)
    shutil.copyfile(depth_color_img_name_full ,depth_color_save_path)
    shutil.copyfile(ir_img_name_full ,ir_save_path)

    file_count = file_count + 1

#result_int = int(result.group(1))
#idxes = np.append(idxes, result_int)
