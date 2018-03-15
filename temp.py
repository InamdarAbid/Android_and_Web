from PIL import Image
from scipy.misc import imsave, imread, imresize
import numpy as np

path = dynamic image path generated

x = imread(path,mode = 'L')

x = np.invert(x);

imsave('abid.png',x);

