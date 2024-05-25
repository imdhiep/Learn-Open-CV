import cv2

# Đọc ảnh từ tệp và hiển thị
img = cv2.imread("Resources/lena.png")
imgGray = cv2.cvtColor(img, cv2.COLOR_BAYER_BG2GRAY)
cv2.imshow("Gray Image", imgGray)
cv2.waitKey(0)

# Mở webcam và hiển thị hình ảnh từ webcam
frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)  # Đặt chiều rộng của khung hình
cap.set(4, frameHeight)  # Đặt chiều cao của khung hình
cap.set(10, 150)  # Đặt độ sáng của khung hình

while True:
    success, img = cap.read()
    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Nhấn phím 'q' để thoát
        break

cap.release()  # Giải phóng camera
cv2.destroyAllWindows()  # Đóng tất cả cửa sổ hiển thị
