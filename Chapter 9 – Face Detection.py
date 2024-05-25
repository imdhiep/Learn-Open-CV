import cv2

# Tải bộ phân loại Haar Cascade cho việc phát hiện khuôn mặt
faceCascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")

# Đọc ảnh từ tệp
img = cv2.imread('Resources/lena.png')
# Chuyển đổi ảnh sang màu xám
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Phát hiện các khuôn mặt trong ảnh xám
faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)

# Vẽ hình chữ nhật xung quanh các khuôn mặt phát hiện được
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (250, 0, 0), 2)

# Hiển thị ảnh kết quả
cv2.imshow("Result", img)
cv2.waitKey(0)
