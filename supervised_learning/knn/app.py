##
# A simple image signature knn example
#
# Author: Fabrício G. M. de Carvalho, Ph.D.
##


import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from model import img_signature, distance
from knn import knn

# image file reading
# templates
ref_img_1 = mpimg.imread('data/ref_circunference_1.bmp')
ref_img_2 = mpimg.imread('data/ref_circunference_2.bmp')
ref_img_3 = mpimg.imread('data/ref_square_1.bmp')
ref_img_4 = mpimg.imread('data/ref_square_2.bmp')

# unknown image
unknown_img_1 = mpimg.imread('data/unknown_03.bmp')

ref_img_1_prop = {'img': ref_img_1, 'class': 'circunference', 'rows': len(ref_img_1), 'columns': len(ref_img_1[0])}
ref_img_2_prop = {'img': ref_img_2, 'class': 'circunference', 'rows': len(ref_img_2), 'columns': len(ref_img_2[0])}
ref_img_3_prop = {'img': ref_img_3, 'class': 'square', 'rows': len(ref_img_3), 'columns': len(ref_img_3[0])}
ref_img_4_prop = {'img': ref_img_4, 'class': 'square', 'rows': len(ref_img_4), 'columns': len(ref_img_4[0])}


unknown_img_prop = {'img': unknown_img_1, 'class': 'unknown', 'rows': len(unknown_img_1), 'columns': len(unknown_img_1[0])}

## Compute image horizontal signatures (feature vector):
ref_img_1_prop['feature_vector'] = img_signature(ref_img_1,'h')
ref_img_2_prop['feature_vector'] = img_signature(ref_img_2,'h')
ref_img_3_prop['feature_vector'] = img_signature(ref_img_3,'h')
ref_img_4_prop['feature_vector'] = img_signature(ref_img_4,'h')
unknown_img_prop['feature_vector'] = img_signature(unknown_img_1,'h')

templates = [ref_img_1_prop, ref_img_2_prop, ref_img_3_prop, ref_img_4_prop]
unknown_img_prop['class'] = knn(templates, unknown_img_prop, 3)


for i in range(len(templates)):
    fig, ax = plt.subplots(2)
    fig.suptitle(templates[i]['class'])
    ax[0].imshow(templates[i]['img'])
    ax[1].plot(templates[i]['feature_vector'])

fig, ax = plt.subplots(2)
fig.suptitle(unknown_img_prop['class'])
ax[0].imshow(unknown_img_prop['img'])
ax[1].plot(unknown_img_prop['feature_vector'])

plt.show()



