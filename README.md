<h2>Tiled-ImageMask-Dataset-Follicular-Cell (Updated:2024/09/29)</h2>
<li>
2024/09/29: Added <a href="https://drive.google.com/file/d/1ISpL9l-Dv8k93BrqGb0V0vaab9TrQP5U/view?usp=sharing">
Tiled-Follicular-Cell-ImageMask-Dataset-V2.zip</a>
</li>
<br>
This is Tiled ImageMask Dataset for Follicular-Cell<a href="https://github.com/bupt-ai-cz/Hybrid-Model-Enabling-Highly-Efficient-Follicular-Segmentation">
Hybrid-Model-Enabling-Highly-Efficient-Follicular-Segmentation</a>
<br>
The original Follicular-Cell Patch Dataset can be downloaded from the google drive 
<a href="https://drive.google.com/file/d/1t1W7tpKscqLxPApqH3JSP_zsljLHWKxQ/view?usp=sharing">IM_PatchDataset.zip</a>.
<br>
<br>

<b>Download Tiled-ImageMask-Dataset</b><br>
You can download our dataset from the google drive:<br>
<a href="https://drive.google.com/file/d/1Muvzh0nzaqhYvYF1iUwfHGSGIXq0bQG3/view?usp=sharing">
Tiled-Follicular-Cell-ImageMask-Dataset.zip</a>
<br>
<br>
<b>Download Tiled-ImageMask-Dataset V2</b><br>
You can download our dataset from the google drive:<br>
<a href="https://drive.google.com/file/d/1ISpL9l-Dv8k93BrqGb0V0vaab9TrQP5U/view?usp=sharing">
Tiled-Follicular-Cell-ImageMask-Dataset-V2.zip</a>, which was derived from training_set only wthout testing set.
<br>
Probably, this dataset is more suitable for a real train-eval process of a segmentation model.
<br>

<h3>1. Dataset Citation</h3>
Please cite these papers in your publications if it helps your research: 
<a href="https://www.sciencedirect.com/science/article/pii/S2667102621000036">
<b>pdf of Intelligent Medicine</b>
</a>
<pre>
@article{zhu2021hybrid,
  title={Hybrid model enabling highly efficient follicular segmentation in thyroid cytopathological whole slide image},
  author={Zhu, Chuang and Tao, Siyan and Chen, Huang and Li, Minzhen and Wang, Ying and Liu, Jun and Jin, Mulan},
  journal={Intelligent Medicine},
  year={2021},
  publisher={Elsevier}
}
</pre>
License: This data can be freely used for academic purposes. (non-commercial)
<br>
<br>
<h3>2. Download Follicular-Cell</h3>

If you would like to create Follicular Cell ImageMask Dataset by yourself,
please download the original PatchDataset from the google drive 
<a href="https://drive.google.com/file/d/1t1W7tpKscqLxPApqH3JSP_zsljLHWKxQ/view?usp=sharing">IM_PatchDataset.zip</a>.
<br>
It contains the following testing set and training set of 1024x1024 pixels png files.<br>
<pre>
./patch dataset
├─testing set
│  ├─data
│  │  ├─background
│  │  ├─jiaozhi
│  │  └─lvpao
│  ├─label
│  │  ├─background
│  │  ├─jiaozhi
│  │  └─lvpao
│  └─label_transfered
│      ├─background
│      ├─jiaozhi
│      └─lvpao
└─training set
    ├─data
    │  ├─background
    │  ├─jiaozhi
    │  └─lvpao
    ├─label
    │  ├─background
    │  ├─jiaozhi
    │  └─lvpao
    └─label_transfered
        ├─background
        ├─jiaozhi
        └─lvpao
</pre>

<br>

<h3>3. Generate tiled dataset</h3>
Please run the following command for Python script <a href="./TiledImageMaskDatasetGenerator.py">
TiledImageMaskDatasetGenerator.py
</a><br>
<pre>
python TiledImageMaskDatasetGenerator.py
</pre>

This command generates tiledly-splitted 512x512 image and mask files, and size-reduced 512x512 image and mask files 
from <b>lvpao</b> in data and label_transfered of testing set and training set.<br><br>
<pre>
./Tiled-Follicular-Cell-master
├─test
│  ├─images
│  └─masks
└─train
    ├─images
    └─masks
</pre>

</pre>

For example, an image and mask files can be split into four tiles of 512x512 pixels respectively as shown below:<br>
<hr>
<table>
<tr>
<th>
Image
</th>
<th>
Mask
</th>
</tr>
<tr>
<td>
<img src="./tiled_sample/image_13_31744-109568.png"  width="480" height="auto">
</td>
<td>
<img src="./tiled_sample/mask_13_31744-109568.png"  width="480" height="auto">
</td>
</tr>
</table>
<br>
<table>
<tr>
<th>
Splitted images
</th>
<th>
Splitted masks
</th>
</tr>
<tr>
<td>
<img src="./tiled_sample/tiled_images.png"  width="480" height="auto">

