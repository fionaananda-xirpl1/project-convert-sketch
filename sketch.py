#library numpy -> pip install numpy
#library imageio -> pip install imageio
#library scipy -> pip install scipy
#library opencv -> pip install opencv-python
#pakai library image yg kmrn (pip install imgae)
#siapkan 1 gambar di folder yg sm untk diconvert mjd sketsa pencil

import numpy as np
import imageio 
import scipy.ndimage
import cv2

img = "taylor.jpg" #nama file input

def rgb2gray(rgb):
    return np.dot(rgb[...,:3],[0.2989,0.5870,0.1140])
    #formula untuk convert img -> grayscale // pakai kode warna matlab

def dodge(front,back):
    final_sketch = front*255/(255-back)
    # jika gambarnya lbh bsr dari 255 bit/px maka akan diconvert jadi 255
    final_sketch[final_sketch>255]=255
    final_sketch[back==255]=255
    
    return final_sketch.astype('uint8')

ss = imageio.imread(img) # untuk read gambar yang dipilih diawal tadi
gray = rgb2gray(ss) #untuk convert gambar jd black and white 

i = 255-gray

# untuk memberi efek blur
blur = scipy.ndimage.filters.gaussian_filter(i, sigma=15)
#sigma adalah intensitas blurnya 

r = dodge(blur,gray)
# untuk convert gambarnya (dengan mengaplikasikan blur & black&white tadi)

cv2.imwrite("sketsa.png", r)
#untuk menghasilkan uotput gambar bernama sketsa.png 
# run > start debugging 