import os
import glob
from PIL import Image
from PIL import ImageOps
import numpy as np
import matplotlib.pyplot as plt

files = glob.glob('../../../py-project/py-funny/image_mosaic/assets/my-photos/*')

for f in files:
    print(f)
    img = Image.open(f)
    # print(img.size)

    x, y = img.width, img.height
    sx = x // 2 - (min(x, y) // 2)
    sy = y // 2 - (min(x, y) // 2)
    img = img.crop((sx, sy, sx + min(x, y), sy + min(x, y)))  # (가로 시작점, 세로 시작점, 가로 범위, 세로 범위)
    img.show()





def crop_center(img):
    """
    중심 기준으로 자르기
    """
    if type(img) == np.ndarray:
        # print('USE Numpy')
        y, x, c = img.shape
        sx = x // 2-(min(x, y) // 2)
        sy = y // 2-(min(x, y) // 2)
        img = img[sy:sy+min(x, y), sx:sx+min(x, y)]
    else:
        # print('Use PIL')
        x, y = img.width, img.height
        sx = x // 2-(min(x, y) // 2)
        sy = y // 2-(min(x, y) // 2)
        img = img.crop((sx, sy, sx+min(x, y), sy+min(x, y)))
    return img


def make_square(img, size):
    """
    짮은 쪽은 채우고, 중심기준으로 자르기
    """
    border_size = abs(img.width - img.height)
    k = max(img.width, img.height)
    img_bordered = ImageOps.expand(img, border=border_size, fill='black')
    w = img_bordered.width
    h = img_bordered.height
    img_squared = img_bordered.crop((w//2-k//2, h//2-k//2, w//2+k//2, h//2+k//2))
    return img_squared.resize(size)

def make_square2(img):
    """
    짮은쪽을 기준으로 하여 중심기준으로 자르기
    """
    # border_size = abs(img.width - img.height)
    k = min(img.width, img.height)
    # img_bordered = ImageOps.expand(img, border=border_size, fill='white')
    # w = img_bordered.width
    # h = img_bordered.height
    x, y = img.width, img.height
    sx = x // 2 - (min(x, y) // 2)
    sy = y // 2 - (min(x, y) // 2)
    img = img.crop((sx, sy, sx + min(x, y), sy + min(x, y)))  # (가로 시작점, 세로 시작점, 가로 범위, 세로 범위)
    #
    # img_squared = img_bordered.crop((w//2-k//2, h//2-k//2, w//2+k//2, h//2+k//2))
    # return img_squared.resize(size)

# for f in files:
#     print(f)
#     img = Image.open(f)
#     img_resize = img.resize((int(img.width / 2), int(img.height / 2)))
#     title, ext = os.path.splitext(f)
#     img_resize.save(title + '_half' + ext)
#
# for f in files:
#     print(f)
#     img = Image.open(f)
#     img_resize = img.resize((256, 256))
#     img_resize.save('data/dst/sample_pillow_resize_nearest.jpg')
#
#     img_resize_lanczos = img.resize((256, 256), Image.LANCZOS)
#     img_resize_lanczos.save('data/dst/sample_pillow_resize_lanczos.jpg')

