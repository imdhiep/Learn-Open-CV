import cv2
import numpy as np

# Đọc ảnh từ tệp và in kích thước của ảnh
img = cv2.imread("Resources/lambo.png")
print(img.shape)

# Thay đổi kích thước của ảnh
imgResize = cv2.resize(img, (300, 200))
print(imgResize.shape)

# Cắt ảnh từ tọa độ (0, 200) đến (200, 500)
imgCropped = img[0:200, 200:500]

# Hiển thị các ảnh kết quả
cv2.imshow("Image", img)
cv2.imshow("Image Resize", imgResize)
cv2.imshow("Image Cropped", imgCropped)
cv2.waitKey(0)
