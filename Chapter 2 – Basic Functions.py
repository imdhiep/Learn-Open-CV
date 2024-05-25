import cv2
import numpy as np

# Đọc ảnh từ tệp
img = cv2.imread("Resources/lena.png")
kernel = np.ones((5,5),np.uint8)

# Chuyển đổi ảnh sang màu xám
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Làm mờ ảnh
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 0)
# Phát hiện cạnh bằng Canny
imgCanny = cv2.Canny(img, 100, 100)
# Giãn ảnh
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)
# Xói mòn ảnh
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)

# Hiển thị các ảnh kết quả
cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dialation Image", imgDialation)
cv2.imshow("Eroded Image", imgEroded)
cv2.waitKey(0)
