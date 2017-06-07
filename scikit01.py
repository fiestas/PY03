from skimage import data, io, filters
img = io.imread('baboon-gs.png')
edges = filters.sobel(img)
io.imshow(edges)
io.show()