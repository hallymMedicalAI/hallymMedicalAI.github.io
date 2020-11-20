import cv2
import numpy as np

# img = cv2.imread('Figure2.tif')
# cv2.imwrite('Figure2.jpg', img)
# img = cv2.imread('Figure5.tif')
# cv2.imwrite('Figure5.jpg', img)
#
# img1 = cv2.imread('2.png')
# img2 = cv2.imread('3.png')
# img3 = cv2.imread('4.png')
#
# print(img.shape)
# print(img1.shape)
# print(img2.shape)
# cv2.imwrite("6_resized.png",img)
# img = cv2.resize(img, (600, 700))
#
# img1 = cv2.resize(img1, (600, 900))
# img2 = cv2.resize(img2, (600, 900))
# img3 = cv2.resize(img3, (600, 900))
# print(img.shape)
# print(img1.shape)
# print(img2.shape)
#
# vis = np.vstack([img, img1, img2, img3])
#
# cv2.imwrite('paper_combined3.png', vis)
#
#
img = cv2.imread('./imgs/1.png')
img1 = cv2.imread('./imgs/2.png')
img2 = cv2.imread('./imgs/3.png')
img3 = cv2.imread('./imgs/4.png')
img4 = cv2.imread('./imgs/5.png')

print(img.shape)
print(img1.shape)
print(img2.shape)
print(img3.shape)
#
img = cv2.resize(img, (700, 900))
cv2.imwrite('./imgs/1_resized.png', img)

img1 = cv2.resize(img1, (700, 900))
cv2.imwrite('./imgs/2_resized.png', img1)

img2 = cv2.resize(img2, (700, 900))
cv2.imwrite('./imgs/3_resized.png', img2)

img3 = cv2.resize(img3, (700, 900))
cv2.imwrite('./imgs/4_resized.png', img3)

img4 = cv2.resize(img4, (700, 900))
cv2.imwrite('./imgs/5_resized.png', img4)
# img1 = cv2.resize(img1, (467, 426))
# img2 = cv2.resize(img2, (467, 426))
# img3 = cv2.resize(img3, (467, 426))
#
# print(img.shape)
# print(img1.shape)
# print(img2.shape)
# print(img3.shape)
#
# vis = np.vstack([img3, img2])
# vis1 = np.vstack([img1, img])
# vis = np.hstack([vis, vis1])
# cv2.imwrite('office_combined.png', vis)
#
# img = cv2.imread('hos0.jpg')
# print(img.shape)
# print(int(img.shape[1]/5), int(img.shape[0]/3))
# img = cv2.resize(img, (int(img.shape[1]/15), int(img.shape[0]/15)))
# cv2.imwrite('hos0_resized.jpg', img)
#
# img1 = cv2.imread('hos1.JPG')
# print(img1.shape)
# print(int(img1.shape[1]/5), int(img1.shape[0]/3))
# img1 = cv2.resize(img1, (int(img1.shape[1]/15), int(img1.shape[0]/15)))
# cv2.imwrite('hos1_resized.jpg', img1)
#
# img2 = cv2.imread('hos2.jpg')
# print(img2.shape)
# print(int(img2.shape[1]/5), int(img2.shape[0]/3))
# img2 = cv2.resize(img2, (int(img2.shape[1]/15), int(img2.shape[0]/15)))
# cv2.imwrite('hos2_resized.jpg', img2)
#
# img3 = cv2.imread('hos3.jpg')
# print(img3.shape) # height / width
# # width / height 1920 / 1197
# print(int(img3.shape[1]/5), int(img3.shape[0]/3))
# # img3 = cv2.resize(img3, (2000, 3000))
# img3 = cv2.resize(img3, (int(img3.shape[1]/15), int(img3.shape[0]/15)))
# cv2.imwrite('hos3_resized.jpg', img3)
#
# img4 = cv2.imread('hos4.jpg')
# print(img4.shape)
# print(int(img4.shape[1]/15), int(img4.shape[0]/15))
# img4 = cv2.resize(img4, (374, 1200))
# cv2.imwrite('hos4_resized.jpg', img4)

# img4 = cv2.resize(img4, (2000, 3000))
# vis = np.hstack([img, img1, img2, img3, img4])
# vis = cv2.resize()
# vis = cv2.resize(vis, (vis.shape[1], 1197))
# cv2.imwrite('hos_combined.png', vis)

# img4 = cv2.imread('MACH_homepage_v1.jpg')
# # print(img4.shape)
# # print(int(img4.shape[1]/15), int(img4.shape[0]/15))
# img4 = cv2.resize(img4, (1920, 1200))
# cv2.imwrite('MACH_homepage_v1_resized.png', img4)
