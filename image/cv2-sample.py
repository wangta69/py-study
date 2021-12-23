import cv2

fname = 'images/sample1.jpg'

# 컬러 변경
original = cv2.imread(fname, cv2.IMREAD_COLOR)
gray = cv2.imread(fname, cv2.IMREAD_GRAYSCALE)
unchange = cv2.imread(fname, cv2.IMREAD_UNCHANGED)

cv2.imshow('Original', original)
cv2.imshow('Gray', gray)
cv2.imshow('Unchange', unchange)

# 이미지 크기 변경
# dst = cv2.resize(src, dsize=(640, 480), interpolation=cv2.INTER_AREA)
# dst2 = cv2.resize(src, dsize=(0, 0), fx=0.3, fy=0.7, interpolation=cv2.INTER_LINEAR)

cv2.waitKey(0)
cv2.destroyAllWindows()