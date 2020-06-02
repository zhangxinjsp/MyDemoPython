#!/usr/bin/env python
# -*- coding: utf-8 -*-


# pip install pytesseract
# pip install pillow
# brew install tesseract
import pytesseract
from PIL import Image
from PIL import ImageChops

import imghdr

import math
import operator
from functools import reduce


# 识别图片中的文字
# tesseract 输入图片的文件名 输出文件的文件名 [-l lang][-psm pagesegmode][configfile...]
# -psm 在新版本中无效
# 输出文件名不需要带后缀名，会直接使用 txt 后缀
def image_to_str():
    image = Image.open("/Users/zhangxin//Desktop/test_image.png")
    # image.show()
    code = pytesseract.image_to_string(image, lang="chi_sim+eng")
    print(code)


# 推断图片类型
def get_image_type(path):
    return imghdr.what(path)


def compare_images(path_one, path_two, diff_save_location):
    """
    比较图片，如果有不同则生成展示不同的图片

    @参数一: path_one: 第一张图片的路径
    @参数二: path_two: 第二张图片的路径
    @参数三: diff_save_location: 不同图的保存路径
    """
    image_one = Image.open(path_one)
    image_two = Image.open(path_two)

    print(image_one.mode + '----' + image_two.mode)

    image_one.show("1")
    image_two.show("2")
    try:
        # RGBA 没法使用diffence
        # 结果是较小图片的尺寸
        # 图片的 mode 需要一致，不然没法比较
        diff = ImageChops.difference(image_one.convert('RGB'), image_two.convert('RGB'))
        print(diff.getbbox())
        if diff.getbbox() is None:
            # 图片间没有任何不同则直接退出
            print("【+】We are the same!")
        else:
            diff.save(diff_save_location)

    except ValueError as e:
        text = ("表示图片大小和box对应的宽度不一致，参考API说明：Pastes another image into this image."
                "The box argument is either a 2-tuple giving the upper left corner, " + \
                "a 4-tuple defining the left, upper, right, and lower pixel coordinate, "
                "or None (same as (0, 0)). " + \
                "If a 4-tuple is given, the size of the pasted "
                "image must match the size of the region.使用2纬的box避免上述问题")
        print("【{0}】{1}".format(e, text))

    image_one.close()
    image_two.close()


# 图片的相似度比较，数值越大相似度越低，0.0 为完全相同
def image_contrast(img1, img2):
    image1 = Image.open(img1)
    image2 = Image.open(img2)

    h1 = image1.histogram()
    h2 = image2.histogram()

    result = math.sqrt(reduce(operator.add, list(map(lambda a, b: (a - b) ** 2, h1, h2))) / len(h1))
    return result


if __name__ == '__main__':
    # image_to_str()

    image_path_1 = '/Users/zhangxin/Desktop/2.png'
    image_path_2 = '/Users/zhangxin/Desktop/3.png'

    print(get_image_type(image_path_1) + '----' + get_image_type(image_path_2))

    # compare_images(image_path_1, image_path_2, '/Users/zhangxin/Desktop/我们不一样.png')
    print(image_contrast(image_path_1, image_path_2))
