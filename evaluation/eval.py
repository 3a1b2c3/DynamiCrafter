import torch
import sys

sys.path.insert(0, "C:\workspace\cs231n\proj\common_metrics_on_video_quality")
from calculate_fvd import calculate_fvd
from calculate_psnr import calculate_psnr
from calculate_ssim import calculate_ssim
from calculate_lpips import calculate_lpips
import cv2
import numpy as np


def load_video_to_numpy(path, resize=None, max_frames=None):
    cap = cv2.VideoCapture(path)
    frames = []
    print("____cap.isOpened():", cap.isOpened(), path)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        if resize:
            frame = cv2.resize(frame, resize)  # e.g., (width, height)

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB
        frames.append(frame)

        if max_frames and len(frames) >= max_frames:
            break
    print("frames:", len(frames))
    cap.release()
    return np.stack(frames)  # Shape: (T, H, W, 3)


NUMBER_OF_VIDEOS = 2
VIDEO_LENGTH = 16
CHANNEL = 3
SIZE = 320
SIZE2 = 512
videos1a = torch.zeros(
    NUMBER_OF_VIDEOS, VIDEO_LENGTH, CHANNEL, SIZE, SIZE2, requires_grad=False
)
videos2a = torch.ones(
    NUMBER_OF_VIDEOS, VIDEO_LENGTH, CHANNEL, SIZE, SIZE2, requires_grad=False
)
device = torch.device("cuda")
# device = torch.device("cpu")
# Example
# calculate_fvd(videos1, videos2, only_final=True)
# output:
# [fvd-tensorflow] [151.39244]
# For pixel value: Make sure the pixel value of videos should be in [0, 1]
v1 = r"C:\workspace\cs231n\proj\DynamiCrafter\output\50samples\slowly_going_down_the_street.mp4"
v2 = r"C:\workspace\cs231n\proj\DynamiCrafter\output\150samples\slowly_going_down_the_street.mp4"
''' 
v1 = r"C:\workspace\cs231n\proj\DynamiCrafter\output\50samples\slowly_going_down_the_street.mp4"
v2 = r"C:\workspace\cs231n\proj\DynamiCrafter\output\150samples\slowly_going_down_the_street.mp4"
v3 = r"C:\workspace\cs231n\proj\DynamiCrafter\output\eta0.5\slowly_going_down_the_street.mp4"
v2 = v3
v1 = r"C:\workspace\cs231n\proj\DynamiCrafterLora\output\backstreet_582\
v2 = r"C:\workspace\cs231n\proj\DynamiCrafter\output\150samples\slowly_going_down_the_street.mp4"
v2 = r"C:\workspace\cs231n\proj\DynamiCrafter\output\150samples\slowly_going_down_the_street.mp4"
#ffmpeg.exe -i  "C:\workspace\cs231n\proj\DynamiCrafterLora\output\train\TEST\train_ground_55_16frames_interp.mp4"  -i "C:\workspace\cs231n\proj\DynamiCrafterLora\output\train\TEST\6_st_001no_lora_.a_train_rides_on_the_si.mp4" -lavfi psnr=stats_file=psnr_logfile.txt -f null -  #PSNR y:17.419270
#ffmpeg.exe -i  "C:\workspace\cs231n\proj\DynamiCrafterLora\output\train\TEST\train_ground_55_16frames_interp.mp4"  -i "C:\workspace\cs231n\proj\DynamiCrafterLora\output\train\TEST\6_st_001lora_.a_train_rides_on_the_side_.mp4" -lavfi psnr=stats_file=psnr_logfile.txt -f null - # PSNR y:17.178489 
'''
v1 = r"C:\workspace\cs231n\proj\DynamiCrafterLora\output\train\TEST\train_ground_55_16frames_interp.mp4"
v2 = r"C:\workspace\cs231n\proj\DynamiCrafterLora\output\train\TEST\6_st_001no_lora_.a_train_rides_on_the_si.mp4"
v2a = r"C:\workspace\cs231n\proj\DynamiCrafterLora\output\train\TEST\6_st_001lora_.a_train_rides_on_the_side_.mp4"

