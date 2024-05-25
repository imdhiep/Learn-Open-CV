import cv2
import numpy as np

# Đọc ảnh từ tệp
img = cv2.imread("Resources/cards.jpg")

# Định nghĩa các điểm để biến đổi phối cảnh
width, height = 250, 350
pts1 = np.float32([[111, 219], [287, 188], [154, 482], [352, 440]])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)

# Biến đổi phối cảnh của ảnh
imgOutput = cv2.warpPerspective(img, matrix, (width, height))

# Hiển thị ảnh gốc và ảnh đã biến đổi
cv2.imshow("Image", img)
cv2.imshow("Output", imgOutput)
cv2.waitKey(0)
