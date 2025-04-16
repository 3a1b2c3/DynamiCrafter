<<<<<<< HEAD
## ___***FreeNoise: Tuning-Free Longer Video Diffusion via Noise Rescheduling***___

### 🔥🔥🔥 The LongerCrafter for longer high-quality video generation are now released!

<div align="center">
<p style="font-weight: bold">
✅ totally <span style="color: red; font-weight: bold">no</span> tuning &nbsp;&nbsp;&nbsp;&nbsp;
✅ less than <span style="color: red; font-weight: bold">20%</span> extra time &nbsp;&nbsp;&nbsp;&nbsp;
✅ support <span style="color: red; font-weight: bold">512</span> frames &nbsp;&nbsp;&nbsp;&nbsp;
</p>

 <a href='https://arxiv.org/abs/2310.15169'><img src='https://img.shields.io/badge/arXiv-2310.15169-b31b1b.svg'></a> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
 <a href='http://haonanqiu.com/projects/FreeNoise.html'><img src='https://img.shields.io/badge/Project-Page-Green'></a> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
 [![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/MoonQiu/FreeNoise) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
 [![Replicate](https://replicate.com/cjwbw/longercrafter/badge)](https://replicate.com/cjwbw/longercrafter)


_**[Haonan Qiu](http://haonanqiu.com/), [Menghan Xia*](https://menghanxia.github.io), [Yong Zhang](https://yzhang2016.github.io), [Yingqing He](https://github.com/YingqingHe), 
<br>
[Xintao Wang](https://xinntao.github.io), [Ying Shan](https://scholar.google.com/citations?hl=zh-CN&user=4oXBp9UAAAAJ), and [Ziwei Liu*](https://liuziwei7.github.io/)**_
<br><br>
(* corresponding author)

From Tencent AI Lab and Nanyang Technological University.

<img src=assets/t2v/hd01.gif>
<p>Input: "A chihuahua in astronaut suit floating in space, cinematic lighting, glow effect"; 
<br>
Resolution: 1024 x 576; Frames: 64.</p>
<img src=assets/t2v/hd02.gif>
<p>Input: "Campfire at night in a snowy forest with starry sky in the background"; 
<br>
Resolution: 1024 x 576; Frames: 64.</p>
</div>
 
## 🔆 Introduction


🤗🤗🤗 LongerCrafter (FreeNoise) is a tuning-free and time-efficient paradigm for longer video generation based on pretrained video diffusion models.

### 1. Longer Single-Prompt Text-to-video Generation

<div align="center">
<img src=assets/t2v/sp512.gif>
<p>Longer single-prompt results. Resolution: 256 x 256; Frames: 512. (Compressed)</p>
</div>

### 2. Longer Multi-Prompt Text-to-video Generation

<div align="center">
<img src=assets/t2v/mp256.gif>
<p>Longer multi-prompt results. Resolution: 256 x 256; Frames: 256. (Compressed)</p>
</div>

## 📝 Changelog
- __[2024.01.28]__: 🔥🔥 Support FreeNoise on VideoCrafter2!
- __[2024.01.23]__: 🔥🔥 Support FreeNoise on other two video frameworks AnimateDiff and LaVie!
- __[2023.10.25]__: 🔥🔥 Release the 256x256 model and support multi-prompt generation!
- __[2023.10.24]__: 🔥🔥 Release the LongerCrafter (FreeNoise), longer video generation!
=======
## ___***DynamiCrafter: Animating Open-domain Images with Video Diffusion Priors***___
<!-- ![](./assets/logo_long.png#gh-light-mode-only){: width="50%"} -->
<!-- ![](./assets/logo_long_dark.png#gh-dark-mode-only=100x20) -->
<div align="center">
<img src='assets/logo_long.png' style="height:100px"></img>




 <a href='https://arxiv.org/abs/2310.12190'><img src='https://img.shields.io/badge/arXiv-2310.12190-b31b1b.svg'></a> &nbsp;
 <a href='https://doubiiu.github.io/projects/DynamiCrafter/'><img src='https://img.shields.io/badge/Project-Page-Green'></a> &nbsp;
 <a href='https://huggingface.co/papers/2310.12190'><img src='https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Page-blue'></a> &nbsp;
<a href='https://youtu.be/0NfmIsNAg-g'><img src='https://img.shields.io/badge/Youtube-Video-b31b1b.svg'></a><br>
[![Open in OpenXLab](https://cdn-static.openxlab.org.cn/app-center/openxlab_app.svg)](https://openxlab.org.cn/apps/detail/JinboXING/DynamiCrafter)&nbsp;&nbsp;
<a href='https://replicate.com/camenduru/dynami-crafter-576x1024'><img src='https://img.shields.io/badge/replicate-Demo-blue'></a>&nbsp;&nbsp;
<a href='https://github.com/camenduru/DynamiCrafter-colab'><img src='https://img.shields.io/badge/Colab-Demo-Green'></a>&nbsp;
<a href='https://huggingface.co/spaces/Doubiiu/DynamiCrafter'><img src='https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face%20ImageAnimation-Demo-blue'></a>&nbsp;
<a href='https://huggingface.co/spaces/Doubiiu/DynamiCrafter_interp_loop'><img src='https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face%20Interpolation/Looping-Demo-blue'></a>&nbsp;
<a href='https://openbayes.com/console/public/tutorials/XMVDVpXKN5o'><img src='https://img.shields.io/badge/Demo-OpenBayes贝式计算-blue'></a>

_**[Jinbo Xing](https://doubiiu.github.io/), [Menghan Xia](https://menghanxia.github.io), [Yong Zhang](https://yzhang2016.github.io), [Haoxin Chen](), [Wangbo Yu](), <br>[Hanyuan Liu](https://github.com/hyliu), [Gongye Liu](), [Xintao Wang](https://xinntao.github.io/), [Ying Shan](https://scholar.google.com/citations?hl=en&user=4oXBp9UAAAAJ&view_op=list_works&sortby=pubdate), [Tien-Tsin Wong](https://ttwong12.github.io/myself.html)**_
<br><br>
From CUHK and Tencent AI Lab.

<strong>at European Conference on Computer Vision (ECCV) 2024, Oral</strong>
</div>
 
## 🔆 Introduction
🔥🔥 Training / Fine-tuning code is available NOW!!!

🔥 We 1024x576 version ranks 1st on the I2V benchmark list from [VBench](https://huggingface.co/spaces/Vchitect/VBench_Leaderboard)!<br>
🔥 Generative frame interpolation / looping video generation model weights (320x512) have been released!<br>
🔥 New Update Rolls Out for DynamiCrafter! Better Dynamic, Higher Resolution, and Stronger Coherence! <br>
🤗 DynamiCrafter can animate open-domain still images based on <strong>text prompt</strong> by leveraging the pre-trained video diffusion priors. Please check our project page and paper for more information. <br>


👀 Seeking comparisons with [Stable Video Diffusion](https://stability.ai/news/stable-video-diffusion-open-ai-video-model) and [PikaLabs](https://pika.art/)? Click the image below.
[![](https://img.youtube.com/vi/0NfmIsNAg-g/0.jpg)](https://www.youtube.com/watch?v=0NfmIsNAg-g)


### 1.1. Showcases (576x1024)
<table class="center">
  <!-- <tr>
    <td colspan="1">"fireworks display"</td>
    <td colspan="1">"a robot is walking through a destroyed city"</td>
  </tr> -->
  <tr>
  <td>
    <img src=assets/showcase/firework03.gif width="340">
  </td>
  <td>
    <img src=assets/showcase/robot01.gif width="340">
  </td>
  </tr>

  <!-- <tr>
    <td colspan="1">"riding a bike under a bridge"</td>
    <td colspan="1">""</td>
  </tr> -->
  <tr>
  <td>
    <img src=assets/showcase/bike_chineseink.gif width="340">
  </td>
  <td>
    <img src=assets/showcase/girl07.gif width="340">
  </td>
  </tr>
</table>


### 1.2. Showcases (320x512)
<table class="center">
  <!-- <tr>
    <td colspan="1">"fireworks display"</td>
    <td colspan="1">"a robot is walking through a destroyed city"</td>
  </tr> -->
  <tr>
  <td>
    <img src=assets/showcase/bloom2.gif width="340">
  </td>
  <td>
    <img src=assets/showcase/train_anime02.gif width="340">
  </td>
  </tr>

  <!-- <tr>
    <td colspan="1">"riding a bike under a bridge"</td>
    <td colspan="1">""</td>
  </tr> -->
  <tr>
  <td>
    <img src=assets/showcase/pour_honey.gif width="340">
  </td>
  <td>
    <img src=assets/showcase/lighthouse.gif width="340">
  </td>
  </tr>
</table>




### 1.3. Showcases (256x256)

<table class="center">
  <tr>
    <td colspan="2">"bear playing guitar happily, snowing"</td>
    <td colspan="2">"boy walking on the street"</td>
  </tr>
  <tr>
  <td>
    <img src=assets/showcase/guitar0.jpeg_00.png width="170">
  </td>
  <td>
    <img src=assets/showcase/guitar0.gif width="170">
  </td>
  <td>
    <img src=assets/showcase/walk0.png_00.png width="170">
  </td>
  <td>
    <img src=assets/showcase/walk0.gif width="170">
  </td>
  </tr>


  <!-- <tr>
    <td colspan="2">"two people dancing"</td>
    <td colspan="2">"girl talking and blinking"</td>
  </tr>
  <tr>
  <td>
    <img src=assets/showcase/dance1.jpeg_00.png width="170">
  </td>
  <td>
    <img src=assets/showcase/dance1.gif width="170">
  </td>

  <td>
    <img src=assets/showcase/girl3.jpeg_00.png width="170">
  </td>
  <td>
    <img src=assets/showcase/girl3.gif width="170">
  </td>
  </tr> -->


  <!-- <tr>
    <td colspan="2">"zoom-in, a landscape, springtime"</td>
    <td colspan="2">"A blonde woman rides on top of a moving <br>washing machine into the sunset."</td>
  </tr>
  <tr>
  <td>
    <img src=assets/showcase/Upscaled_Aime_Tribolet_springtime_landscape_golden_hour_morning_pale_yel_e6946f8d-37c1-4ce8-bf62-6ba90d23bd93.mp4_00.png width="170">
  </td>
  <td>
    <img src=assets/showcase/Upscaled_Aime_Tribolet_springtime_landscape_golden_hour_morning_pale_yel_e6946f8d-37c1-4ce8-bf62-6ba90d23bd93.gif width="170">
  </td>

  <td>
    <img src=assets/showcase/Upscaled_Alex__State_Blonde_woman_riding_on_top_of_a_moving_washing_mach_c31acaa3-dd30-459f-a109-2d2eb4c00fe2.mp4_00.png width="170">
  </td>
  <td>
    <img src=assets/showcase/Upscaled_Alex__State_Blonde_woman_riding_on_top_of_a_moving_washing_mach_c31acaa3-dd30-459f-a109-2d2eb4c00fe2.gif width="170">
  </td>
  </tr>

  <tr>
    <td colspan="2">"explode colorful smoke coming out"</td>
    <td colspan="2">"a bird on the tree branch"</td>
  </tr>
  <tr>
  <td>
    <img src=assets/showcase/explode0.jpeg_00.png width="170">
  </td>
  <td>
    <img src=assets/showcase/explode0.gif width="170">
  </td>

  <td>
    <img src=assets/showcase/bird000.jpeg width="170">
  </td>
  <td>
    <img src=assets/showcase/bird000.gif width="170">
  </td>
  </tr> -->
</table >

### 2. Applications
#### 2.1 Storytelling video generation (see project page for more details)
<table class="center">
    <!-- <tr style="font-weight: bolder;text-align:center;">
        <td>Input</td>
        <td>Output</td>
        <td>Input</td>
        <td>Output</td>
    </tr> -->
  <tr>
    <td colspan="4"><img src=assets/application/storytellingvideo.gif width="250"></td>
  </tr>
</table >

#### 2.2 Generative frame interpolation

<table class="center">
    <tr style="font-weight: bolder;text-align:center;">
        <td>Input starting frame</td>
        <td>Input ending frame</td>
        <td>Generated video</td>
    </tr>
  <tr>
  <td>
    <img src=assets/application/gkxX0kb8mE8_input_start.png width="250">
  </td>
  <td>
    <img src=assets/application/gkxX0kb8mE8_input_end.png width="250">
  </td>
  <td>
    <img src=assets/application/gkxX0kb8mE8.gif width="250">
  </td>
  </tr>


   <tr>
  <td>
    <img src=assets/application/smile_start.png width="250">
  </td>
  <td>
    <img src=assets/application/smile_end.png width="250">
  </td>
  <td>
    <img src=assets/application/smile.gif width="250">
  </td>
  </tr>
  <tr>
  <td>
    <img src=assets/application/stone01_start.png width="250">
  </td>
  <td>
    <img src=assets/application/stone01_end.png width="250">
  </td>
  <td>
    <img src=assets/application/stone01.gif width="250">
  </td>
  </tr> 
</table >

#### 2.3 Looping video generation
<table class="center">

  <tr>
  <td>
    <img src=assets/application/60.gif width="300">
  </td>
  <td>
    <img src=assets/application/35.gif width="300">
  </td>
  <td>
    <img src=assets/application/36.gif width="300">
  </td>
  </tr>
  <!-- <tr>
  <td>
    <img src=assets/application/05.gif width="300">
  </td>
  <td>
    <img src=assets/application/25.gif width="300">
  </td>
  <td>
    <img src=assets/application/34.gif width="300">
  </td>
  </tr> -->
</table >





## 📝 Changelog
- __[2024.06.14]__: 🔥🔥 Release training code for interpolation.
- __[2024.05.24]__: Release WebVid10M-motion annotations.
- __[2024.05.05]__: Release training code.
- __[2024.03.14]__: Release generative frame interpolation and looping video models (320x512).
- __[2024.02.05]__: Release high-resolution models (320x512 & 576x1024).
- __[2023.12.02]__: Launch the local Gradio demo.
- __[2023.11.29]__: Release the main model at a resolution of 256x256.
- __[2023.11.27]__: Launch the project page and update the arXiv preprint.
>>>>>>> 859021927d8e0f8eb4d91d16f86711b8c25a2023
<br>


## 🧰 Models

<<<<<<< HEAD
|Model|Resolution|Checkpoint|Description
|:---------|:---------|:--------|:--------|
|VideoCrafter (Text2Video)|576x1024|[Hugging Face](https://huggingface.co/VideoCrafter/Text2Video-1024-v1.0/blob/main/model.ckpt)|Support 64 frames on NVIDIA A100 (40GB)
|VideoCrafter (Text2Video)|256x256|[Hugging Face](https://huggingface.co/VideoCrafter)|Support 512 frames on NVIDIA A100 (40GB)
|VideoCrafter2 (Text2Video)|320x512|[Hugging Face](https://huggingface.co/VideoCrafter/VideoCrafter2/blob/main/model.ckpt)|Support 128 frames on NVIDIA A100 (40GB)

(Reduce the number of frames when you have smaller GPUs, e.g. 256x256 resolutions with 64 frames.)
=======
|Model|Resolution|GPU Mem. & Inference Time (A100, ddim 50steps)|Checkpoint|
|:---------|:---------|:--------|:--------|
|DynamiCrafter1024|576x1024|18.3GB & 75s (`perframe_ae=True`)|[Hugging Face](https://huggingface.co/Doubiiu/DynamiCrafter_1024/blob/main/model.ckpt)|
|DynamiCrafter512|320x512|12.8GB & 20s (`perframe_ae=True`)|[Hugging Face](https://huggingface.co/Doubiiu/DynamiCrafter_512/blob/main/model.ckpt)|
|DynamiCrafter256|256x256|11.9GB  & 10s (`perframe_ae=False`)|[Hugging Face](https://huggingface.co/Doubiiu/DynamiCrafter/blob/main/model.ckpt)|
|DynamiCrafter512_interp|320x512|12.8GB & 20s (`perframe_ae=True`)|[Hugging Face](https://huggingface.co/Doubiiu/DynamiCrafter_512_Interp/blob/main/model.ckpt)|


Currently, our DynamiCrafter can support generating videos of up to 16 frames with a resolution of 576x1024. The inference time can be reduced by using fewer DDIM steps.

GPU memory consumed on RTX 4090 reported by @noguchis in [Twitter](https://x.com/noguchis/status/1754488826016432341?s=20): 18.3GB (576x1024), 12.8GB (320x512), 11.9GB (256x256).
<!-- It takes approximately 10 seconds and requires a peak GPU memory of 20 GB to animate an image using a single NVIDIA A100 (40G) GPU. -->
>>>>>>> 859021927d8e0f8eb4d91d16f86711b8c25a2023

## ⚙️ Setup

### Install Environment via Anaconda (Recommended)
```bash
<<<<<<< HEAD
conda create -n freenoise python=3.8.5
conda activate freenoise
=======
conda create -n dynamicrafter python=3.8.5
conda activate dynamicrafter
>>>>>>> 859021927d8e0f8eb4d91d16f86711b8c25a2023
pip install -r requirements.txt
```


<<<<<<< HEAD
## 💫 Inference 
### 1. Longer Text-to-Video

<!-- 1) Download pretrained T2V models via [Hugging Face](https://huggingface.co/VideoCrafter/Text2Video-512-v1/blob/main/model.ckpt), and put the `model.ckpt` in `checkpoints/base_512_v1/model.ckpt`.
2) Input the following commands in terminal.
```bash
  sh scripts/run_text2video_freenoise_512.sh
``` -->

1) Download pretrained T2V models via [Hugging Face](https://huggingface.co/VideoCrafter/Text2Video-1024-v1.0/blob/main/model.ckpt), and put the `model.ckpt` in `checkpoints/base_1024_v1/model.ckpt`.
2) Input the following commands in terminal.
```bash
  sh scripts/run_text2video_freenoise_1024.sh
```

### 2. Longer Multi-Prompt Text-to-Video

1) Download pretrained T2V models via [Hugging Face](https://huggingface.co/VideoCrafter), and put the `model.ckpt` in `checkpoints/base_256_v1/model.ckpt`.
2) Input the following commands in terminal.
```bash
  sh scripts/run_text2video_freenoise_mp_256.sh
```


## 🧲 Support For Other Models

FreeNoise is supposed to work on other similar frameworks. An easy way to test compatibility is by shuffling the noise to see whether a new similar video can be generated (set eta to 0). If your have any questions about applying FreeNoise to other frameworks, feel free to contact [Haonan Qiu](http://haonanqiu.com/).

Current official implementation: [FreeNoise-VideoCrafter](https://github.com/AILab-CVC/FreeNoise), [FreeNoise-AnimateDiff](https://github.com/arthur-qiu/FreeNoise-AnimateDiff), [FreeNoise-LaVie](https://github.com/arthur-qiu/FreeNoise-LaVie) 


## 👨‍👩‍👧‍👦 Crafter Family
[VideoCrafter](https://github.com/AILab-CVC/VideoCrafter): Framework for high-quality video generation.
=======
## 💫 Inference
### 1. Command line
### Image-to-Video Generation
1) Download pretrained models via Hugging Face, and put the `model.ckpt` with the required resolution in `checkpoints/dynamicrafter_[1024|512|256]_v1/model.ckpt`.
2) Run the commands based on your devices and needs in terminal.
```bash
  # Run on a single GPU:
  # Select the model based on required resolutions: i.e., 1024|512|320:
  sh scripts/run.sh 1024
  # Run on multiple GPUs for parallel inference:
  sh scripts/run_mp.sh 1024
```

### Generative Frame Interpolation / Looping Video Generation
Download pretrained model DynamiCrafter512_interp and put the `model.ckpt` in `checkpoints/dynamicrafter_512_interp_v1/model.ckpt`.
```bash
  sh scripts/run_application.sh interp # Generate frame interpolation
  sh scripts/run_application.sh loop   # Looping video generation
```


### 2. Local Gradio demo
### Image-to-Video Generation
1. Download the pretrained models and put them in the corresponding directory according to the previous guidelines.
2. Input the following commands in terminal (choose a model based on the required resolution: 1024, 512 or 256).
```bash
  python gradio_app.py --res 1024
```

### Generative Frame Interpolation / Looping Video Generation
Download the pretrained model and put it in the corresponding directory according to the previous guidelines.
```bash
  python gradio_app_interp_and_loop.py 
```

## 💥 Training / Fine-tuning
### Image-to-Video Generation
0. Download the WebVid Dataset, and important items in `.csv` are `page_dir`, `videoid`, and `name`.
1. Download the pretrained models and put them in the corresponding directory according to the previous guidelines.
2. Change `<YOUR_SAVE_ROOT_DIR>` path in `training_[1024|512]_v1.0/run.sh`
3. Carefully check all paths in `training_[1024|512]_v1.0/config.yaml`, including `model:pretrained_checkpoint`, `data:data_dir`, and `data:meta_path`.
4. Input the following commands in terminal (choose a model based on the required resolution: 1024 or 512).

We adopt `DDPShardedStrategy` by default for training, please make sure it is available in your pytorch_lightning.
```bash
  sh configs/training_1024_v1.0/run.sh ## fine-tune DynamiCrafter1024
```
5. All the checkpoints/tensorboard record/loginfo will be saved in `<YOUR_SAVE_ROOT_DIR>`.

### Generative Frame Interpolation
Download pretrained model DynamiCrafter512_interp and put the `model.ckpt` in `checkpoints/dynamicrafter_512_interp_v1/model.ckpt`. Follow the same fine-tuning procedure in "Image-to-Video Generation", and run the script below:
```bash
sh configs/training_512_v1.0/run_interp.sh
```


## 🎁 WebVid-10M-motion annotations (~2.6M)
The annoations of our WebVid-10M-motion is available on [Huggingface Dataset](https://huggingface.co/datasets/Doubiiu/webvid10m_motion). In addition to the original annotations, we add three more motion-related annotations: `dynamic_confidence`, `dynamic_wording`, and `dynamic_source_category`. Please refer to our [supplementary document](https://arxiv.org/pdf/2310.12190) (Section D) for more details.




## 🤝 Community Support

1. ComfyUI and pruned models (bf16): [ComfyUI-DynamiCrafterWrapper](https://github.com/kijai/ComfyUI-DynamiCrafterWrapper) (Thanks to [kijai](https://twitter.com/kijaidesign))


|Model|Resolution|GPU Mem. |Checkpoint|
|:---------|:---------|:--------|:--------|
|DynamiCrafter1024|576x1024|10GB |[Hugging Face](https://huggingface.co/Kijai/DynamiCrafter_pruned/blob/main/dynamicrafter_1024_v1_bf16.safetensors)|
|DynamiCrafter512_interp|320x512|8GB |[Hugging Face](https://huggingface.co/Kijai/DynamiCrafter_pruned/blob/main/dynamicrafter_512_interp_v1_bf16.safetensors)|


2. ComfyUI: [ComfyUI-DynamiCrafter](https://github.com/chaojie/ComfyUI-DynamiCrafter) (Thanks to [chaojie](https://github.com/chaojie))

3. ComfyUI: [ComfyUI_Native_DynamiCrafter](https://github.com/ExponentialML/ComfyUI_Native_DynamiCrafter) (Thanks to [ExponentialML](https://github.com/ExponentialML))

4. Docker: [DynamiCrafter_docker](https://github.com/maximofn/DynamiCrafter_docker) (Thanks to [maximofn](https://github.com/maximofn))


## 👨‍👩‍👧‍👦 Crafter Family
[VideoCrafter1](https://github.com/AILab-CVC/VideoCrafter): Framework for high-quality video generation.
>>>>>>> 859021927d8e0f8eb4d91d16f86711b8c25a2023

[ScaleCrafter](https://github.com/YingqingHe/ScaleCrafter): Tuning-free method for high-resolution image/video generation.

[TaleCrafter](https://github.com/AILab-CVC/TaleCrafter): An interactive story visualization tool that supports multiple characters.  

<<<<<<< HEAD

## 😉 Citation
```bib
@misc{qiu2023freenoise,
      title={FreeNoise: Tuning-Free Longer Video Diffusion Via Noise Rescheduling}, 
      author={Haonan Qiu and Menghan Xia and Yong Zhang and Yingqing He and Xintao Wang and Ying Shan and Ziwei Liu},
      year={2023},
      eprint={2310.15169},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```


## 📢 Disclaimer
We develop this repository for RESEARCH purposes, so it can only be used for personal/research/non-commercial purposes.
****

=======
[LongerCrafter](https://github.com/arthur-qiu/LongerCrafter): Tuning-free method for longer high-quality video generation.  

[MakeYourVideo, might be a Crafter:)](https://doubiiu.github.io/projects/Make-Your-Video/): Video generation/editing with textual and structural guidance.

[StyleCrafter](https://gongyeliu.github.io/StyleCrafter.github.io/): Stylized-image-guided text-to-image and text-to-video generation.

[ViewCrafter](https://github.com/Drexubery/ViewCrafter): Novel view synthesis by taming camera-pose-controlled DynamiCrafter.
## 😉 Citation
Please consider citing our paper if our code and dataset annotations are useful:
```bib
@article{xing2023dynamicrafter,
  title={DynamiCrafter: Animating Open-domain Images with Video Diffusion Priors},
  author={Xing, Jinbo and Xia, Menghan and Zhang, Yong and Chen, Haoxin and Yu, Wangbo and Liu, Hanyuan and Wang, Xintao and Wong, Tien-Tsin and Shan, Ying},
  journal={arXiv preprint arXiv:2310.12190},
  year={2023}
}
```

## 🙏 Acknowledgements
We would like to thank [AK(@_akhaliq)](https://twitter.com/_akhaliq?lang=en) for the help of setting up hugging face online demo, and [camenduru](https://twitter.com/camenduru) for providing the replicate & colab online demo, and [Xinliang](https://github.com/dailingx) for his support and contribution to the open source project.

## 📢 Disclaimer
This project strives to impact the domain of AI-driven video generation positively. Users are granted the freedom to create videos using this tool, but they are expected to comply with local laws and utilize it responsibly. The developers do not assume any responsibility for potential misuse by users.
****
>>>>>>> 859021927d8e0f8eb4d91d16f86711b8c25a2023
