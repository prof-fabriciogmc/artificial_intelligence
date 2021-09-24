# Basic image signature function
#
# Author: Fabrício G. M. de Carvalho, Ph.D.
##

from math import sqrt

# This implementation considers white background and
# that grayscale ranges from 0 to 255

MAX_GRAY_LEVEL = 255
MIN_GRAY_LEVEL = 0
GRAY_BYTE_REF = 1

def img_signature(img, mode):
    signature = []
    if mode == 'h':
        for row in range(len(img)):
            signature.append(0)
            for column in range(len(img[0])):
                if (img[row][column][GRAY_BYTE_REF] != MAX_GRAY_LEVEL):
                    signature[row] += 1
    elif mode == 'v':
        for column in range(len(img[0])):
            signature.append(0)
            for row in range(len(img)):
                if (img[row][column][GRAY_BYTE_REF] != MAX_GRAY_LEVEL):
                    signature[column] += 1
    else:
        raise ValueError('unknown mode')

    return signature

#euclidean norm calculation
def distance(a, b):
    distance = 0
    for i in range(len(a)):
        distance += (a[i] - b[i])**2
    distance = sqrt(distance)
    return distance
