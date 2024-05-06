import cv2
""" print("Package Imported")

image = cv2.imread("Resources/lambo.png")

cv2.imshow("Output" ,image)
cv2.waitKey(0) """

"""cap = cv2.VideoCapture(1)
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)

while True:
    success, img = cap.read()
    cv2.imshow("Result",img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break"""
        
img = cv2.imread("Resources/lena.png")
imgGray = cv2.cvtColor(img,cv2.COLOR_BAYER_BG2GRAY)

cv2.imshow("Gray Image", imgGray)
cv2.waitKey(0)