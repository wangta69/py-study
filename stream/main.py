import cv2

scaler = 0.3

cap = cv2.VideoCapture('girl.mp4')

while True:
    ret, img = cap.read()
    if not ret:
        break

    # 동영상 사이즈 변경
    img = cv2.resize(img, (int(img.shape[1] * scaler), int(img.shape[0] * scaler)))

    cv2.imshow('img', img)
    cv2.waitKey(1)