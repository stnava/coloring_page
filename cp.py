import cv2
import matplotlib.pyplot as plt
import numpy as np
imgfn='IMG_5145.jpeg'
imgfn='/Users/stnava/Pictures/Photos Library.photoslibrary/resources/derivatives/5/5B7A2235-1860-4CB4-A4E1-2F4587D3F363_1_105_c.jpeg'
image = cv2.imread( imgfn )
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
s=[5,30,66]
blurred = cv2.GaussianBlur(gray, (s[0], s[0]), 0)
edges = cv2.Canny(blurred, s[1], s[2] )
edges_inv = cv2.bitwise_not(edges)

# Create a kernel for dilation
kernel = np.ones((3, 3), np.uint8)  # Adjust the size of the kernel as needed
retVal,masked_image = cv2.threshold(edges_inv,155,255,cv2.THRESH_BINARY_INV)
print(np.unique(masked_image))
# Dilate the edges
dilated_edges = cv2.dilate(masked_image, kernel, iterations=1)

# plt.imshow( edges_inv, cmap = 'gray')
# plt.show()

# jpeg_filename = "/Users/stnava/Downloads/maili_coloring_pages_2_years_old/maili_laughing_flower.jpg"
# jpeg_filename = "/Users/stnava/Downloads/maili_coloring_pages_2_years_old/maili_fam.jpg"
# jpeg_filename = "/Users/stnava/Downloads/maili_coloring_pages_2_years_old/maili_walk.jpg"
jpeg_filename = "/Users/stnava/Downloads/maili_coloring_pages_2_years_old/maili_wants_ice_cream.jpg"
dilated_edges2=dilated_edges.copy()
dilated_edges2[dilated_edges==255]=0
dilated_edges2[dilated_edges==0]=255
cv2.imwrite(jpeg_filename, dilated_edges2)
