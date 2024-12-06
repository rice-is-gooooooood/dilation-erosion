import cv2
import numpy as np

# 读取图像
image = cv2.imread('2.png', cv2.IMREAD_GRAYSCALE)

# 应用阈值处理以生成二值图,将像素值大于 128 的设置为 255（白色），小于等于 128 的设置为 0（黑色），得到二值图像binary_image。
_, binary_image = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)

# 在进行开操作和闭操作之前，需要定义一个结构元素。
# 这里使用numpy库创建了一个 3×3 的全 1 数组（数据类型为np.uint8）作为结构元素.
kernel = np.ones((3, 3), np.uint8)

# cv2.morphologyEx函数用于执行各种形态学操作，这里指定cv2.MORPH_OPEN表示开操作。
# 开操作是先对图像进行腐蚀操作，然后再对腐蚀后的结果进行膨胀操作。
# 它的主要作用是去除图像中的小的孤立的白色噪声点（在二值图像中，白色区域为目标区域，黑色区域为背景区域），
# 同时尽量保持目标区域的大小和形状不变。
opening = cv2.morphologyEx(binary_image, cv2.MORPH_OPEN, kernel)

# 对二值图像binary_image进行闭操作。同样使用cv2.morphologyEx函数，指定cv2.MORPH_CLOSE表示闭操作
# 闭操作是先对图像进行膨胀操作，然后再对膨胀后的结果进行腐蚀操作。它主要用于填充图像中目标区域内的小空洞
closing = cv2.morphologyEx(binary_image, cv2.MORPH_CLOSE, kernel)

# 使用cv2.imshow函数分别来显示原始的二值图像、经过开操作后的图像以及经过闭操作后的图像。
# 每个cv2.imshow函数的第一个参数是窗口的名称，第二个参数是要显示的图像数据。
cv2.imshow('Original Image', binary_image)
cv2.imshow('Opening', opening)
cv2.imshow('Closing', closing)

# 等待按键
cv2.waitKey(0)
cv2.destroyAllWindows()