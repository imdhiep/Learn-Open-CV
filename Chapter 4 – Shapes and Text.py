import cv2
import numpy as np

# Tạo một ảnh đen kích thước 512x512 với 3 kênh màu
img = np.zeros((512, 512, 3), np.uint8)

# Vẽ các hình dạng và văn bản trên ảnh
cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 3)
cv2.rectangle(img, (0, 0), (250, 350), (0, 0, 255), 2)
cv2.circle(img, (400, 50), 30, (255, 255, 0), 5)
cv2.putText(img, " OPENCV ", (300, 200), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 150, 0), 1)

# Hiển thị ảnh kết quả
cv2.imshow("Image", img)
print(img.shape)
cv2.waitKey(0)
