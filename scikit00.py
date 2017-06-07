import skimage.io as io
from skimage.color import rgb2gray 
img = io.imread('baboon.png')
img_grayscale = rgb2gray(img)
io.imsave('baboon-gs.png',img_grayscale)
show_grayscale = io.imshow(img_grayscale)
io.show()