v1 = r"C:\workspace\cs231n\proj\DynamiCrafterLora\output\restaurant\TEST\6_st_061lora_.a_backlane_with_restaurant.mp4" 
v2 = r"C:\workspace\cs231n\proj\DynamiCrafterLora\output\restaurant\TEST\6_st_061no_lora_.a_backlane_with_restaur.mp4"

 
#-filter_complex "[0:v]setsar=1:1[v0]; [1:v]setsar=1:1[v1]; [v0][v1]blend=all_mode=difference,format=gray"      -c:v libx264 -crf 18 -pix_fmt yuv420p "C:\workspace\cs231n\proj\DynamiCrafterLora\output\malaga\TEST\malaga_diff_no_lora_lora.mp4"

v1 =r"C:\workspace\cs231n\proj\DynamiCrafterLora\output\malaga\TEST\malaga_ground_73.mp4"
v2 =r"C:\workspace\cs231n\proj\DynamiCrafterLora\output\malaga\TEST\12_st_073no_lora_.driving_around_Malaga.mp4" 
#v2 = r"C:\workspace\cs231n\proj\DynamiCrafterLora\output\malaga\TEST\12_st_073lora_.driving_around_Malaga.mp4" 

v1 = r"C:\workspace\cs231n\proj\DynamiCrafterLora\output\cal\TEST\coma_ground_73.mp4"
v2 = r"C:\workspace\cs231n\proj\DynamiCrafterLora\output\cal\TEST\6_st_001lora_.driving_off_from_a_crossin.mp4"
#v2 = r"C:\workspace\cs231n\proj\DynamiCrafterLora\output\cal\TEST\6_st_001no_lora_.driving_off_from_a_cros.mp4"

#ffmpeg -i "C:\workspace\cs231n\proj\DynamiCrafterLora\output\cal_28\TEST\%03d_result.jpg" -filter_complex "minterpolate=fps=70:mi_mode=mci" "C:\workspace\cs231n\proj\DynamiCrafterLora\output\cal_28\TEST\coma_28_ground_1.mp4"
#ffmpeg -i "C:\workspace\cs231n\proj\DynamiCrafterLora\output\cal_28\TEST\6_st_001lora_.driving_fast_on_highway_in.mp4" -i "C:\workspace\cs231n\proj\DynamiCrafterLora\output\cal_28\TEST\6_st_001no_lora_.driving_fast_on_highway.mp4"   

v1 = r"C:\workspace\cs231n\proj\DynamiCrafterLora\output\suburbia\Test\6_st_126no_lora_.Going_down_a_suburbian_.mp4" 
v1 = r"C:\workspace\cs231n\proj\DynamiCrafterLora\output\suburbia\Test\6_st_120lora_.Going_down_a_suburbian_lea.mp4"  # -filter_complex "[0:v]setsar=1:1[v0]; [1:v]setsar=1:1[v1]; [v0][v1]blend=all_mode=difference,format=gray"      -c:v libx264 -crf 18 -pix_fmt yuv420p "C:\workspace\cs231n\proj\DynamiCrafterLora\output\suburbia\TEST\driving_diff_28_no_lora_lora.mp4"
v2 = r"C:\workspace\cs231n\proj\DynamiCrafterLora\output\suburbia\TEST\Kitti_driving_ground_120.mp4" 
#-i "C:\workspace\cs231n\proj\DynamiCrafterLora\output\suburbia\Test\6_st_126no_lora_.Going_down_a_suburbian_.mp4"  -filter_complex "[0:v]setsar=1:1[v0]; [1:v]setsar=1:1[v1]; [v0][v1]blend=all_mode=difference,format=gray"      -c:v libx264 -crf 18 -pix_fmt yuv420p "C:\workspace\cs231n\proj\DynamiCrafterLora\output\suburbia\TEST\drivingd_no_lora_lora.mp4"
v1 = r"C:\workspace\cs231n\proj\DynamiCrafterLora\output\whiteTruckbarrels_582\5\TEST\5_st_001lora_.discovering_Tokyo_backlane.mp4" 
#-i "C:\workspace\cs231n\proj\DynamiCrafterLora\output\whiteTruckbarrels_582\5\TEST\5_st_001no_lora_.discovering_Tokyo_backl.mp4"   -filter_complex "[0:v]setsar=1:1[v0]; [1:v]setsar=1:1[v1]; [v0][v1]blend=all_mode=difference,format=gray"      -c:v libx264 -crf 18 -pix_fmt yuv420p "C:\workspace\cs231n\proj\DynamiCrafterLora\output\whiteTruckbarrels_582\5\TEST\582_TITAN_no_lora_lora.mp4"
v2 = r"C:\workspace\cs231n\proj\DynamiCrafterLora\output\whiteTruckbarrels_582\5\TEST\582_TITAN_ground1.mp4" 

