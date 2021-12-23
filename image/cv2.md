```
pip install opencv-contrib-python
pip install opencv-python
```

에러가 발생한다면
```
pip uninstall opencv-python
pip uninstall opencv-contrib-python

pip install opencv-contrib-python
pip install opencv-python
```

- cv2.IMREAD_COLOR : 이미지 파일을 Color로 읽어들입니다. 투명한 부분은 무시되며, Default값입니다.
- cv2.IMREAD_GRAYSCALE : 이미지를 Grayscale로 읽어 들입니다. 실제 이미지 처리시 중간단계로 많이 사용합니다.
- cv2.IMREAD_UNCHANGED : 이미지파일을 alpha channel까지 포함하여 읽어 들입니다.
* 3개의 flag대신에 1, 0, -1을 사용해도 됩니다.
```
>>>> img.shape
(206, 207, 3)
```
이미지는 3차원 행렬로 return이 됩니다. 206은 행(Y축), 207은 열(X축), 3은 행과 열이 만나는 지점의 값이 몇개의 원소로 이루어져 있는지를 나타납니다. \
위 값의 의미는 이미지의 사이즈는 207 X 206이라는 의미입니다.
그렇다면 3은 어떤 의미일까요. 바로 색을 표현하는 BGR값입니다. \
일반적으로 RGB로 많이 나타내는데, openCV는 B(lue), G(reen), R(ed)로 표현을 합니다.
3: BGR
## 이미지 저장
```
cv2.imwrite('lenagray.png', gray)
```

##
BGR to RGB :  matplotlib에서 rgb순서와 open cv에서의 순서가 다르기 때문에 색상을 변경해야 함
```
sample_img = cv2.cvtColor(sample_img, cv2.COLOR_BGR2RGB)
```