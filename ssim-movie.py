from cv2 import VideoCapture
import numpy as np
import cv2
import sys

def AddGaussianNoise(image, mean, sigma):
    noise = np.random.normal(mean, sigma, np.shape(image))
    noisy_image = image + noise
    noisy_image[noisy_image > 255] = 255
    noisy_image[noisy_image < 0] = 0
    noisy_image = noisy_image.astype(np.uint8)    # Float -> Uint
    return noisy_image


# README

print("OpenCV Version: " + str(cv2.__version__))
print("Start")

# STEP1 Movie Read

args = sys.argv

if len(args) !=2 :
    print('Arguments are too short')
    

print(args[1])
print(args[2])


print("========== Print SrcVideo Information ==========")
SrcVideoPath = "./test1.mp4"
SrcVideoCap = cv2.VideoCapture(SrcVideoPath)
print(f"SrcVideoWidth: {SrcVideoCap.get(cv2.CAP_PROP_FRAME_WIDTH)}")
print(f"SrcVideoHeight: {SrcVideoCap.get(cv2.CAP_PROP_FRAME_HEIGHT)}")
print(f"SrcVideoFps: {SrcVideoCap.get(cv2.CAP_PROP_FPS)}")
print(f"SrcVideoFrameCount: {SrcVideoCap.get(cv2.CAP_PROP_FRAME_COUNT)}")
print(f"SrcVideoLength: {SrcVideoCap.get(cv2.CAP_PROP_FRAME_COUNT) / SrcVideoCap.get(cv2.CAP_PROP_FPS)} s")
print(f"SrcVideoFourcc: " + int(SrcVideoCap.get(cv2.CAP_PROP_FOURCC)).to_bytes(4, "little").decode("utf-8"))

print("========== Print DstVideo Information ==========")
DstVideoPath = "./test1.mp4"
DstVideoCap = cv2.VideoCapture(DstVideoPath)
print(f"DstVideoWidth: {DstVideoCap.get(cv2.CAP_PROP_FRAME_WIDTH)}")
print(f"DstVideoHeight: {DstVideoCap.get(cv2.CAP_PROP_FRAME_HEIGHT)}")
print(f"DstVideoFps: {DstVideoCap.get(cv2.CAP_PROP_FPS)}")
print(f"DstVideoFrameCount: {DstVideoCap.get(cv2.CAP_PROP_FRAME_COUNT)}")
print(f"DstVideoLength: {DstVideoCap.get(cv2.CAP_PROP_FRAME_COUNT) / DstVideoCap.get(cv2.CAP_PROP_FPS)} s")
print(f"DstVideoFourcc: " + int(DstVideoCap.get(cv2.CAP_PROP_FOURCC)).to_bytes(4, "little").decode("utf-8"))



# STEP2 CaptureFolder Make
print("========== CaptureFolder Make ==========")
# *****

# STEP3 Movie Capture
print("========== Print SrcVideo Capture ==========")
SrcVideoCapture = cv2.VideoCapture(SrcVideoPath)
totalFrames = SrcVideoCapture.get(cv2.CAP_PROP_FRAME_COUNT)
success,image = SrcVideoCapture.read()
count = 0
while success:
    cv2.imwrite("./frameSrcVideo/frame%d.jpg" % count, image)
    success,image = SrcVideoCapture.read()
    count += 1
    # Print Counter

print("SrcVideoCapture End!")

print("========== Print DstVideo Capture ==========")
DstVideoCapture = cv2.VideoCapture(DstVideoPath)
totalFrames = DstVideoCapture.get(cv2.CAP_PROP_FRAME_COUNT)
success,image = DstVideoCapture.read()
count = 0
while success:
    cv2.imwrite("./frameDstVideo/frame%d.jpg" % count, image)
    success,image = DstVideoCapture.read()
    count += 1
    # Print Counter

print("DstVideoCapture End!")


# (DEBUG) Add Noise
sigma = 5
for i in range(count):
    DstVideoImage = cv2.imread("./frameDstVideo/frame"+str(i)+".jpg", cv2.IMREAD_COLOR)
    noisy_image = AddGaussianNoise(DstVideoImage, 0, sigma)
    cv2.imwrite("frameDstVideo/frame"+str(i)+".jpg",noisy_image)


# STEP4 SSIM Calculate
print("========== SSIM Calculate ==========")

with open("./output-ssim-jpg.csv", "w") as f:
    f.write("FrameCount, FrameSec , SSIM \n")
    for i in range(count):
        SrcVideoImage = cv2.imread("./frameSrcVideo/frame"+str(i)+".jpg", cv2.IMREAD_COLOR)
        DstVideoImage = cv2.imread("./frameDstVideo/frame"+str(i)+".jpg", cv2.IMREAD_COLOR)
        SSIM_opencv, _ = cv2.quality.QualitySSIM_compute(SrcVideoImage, DstVideoImage)
        print("SSIM Evaluation Results")
        print("   SSIM OpenCV (Blue): " + str(SSIM_opencv[0]))
        print("   SSIM OpenCV (Green): " + str(SSIM_opencv[1]))
        print("   SSIM OpenCV (Red): " + str(SSIM_opencv[2]))
        print("   SSIM OpenCV (RGB Average): " + str((SSIM_opencv[0] + SSIM_opencv[1] + SSIM_opencv[2]) / 3))
        print("   Count: " + str(i))
        f.write( str(i) + "," + str(round(i * (1.0/ float(SrcVideoCap.get(cv2.CAP_PROP_FPS))),2)) + "s," + str((SSIM_opencv[0] + SSIM_opencv[1] + SSIM_opencv[2]) / 3)+"\n")
        #f.write( i+ "," + i * ( 1.0 / int(SrcVideoCap.get(cv2.CAP_PROP_FPS)))  + "s," + str((SSIM_opencv[0] + SSIM_opencv[1] + SSIM_opencv[2]) / 3)+"\n")

print("========== SSIM Calculate End==========")

print("End")