# -i "C:\workspace\cs231n\proj\DynamiCrafterLora\output\restaurant\TEST\537_ground_61frames.mp
videos1t = load_video_to_numpy(v1, resize=None, max_frames=None) / 255
# x = x.permute(0, 2, 1, 3, 4)
videos1 = torch.from_numpy(np.transpose(videos1t, (0, 3, 1, 2))).float()
videos1 = videos1.unsqueeze(0)

videos2t = (
    load_video_to_numpy(v2, resize=None, max_frames=None) / 255
)  # (torch.cuda.FloatTensor)
videos2 = torch.from_numpy(np.transpose(videos2t, (0, 3, 1, 2))).float()
videos2 = videos2.unsqueeze(0)  #
# print(videos2)
print(
    "videos1.shape", videos1.shape, "videos1a.shape", videos1a.shape, videos2.shape
)  # (num_frames, height, width, 3)
# videos1.shape torch.Size([16, 3, 320, 512]) torch.Size([8, 30, 3, 64, 64])#
# ps: pixel value should be in [0, 1]!
# video_np = video_np.transpose(0, 2, 3, 1)


import json

result = {}
only_final = True
# only_final = True
result["fvd"] = calculate_fvd(
    videos1, videos2, device, method="styleganv", only_final=only_final
)
# result['fvd'] = calculate_fvd(videos1, videos2, device, method='videogpt', only_final=only_final)
result["ssim"] = calculate_ssim(videos1, videos2, only_final=only_final)
result["psnr"] = calculate_psnr(videos1, videos2, only_final=only_final)
result["lpips"] = calculate_lpips(videos1, videos2, device, only_final=only_final)
print(json.dumps(result, indent=4))

""""
fvd
0 = perfect match between real and generated video distributions.
< 100 = often considered high-quality generation (depends on the dataset).
> 200–300 = usually indicates lower quality or poor temporal consistency.

Higher PSNR values (typically above 30 dB) are desirable, as they signify better reconstruction quality

Fréchet Video Distance (FVD)
Scale: 0 (best) to ∞ (worst)

Interpretation:

0–50: Excellent temporal and visual quality

50–200: Good quality

200–500: Moderate quality

500–1000: Poor quality

>1000: Very poor; significant artifacts or instability
arXiv
Wikipedia

An FVD score of 833.46 indicates poor temporal coherence and visual quality in the generated videos.

🖼️ Structural Similarity Index (SSIM)
Scale: 0 (no similarity) to 1 (perfect similarity)

Interpretation:

>0.95: Excellent structural similarity

0.85–0.95: Good similarity

0.70–0.85: Fair similarity

<0.70: Poor similarity
arXiv
+19
Wikipedia
+19
visionular.ai
+19
Paperspace by DigitalOcean Blog
MathWorks
+20
SpringerLink
+20
Artificial Intelligence Stack Exchange
+20

An SSIM of 0.585 ± 0.143 suggests poor structural similarity between the generated and reference images.

🔊 Peak Signal-to-Noise Ratio (PSNR)
Scale: Measured in decibels (dB); higher is better

Interpretation:

>40 dB: Excellent quality

30–40 dB: Good quality

20–30 dB: Fair quality

<20 dB: Poor quality
GitHub
+21
Wikipedia
+21
SpringerLink
+21
MathWorks
+3
Paperspace by DigitalOcean Blog
+3
quality.nfdi4ing.de
+3
GitHub
+7
NI
+7
quality.nfdi4ing.de
+7

A PSNR of 16.78 ± 4.95 dB indicates poor pixel-level fidelity, with noticeable differences from the reference images.

👁️ Learned Perceptual Image Patch Similarity (LPIPS)
Scale: 0 (identical) to 1 (completely different)

Interpretation:

<0.10: Excellent perceptual similarity

0.10–0.20: Good similarity

0.20–0.40: Moderate similarity

>0.40: Poor similarity
Signal Processing Stack Exchange
GitHub
+18
Artificial Intelligence Stack Exchange
+18
Stack Overflow
+18

An LPIPS of 0.166 ± 0.052 indicates good perceptual similarity, though there is room for improvement.
"""
