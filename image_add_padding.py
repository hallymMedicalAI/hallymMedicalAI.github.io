import cv2
import numpy as np

img = cv2.imread("MACH_homepage_v1_resized.jpg")

ht, wd, cc= img.shape
print(img.shape)
# create new image of desired size and color (blue) for padding
ww = 2200
hh = 1500
color = (255,255,255)
result = np.full((hh,ww,cc), color, dtype=np.uint8)

# compute center offset
xx = (ww - wd) // 2
yy = (hh - ht) // 2

# copy img image into center of result image
result[yy:yy+ht, xx:xx+wd] = img

result1 = cv2.resize(result, (1920, 1200))
cv2.imwrite("Homepage1.png", result1)
# view result
cv2.imshow("result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
