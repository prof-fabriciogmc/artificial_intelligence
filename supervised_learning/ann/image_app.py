##
# A simple image signature knn example
#
# Author: Fabrício G. M. de Carvalho, Ph.D.
##


import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from model import img_signature, distance
from neural_network import FFNeuralNetwork
import copy
import numpy as np

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
templates = [ref_img_1_prop, ref_img_2_prop, ref_img_3_prop, ref_img_4_prop, unknown_img_prop]

# resampling  and rescale  of image feature vector.
for template in templates:
    proc_signature = []
    maximum = max(template['feature_vector'])
    for sig_index in range(5, 95, 2):
        proc_signature.append(template['feature_vector'][sig_index]/maximum)
    if template['class'] == 'circunference':
        template['output'] = np.array([1, 0])
    elif template['class'] == 'square':
        template['output'] = np.array([0,1])
    else:
        pass

    template['norm_feature'] = copy.deepcopy(proc_signature)

unknown_img_prop = templates.pop()

ffnn = FFNeuralNetwork( [len(templates[0]['norm_feature']), 4, 2] )

#training phase
n_epochs = 100
e_k = [[],[]]
n_examples = len(templates)
for i in range(n_epochs):
    e_epoch_1 = 0
    e_epoch_2 = 0
    for template in templates:
        y = ffnn.output(template['norm_feature'])
        y = np.array(y)
        e = template['output'] - y
        e_epoch_1 += e[0]
        e_epoch_2 += e[1]
        ffnn.learn(e, 0.05)
    e_k[0].append(e_epoch_1/n_examples) #stores the first ouput classification error
    e_k[1].append(e_epoch_2 / n_examples)  # stores the second ouput classification error

#application/generalization phase
y = ffnn.output(unknown_img_prop['norm_feature'])
y = np.array(y)
c1 = np.array([1,0]) #circunference
c2 = np.array([0,1]) #square
if np.linalg.norm(c1-y) < np.linalg.norm(c2-y):
    unknown_img_prop['class'] ='circunference'
elif np.linalg.norm(c1-y) > np.linalg.norm(c2-y):
    unknown_img_prop['class'] = 'square'
else:
    unknown_img_prop['class'] = 'undefined'


fig, ax = plt.subplots(2)
fig.suptitle("Classification error.")
ax[0].plot(e_k[0])
ax[1].plot(e_k[1])
ax[0].grid()
ax[1].grid()

fig, ax = plt.subplots(2)
fig.suptitle(unknown_img_prop['class'])
ax[0].imshow(unknown_img_prop['img'])
ax[1].plot(unknown_img_prop['feature_vector'])

plt.show()



















