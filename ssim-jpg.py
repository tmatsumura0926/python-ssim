from cv2 import VideoCapture
import numpy as np
import cv2
import sys
import csv

#def AddGaussianNoise(image, mean, sigma):
#    noise = np.random.normal(mean, sigma, np.shape(image))
#    noisy_image = image + noise
#    noisy_image[noisy_image > 255] = 255
#    noisy_image[noisy_image < 0] = 0
#    noisy_image = noisy_image.astype(np.uint8)    # Float -> Uint
#    return noisy_image

# README

print("OpenCV Version: " + str(cv2.__version__))
# STEP1 PiC Read
args = sys.argv
if len(args) !=3 :
    print('比較するファイルを2つ指定してください')

# Debug ADDNOISE

# sigma = 5
# DstPicImage = cv2.imread(DstJPGPath, cv2.IMREAD_COLOR)
# noisy_image = AddGaussianNoise(DstPicImage, 0, sigma)
# cv2.imwrite(DstJPGPath,noisy_image)

SrcJPGPath = args[1]
DstJPGPath = args[2]

SrcJPGImage = cv2.imread(SrcJPGPath, cv2.IMREAD_COLOR)
DstJPGImage = cv2.imread(DstJPGPath, cv2.IMREAD_COLOR)

SrcJPGWidth , SrcJPGHeight ,SrcJPGCH= SrcJPGImage.shape
SrcJPGSize = SrcJPGWidth * SrcJPGHeight

print("SrcJPG Information")
print("   SrcJPG Width:", SrcJPGWidth)
print("   SrcJPG Height:", SrcJPGHeight)
print("   SrcJPG Size", SrcJPGSize)   

DstJPGWidth , DstJPGHeight ,DstJPGCH= DstJPGImage.shape
DstJPGSize = DstJPGWidth * DstJPGHeight

print("DstJPG Information")
print("   DstJPG Width:", DstJPGWidth)
print("   DstJPG Height:", DstJPGHeight)
print("   DstJPG Size", DstJPGSize)   

if SrcJPGHeight != DstJPGHeight or SrcJPGWidth != DstJPGWidth or SrcJPGSize != DstJPGSize :
    print('比較するファイルを2つ指定してください')

# STEP4 SSIM Calculate
print("========== SSIM Calculate ==========")
SSIM_opencv, _ = cv2.quality.QualitySSIM_compute(SrcJPGImage, DstJPGImage)
print("SSIM Evaluation Results")
print("   SSIM OpenCV (Blue): " + str(SSIM_opencv[0]))
print("   SSIM OpenCV (Green): " + str(SSIM_opencv[1]))
print("   SSIM OpenCV (Red): " + str(SSIM_opencv[2]))
print("   SSIM OpenCV (RGB Average): " + str((SSIM_opencv[0] + SSIM_opencv[1] + SSIM_opencv[2]) / 3))
print("========== SSIM Calculate End==========")

# STEP5 Save CSV
print("========== CSV Write ==========")
with open("./output-ssim-jpg.csv", "w") as f:
    # Header
    f.write("SrcJPG:" + SrcJPGPath + "\n")
    f.write("DstJPG:" + DstJPGPath + "\n")
    f.write("SSIM OpenCV (Blue): " + str(SSIM_opencv[0])+"\n")
    f.write("SSIM OpenCV (Green): " + str(SSIM_opencv[1])+"\n")
    f.write("SSIM OpenCV (Red): " + str(SSIM_opencv[2])+"\n")
    f.write("SSIM OpenCV (RGB Average): " + str((SSIM_opencv[0] + SSIM_opencv[1] + SSIM_opencv[2]) / 3)+"\n")
print("========== CSV Write End==========")
print("End")
