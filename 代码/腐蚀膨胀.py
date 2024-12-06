import cv2
import numpy as np

# 因为图像的形态学处理操作都是基于白色像素上处理的，需要对图像做二值化，且需要将处理的像素值改为255，
# 这里导入了cv2（OpenCV 库）用于图像处理相关的操作，以及numpy库用于处理数组数据，在后续定义结构元素等操作中会用到。
# 读取图像,检查图像是否读取成功，这里指定以灰度模式（cv2.IMREAD_GRAYSCALE）读取图像，
# 将彩色图像转换为灰度图像进行后续处理。如果图像读取失败，image将为None，通过if语句进行判断并输出提示信息后退出程序。
image = cv2.imread('1.jpeg', cv2.IMREAD_GRAYSCALE)
if image is None:
    print("图像未找到，请确保路径正确。")
    exit()

# 显示原图像
cv2.imshow('Original Image', image)

# 这部分代码对读取的灰度图像进行二值化处理。将图像中像素值大于 127 的设置为 255（白色），小于等于 127 的设置为 0（黑色）
# 得到一个只有黑、白两种颜色的二值图像
_, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# 显示二值化图像
cv2.imshow('Binary Image', binary_image)

# 在进行形态学操作（膨胀和腐蚀）之前，需要定义一个结构元素。
# 这里使用numpy库创建了一个 5×5 的全 1 数组作为结构元素，
# 它将在后续的膨胀和腐蚀操作中起到类似模板的作用，用于确定对图像中的哪些像素进行操作以及如何操作
kernel = np.ones((5, 5), np.uint8)

# 进行膨胀操作，cv2.dilate函数会根据定义的结构元素kernel对图像中的白色区域（像素值为 255 的区域）进行扩张。
# 这里设置iterations=1，表示只进行一次膨胀操作。
dilated_image = cv2.dilate(binary_image, kernel, iterations=1)

# 显示膨胀图像
cv2.imshow('Dilated Image', dilated_image)

# 进行腐蚀操作，cv2.erode函数与膨胀操作相反，会根据定义的结构元素kernel对图像中的白色区域进行收缩
eroded_image = cv2.erode(binary_image, kernel, iterations=1)

# 显示腐蚀图像
cv2.imshow('Eroded Image', eroded_image)

# cv2.waitKey(0)会等待用户按下任意键，程序在此处暂停，直到用户按键。
# cv2.destroyAllWindows()在用户按键后，会关闭所有由cv2.imshow函数打开的图像显示窗口。
cv2.waitKey(0)
cv2.destroyAllWindows()