</td>
<td>
<img src="./tiled_sample/tiled_masks.png"  width="480" height="auto">

</td>
</tr>

</table>
<br>
<b>However, since all black only masks are irrelevant annotations, 
we excluded those empty mask tiles and corresponding image tiles to generate our tiled-dataset.</b><br>
<br>
<b>After empty images and masks excluded</b><br>
<table>
<tr>
<th>
Splitted images
</th>
<th>
Splitted masks
</th>
</tr>
<tr>
<td>
<img src="./tiled_sample/images/10002_1x0.jpg"  width="480" height="auto">

</td>
<td>
<img src="./tiled_sample/masks/10002_1x0.jpg"  width="480" height="auto">

</td>
</tr>

</table>
 
<hr>
If you would like to generate a pre-augmented tiled dataset, you may set augmentation parameter to be True
in TiledImageMaskDatasetGenerator.py as shown below;<br>
<pre>
if __name__ == "__main__":
  try:
    #...

    # You may set augmentation parameter to be True.      
    augmentation = True
    #augmentation = False
    
    generator = TiledImageMaskDatasetGenerator(exclude_empty_mask=True,
              augmentation=augmentation)

    #...
</pre>

<br>

<h3>4. Split tiled dataset</h3>
Please run the following command for Python script <a href="./split_tiled_master.py">
split_tiled_master.py
</a><br>
<pre>
python split_tiled_master.py
</pre>
This command generates Tiled-Follicular-Cell-ImageMask-Dataset.<br>
<pre>
./Tiled-Follicular-Cell-ImageMask-Dataset
├─test
│  ├─images
│  └─masks
├─train
│  ├─images
│  └─masks
└─valid
    ├─images
    └─masks
</pre>
<hr>
<b>train images: </b><br>
<img src="./asset/train_images_sample.png"  width="1024" height="auto">
<br>
<b>train masks: </b><br>
<img src="./asset/train_masks_sample.png"  width="1024" height="auto">
<hr>

<b>Tiled-Follicular-Cell-ImageMask-Dataset Statistics</b><br>
<img src="./Tiled-Follicular-Cell-ImageMask-Dataset_Statistics.png" width="480" height="auto"><br>

<h3>5. Generate tiled dataset from training_set only</h3>
Please run the following command for Python script <a href="./TrainTiledImageMaskDatasetGenerator.py">
TrainTiledImageMaskDatasetGenerator.py
</a><br>
<pre>
python TrainTiledImageMaskDatasetGenerator.py
</pre>

This command generates tiledly-splitted 512x512 image and mask files, and size-reduced 512x512 image and mask files 
from <b>lvpao</b> in data and label_transfered of training set only.<br><br>
<pre>
./Train-Tiled-Follicular-Cell-master
├─images
└─masks
</pre>

</pre>


<h3>6. Split train tiled dataset</h3>
Please run the following command for Python script <a href="./split_train_tiled_master.py">
split_train_tiled_master.py
</a><br>
<pre>
python split_train_tiled_master.py
</pre>
This command generates Tiled-Follicular-Cell-ImageMask-Dataset-V2.<br>
<pre>
./Tiled-Follicular-Cell-ImageMask-Dataset-V2
├─test
│  ├─images
│  └─masks
├─train
│  ├─images
│  └─masks
└─valid
    ├─images
    └─masks
</pre>
<hr>
<b>train images: </b><br>
<img src="./asset/train_images_sample_v2.png"  width="1024" height="auto">
<br>
<b>train masks: </b><br>
<img src="./asset/train_masks_sample_v2.png"  width="1024" height="auto">
<hr>

<b>Tiled-Follicular-Cell-ImageMask-V2-Dataset Statistics</b><br>
<img src="./Tiled-Follicular-Cell-ImageMask-Dataset-V2_Statistics.png" width="480" height="auto"><br>

<br>
<h3>Reference</h3>
<b>1. Hybrid model enabling highly efficient follicular segmentation <br>
in thyroid cytopathological whole slide image </b><br>
Chuang Zhu, Siyan Tao, Huang Chen, Minzhen Li, Ying Wang, Jun Liu, Mulan Jin<br>

https://doi.org/10.1016/j.imed.2021.04.002<br>
<a href="https://www.sciencedirect.com/science/article/pii/S2667102621000036">https://www.sciencedirect.com/science/article/pii/S2667102621000036</a>



