# Copyright 2024 antillia.com Toshiyuki Arai
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# split_master.py
# 2024/09/27


"""
From 
./Follicular-Cell-master
├─test
│  ├─images
│  └─masks
└─train
  ├─images
  └─masks

this script generates the following dataset.

./Follicular-Cell-ImageMask-Dataset
├─test
│  ├─images
│  └─masks
├─train
│  ├─images
│  └─masks
└─valid
  ├─images
  └─masks
"""


import os
import sys
import glob
import shutil

import traceback
import random

def split_test_master(images_dir, masks_dir, output_dir):
  image_files = glob.glob(images_dir + "/*.jpg")
  random.seed(137)
  random.shuffle(image_files)
  num = len(image_files)
  num_valid = int(num * 0.5)
  num_test  = int(num * 0.5)
  print("num_valid {}".format(num_valid))
  print("num_test  {}".format(num_test ))

  valid_files = image_files[:num_valid]
  test_files  = image_files[num_valid:]
  valid_dir   = os.path.join(output_dir, "valid")
  test_dir    = os.path.join(output_dir, "test")
  copy(valid_files, masks_dir, valid_dir)
  copy(test_files,  masks_dir, test_dir )


def copy(image_files, masks_dir, dataset_dir):
  out_images_dir = os.path.join(dataset_dir, "images")
  out_masks_dir  = os.path.join(dataset_dir, "masks")

  if not os.path.exists(out_images_dir):
    os.makedirs(out_images_dir)
  if not os.path.exists(out_masks_dir):
    os.makedirs(out_masks_dir)

  for image_file in image_files:
    shutil.copy2(image_file, out_images_dir)
    print("Copied {} to {}".format(image_file, out_images_dir))

    basename = os.path.basename(image_file)
    mask_filepath = os.path.join(masks_dir, basename)
    shutil.copy2(mask_filepath, out_masks_dir)
    print("Copied {} to {}".format(mask_filepath, out_masks_dir))


if __name__ == "__main__":
  try:

    train_images_dir = "./Follicular-Cell-master/train/images"
    train_masks_dir  = "./Follicular-Cell-master/train/masks"

    output_dir       = "./Follicular-Cell-ImageMask-Dataset/"
 
    if os.path.exists(output_dir):
      shutil.rmtree(output_dir)
    if not os.path.exists(output_dir):
      os.makedirs(output_dir)

    shutil.copytree(train_images_dir, output_dir + "/train/images")
    shutil.copytree(train_masks_dir,  output_dir + "/train/masks")

    test_images_dir = "./Follicular-Cell-master/test/images"
    test_masks_dir  = "./Follicular-Cell-master/test/masks"

    split_test_master(test_images_dir, test_masks_dir, output_dir)

  except:
    traceback.print_exc()

