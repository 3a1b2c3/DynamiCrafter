import os, time
from cog import BasePredictor, Input, Path
import sys

sys.path.insert(0, r"C:\workspace\cs231n\proj\DynamiCrafterLora")
os.chdir(r"C:\workspace\cs231n\proj\DynamiCrafterLora")
ckpt = r"C:\workspace\cs231n\proj\DynamiCrafter\checkpoints\dynamicrafter_256_v1\dynamicrafter_512_interp_v1.ckpt"
ckpt = r"C:\workspace\cs231n\proj\DynamiCrafterLora\checkpoints\dynamicrafter_512_interp_v1\lora\model_train_epoch=0-step=9_applied.ckpt"
ckpt = r"C:\workspace\cs231n\proj\DynamiCrafterLora\checkpoints\dynamicrafter_512_interp_v1\model_train_epoch=0-step=3-v2_applied.ckpt"
ckpt = r"C:\workspace\cs231n\proj\DynamiCrafterLora\checkpoints\dynamicrafter_512_interp_v1\model_train.ckpt"
# C:\workspace\cs231n\proj\DynamiCrafter\configs\training_512_v1.0\config_interp.yaml
# python apply_lora.py --format ckpt --base_model="C:\workspace\cs231n\proj\DynamiCrafterLora\checkpoints\dynamicrafter_512_interp_v1\model_train.ckpt" --lora=C:\workspace\cs231n\proj\DynamiCrafterLora\main\logs\test\checkpoints\old\epoch=0-step=9.ckpt --alpha=1.0
directory = r"C:\workspace\cs231n\proj\DynamiCrafterLora\output"
# C:\workspace\cs231n\proj\DynamiCrafterLora\main\logs\test\checkpoints\old\epoch=0-step=9.ckpt

from PIL import Image

n = "1"
image1_path = (
    r"C:\workspace\cs231n\proj\data\titan_data\TEST\clip_537\images\%s_result.jpg"
    % n.zfill(3)
)

assert os.path.exists(image1_path)
image1 = Image.open(image1_path)

import numpy as np
import torch
from scripts.gradio.i2v_test_application import Image2Video
import scripts.gradio.i2v_test_application

print(
    scripts.gradio.i2v_test_application,
    "scripts.gradio.i2v_test_application:",
    sys.path,
)

"""

base_scale: 1.0  # or 1.2 for stronger conditioning
unet_config:
  params:
    dropout: 0.0
    transformer_depth: 2  # optional
    num_head_channels: 128  # optional
Creative/Controlling Parameters
Parameter
Influence on Creativity
Notes
--ddim_steps
🔥 Higher = more refined, lower = faster but rougher
Reducing steps can lead to more unexpected outputs.
--ddim_eta
🔀 Adds randomness/noise to sampling
0.0 = deterministic (less creative), 1.0 = more stochastic (more variation)
--unconditional_guidance_scale
🎯 Controls prompt influence
Higher = more adherence to prompt, lower = more freedom
--guidance_rescale
📏 Refines how strongly the guidance is applied
Lower = more balanced realism/creativity; useful for better tradeoffs
--prompt
💬 Directly defines the visual concept to be rendered
Changing this creates entirely new scenes or vibes
--multiple_cond_cfg + --cfg_img
🧠 Combine text + image for hybrid creativity
If True, you can vary conditioning strength from image/text
--seed
🎲 Controls random initialization
Changing seed produces visually different samples even with same prompt

"""


class Predictor(BasePredictor):
    def setup(
        self,
        ckpt=None,
        save_fps=10,
        directory=r"C:\workspace\cs231n\proj\DynamiCrafterLora\output",
    ) -> None:
        if not os.path.exists(directory):
            os.mkdir(directory)
        assert ckpt
        self.image2video = Image2Video(
            directory, ckpt_path=ckpt, resolution="320_512", save_fps=save_fps
        )
        #   def __init__(self,  result_dir='./tmp/',  ckpt_path=None, gpu_num=1,resolution='256_256', save_fps = 8) -> None:
        # self.save_fps = 10 # ME

    def predict(
        self,
        image1_path: Path,
        image2_path: Path,
        prompt,
        steps: int = 150, #Input(default=150),
        cfg_scale: float = 12, #Input(default=7.5),
        eta: float = 0.0,
        fs: int = 10,
        seed: int =22306
        # image1_path: Path = Input(description="Input Image 1"),
        # image2_path: Path = Input(description="Input Image 2"),
        # prompt: str = Input(default='a smiling girl'),
        # steps: int = Input(default=50),
        # cfg_scale: float = Input(default=7.5),
        # eta: float = Input(default=1.0),
        # fs: int = Input(default=5),
        # seed: int = Input(default=12306),
    ) -> Path:
        assert isinstance( image1_path, str)
        image1 = Image.open(image1_path)
        if image1.mode == "RGBA":
            image1 = image1.convert("RGB")
        print("image2_path: ", image2_path)
        image2 = Image.open(image2_path)
        if image2.mode == "RGBA":
            image2 = image2.convert("RGB")
        image1_np = np.array(image1)
        image2_np = np.array(image2)
        print(
            self.image2video,
            "_____________ steps, cfg_scale, eta, fs, seed",
            steps,
            cfg_scale,
            eta,
            fs,
            seed,
        )
        # image, prompt, steps=50, cfg_scale=7.5, eta=1.0, fs=3, seed=123, image2=None):
        i2v_output_video = self.image2video.get_image(
            image1_np, prompt, steps, cfg_scale, eta, fs, seed, image2_np
        )
        print(
            "_____________i2v_output_video,  steps, cfg_scale, eta, fs, seed",
            i2v_output_video,
            steps,
            cfg_scale,
            eta,
            fs,
            seed,
        )
        return i2v_output_video


def recursive_predict(path1, prompt, start, end, img_step=6,
        steps=80, #steps=50,
        cfg_scale=8,#>10	Strongly follows the conditioning – may become overly sharp or brittle  cfg_scale=7.5,
        eta=.5, # deterministic   eta=1.0
        fs=10,
        seed=122
):
    for i in range(start, end, img_step):
        n = str(i)
        image1_path = path1 % n.zfill(3)
        n = str(i + 6)
        image2_path = path1 % n.zfill(3)
        assert os.path.exists(image1_path)
        image1 = Image.open(image1_path)
        assert os.path.exists(image2_path)
        image2 = Image.open(image2_path)
        res6 = p.predict(image1_path,
                image2_path,
                prompt,
                steps=80, #steps=50,
                cfg_scale=8,#>10	Strongly follows the conditioning – may become overly sharp or brittle  cfg_scale=7.5,
                eta=.5, # deterministic   eta=1.0
                fs=10,
                seed=122
                )

    return n


# p10 = Predictor()
p = Predictor()
p.setup(
    ckpt=ckpt,
    save_fps=10,
    directory=r"C:\workspace\cs231n\proj\DynamiCrafterLora\output"
)
img_folder = r"C:\workspace\cs231n\proj\data\kitti\TEST\selected"
img_folder_kitti = r"C:\workspace\cs231n\proj\data\kitti\TEST"
f = "2011_09_26_drive_0091_sync"
# 320_512 10 fps, 8 fps, 40 s
"""
configs/inference_512_v1.0.yaml config_file: {'model': {'target': 'lvdm.models.ddpm3d.LatentVisualDiffusion',
'params': {'rescale_betas_zero_snr': True, 'parameterization': 'v', 'linear_start': 0.00085, 'linear_end': 0.012, 'num_timesteps_cond': 1, 
'timesteps': 1000, 'first_stage_key': 'video', 'cond_stage_key': 'caption', 'cond_stage_trainable': False, 'conditioning_key': 'hybrid',
 'image_size': [40, 64], 'channels': 4, 'scale_by_std': False, 'scale_factor': 0.18215, 'use_ema': False, 'uncond_type': 'empty_seq', 
 'use_dynamic_rescale': True, 'base_scale': 0.7, 'fps_condition_type': 'fps', 'perframe_ae': True, 'unet_config': {'target': 'lvdm.modules.networks.openaimodel3d.UNetModel', 'params': {'in_channels': 8, 'out_channels': 4, 'model_channels': 320, 'attention_resolutions': [4, 2, 1], 'num_res_blocks': 2, 'channel_mult': [1, 2, 4, 4], 'dropout': 0.1, 'num_head_channels': 64, 'transformer_depth': 1, 'context_dim': 1024, 'use_linear': True, 'use_checkpoint': True, 'temporal_conv': True, 'temporal_attention': True, 'temporal_selfatt_only': True, 'use_relative_position': False, 'use_causal_attention': False, 'temporal_length': 16, 'addition_attention': True, 'image_cross_attention': True, 'default_fs': 24, 'fs_condition': True}}, 'first_stage_config': {'target': 'lvdm.models.autoencoder.AutoencoderKL', 'params': {'embed_dim': 4, 'monitor': 'val/rec_loss', 'ddconfig': {'double_z': True, 'z_channels': 4, 'resolution': 256, 'in_channels': 3, 'out_ch': 3, 'ch': 128, 'ch_mult': [1, 2, 4, 4], 'num_res_blocks': 2, 'attn_resolutions': [], 'dropout': 0.0}, 'lossconfig': {'target': 'torch.nn.Identity'}}}, 'cond_stage_config': {'target': 'lvdm.modules.encoders.condition.FrozenOpenCLIPEmbedder', 'params': {'freeze': True, 'layer': 'penultimate'}}, 'img_cond_stage_config': {'target': 'lvdm.modules.encoders.condition.FrozenOpenCLIPImageEmbedderV2', 'params': {'freeze': True}}, 'image_proj_stage_config': {'target': 'lvdm.modules.encoders.resampler.resampler', 'params': {'dim': 1024, 'depth': 4, 'dim_head': 64, 'heads': 12, 'num_queries': 16, 'embedding_dim': 1280, 'output_dim': 1024, 'ff_mult': 4, 'video_length': 16}}}}}
python evaluate.py --config configs/ldm/ldmvfi-vqflow-f32-c256-concat_max.yaml --ckpt <path/to/ldmvfi-vqflow-f32-c256-concat_max.ckpt> --dataset Middlebury_others --metrics PSNR SSIM LPIPS \
--data_dir <path/to/data/dir> --out_dir eval_results/ldmvfi-vqflow-f32-c256-concat_max/  --use_ddim
"""


image1_path = r"C:\workspace\cs231n\proj\data\kitti\TEST\image_03_straba\data_strassenbahn\%s_result.jpg"
#recursive_predict(image1_path, "a train rides on the side off the road", 1, 115, 6)

# for i in range(1, 238, 6):
image1_path = r"C:\workspace\cs231n\proj\data\kitti\TEST\2011_09_26_drive_0106_sync\2011_09_26_rad\2011_09_26_drive_0106_sync_red_flying_cam_pedestrinas\image_03\data\%s_result.jpg"
prompt= "slowly going down the street in Stuttgart"
recursive_predict(image1_path, prompt, 1, 238, 6)

# for i in range(1, 99, 6):
image1_path = r"C:\workspace\cs231n\proj\data\titan_data\TEST\clip_582\images\%s_result.jpg"
prompt= "slowly going down the street in Tokyo"
recursive_predict(image1_path, prompt, 1, 99, 6)


# for i in range(1, 99, 6):
image1_path = (
    r"C:\workspace\cs231n\proj\data\titan_data\TEST\clip_537\images\%s_result.jpg"
)
prompt= "discovering Tokyo backlanes"
recursive_predict(image1_path, prompt, 1, 99, 6)


assert 1 == 2

for i in range(1, 99, 6):
    n = str(i)
    image1_path = (
        r"C:\workspace\cs231n\proj\data\titan_data\TEST\clip_537\images\%s_result.jpg"
        % n.zfill(3)
    )
    n = str(i + 6)
    image2_path = (
        r"C:\workspace\cs231n\proj\data\titan_data\TEST\clip_537\images\%s_result.jpg"
        % n.zfill(3)
    )
    print()
    assert os.path.exists(image1_path)
    image1 = Image.open(image1_path)
    assert os.path.exists(image2_path)
    image2 = Image.open(image2_path)
    # res6 = p.predict(
    #    image1_path=image1_path,
    #    prompt= str(i) + ". discovering Tokyo backlanes",
    # )

for i in range(1, 99, 6):
    n = str(i)
    image1_path = (
        r"C:\workspace\cs231n\proj\data\titan_data\TEST\clip_582\images\%s_result.jpg"
        % n.zfill(3)
    )
    n = str(i + 6)
    assert os.path.exists(image1_path)
    assert os.path.exists(image2_path)
    image2_path = (
        r"C:\workspace\cs231n\proj\data\titan_data\TEST\clip_582\images\%s_result.jpg"
        % n.zfill(3)
    )
    res6 = p.predict(
        image1_path=image1_path,
        prompt=str(i) + "_ walking down a Tokyo backlane",
    )


for i in range(1, 238, 6):
    n = str(i)
    image1_path = (
        r"C:\workspace\cs231n\proj\data\kitti\TEST\2011_09_26_drive_0106_sync\2011_09_26_rad\2011_09_26_drive_0106_sync_red_flying_cam_pedestrinas\image_03\data\%s_result.jpg"
        % n.zfill(3)
    )
    n = str(i + 6)
    image2_path = (
        r"C:\workspace\cs231n\proj\data\kitti\TEST\2011_09_26_drive_0106_sync\2011_09_26_rad\2011_09_26_drive_0106_sync_red_flying_cam_pedestrinas\image_03\data\%s_result.jpg"
        % n.zfill(3)
    )
    res6 = p.predict(
        image1_path=image1_path,
        image2_path=image2_path,
        prompt=str(i) + "_ slowly going down the street in Stuttgart",
    )

    print("t1:", t1 - t0)
    raise AttributeError("tokyo")


print("t1:", t1 - t0)
raise AttributeError("tokyo")

t0 = time.time()
image1_path = (
    r"C:\workspace\cs231n\proj\data\titan_data\TEST\clip_486\images\020_result.jpg"
)
image2_path = (
    r"C:\workspace\cs231n\proj\data\titan_data\TEST\clip_486\images\025_result.jpg"
)
res6 = p.predict(
    image1_path=image1_path,
    image2_path=image2_path,
    prompt="1, slowly going down a construction site in tokyo",
)
t0 = time.time()
image1_path = (
    r"C:\workspace\cs231n\proj\data\titan_data\TEST\clip_486\images\020_result.jpg"
)
image2_path = (
    r"C:\workspace\cs231n\proj\data\titan_data\TEST\clip_486\images\026_result.jpg"
)
res6 = p.predict(
    image1_path=image1_path,
    image2_path=image2_path,
    prompt="2, slowly going down a construction site in tokyo",
)

image1_path = (
    r"C:\workspace\cs231n\proj\data\titan_data\TEST\clip_486\images\026_result.jpg"
)
image2_path = (
    r"C:\workspace\cs231n\proj\data\titan_data\TEST\clip_486\images\032_result.jpg"
)
res6 = p.predict(
    image1_path=image1_path,
    image2_path=image2_path,
    prompt="3. slowly going down a construction site in tokyo",
)
t0 = time.time()
image1_path = (
    r"C:\workspace\cs231n\proj\data\titan_data\TEST\clip_486\images\032_result.jpg"
)
image2_path = (
    r"C:\workspace\cs231n\proj\data\titan_data\TEST\clip_486\images\038_result.jpg"
)
res6 = p.predict(
    image1_path=image1_path,
    image2_path=image2_path,
    prompt="4 slowly going down a construction site in tokyo",
)
raise AttributeError("tokyo")
#############################################################################
t0 = time.time()
image1_path = (
    r"C:\workspace\cs231n\proj\data\titan_data\TEST\clip_756\images\049_result.jpg"
)
image2_path = (
    r"C:\workspace\cs231n\proj\data\titan_data\TEST\clip_756\images\054_result.jpg"
)
res6 = p.predict(
    image1_path=image1_path,
    image2_path=image2_path,
    prompt="slowly going down the street in tokyo",
)
t1 = time.time()
print("t1:", t1 - t0)
raise AttributeError("tokyo")

t0 = time.time()
image1_path = r"C:\workspace\cs231n\proj\data\kitti\TEST\2011_09_26_drive_0106_sync\2011_09_26_rad\2011_09_26_drive_0106_sync_red_flying_cam_pedestrinas\image_03\data\097_result.jpg"
image2_path = r"C:\workspace\cs231n\proj\data\kitti\TEST\2011_09_26_drive_0106_sync\2011_09_26_rad\2011_09_26_drive_0106_sync_red_flying_cam_pedestrinas\image_03\data\103_result.jpg"
res6 = p.predict(
    image1_path=image1_path,
    image2_path=image2_path,
    prompt="slowly going down the street",
)
t1 = time.time()

# linear
# camera only
t0 = time.time()
image1_path = r"C:\workspace\cs231n\proj\data\kitti\TEST\2011_09_26_drive_0106_sync\2011_09_26_rad\2011_09_26_drive_0106_sync_red_flying_cam_pedestrinas\image_03\data\097_result.jpg"
image2_path = r"C:\workspace\cs231n\proj\data\kitti\TEST\2011_09_26_drive_0106_sync\2011_09_26_rad\2011_09_26_drive_0106_sync_red_flying_cam_pedestrinas\image_03\data\103_result.jpg"
res6 = p.predict(
    image1_path=image1_path,
    image2_path=image2_path,
    prompt="slowly going down the street",
)
t1 = time.time()
print("t1:", t1 - t0)

# overlap for recursice
t2 = time.time()
image1_path = r"C:\workspace\cs231n\proj\data\kitti\TEST\2011_09_26_drive_0106_sync\2011_09_26_rad\2011_09_26_drive_0106_sync_red_flying_cam_pedestrinas\image_03\data\103_result.jpg"
image2_path = r"C:\workspace\cs231n\proj\data\kitti\TEST\2011_09_26_drive_0106_sync\2011_09_26_rad\2011_09_26_drive_0106_sync_red_flying_cam_pedestrinas\image_03\data\109_result.jpg"
res7 = p.predict(
    image1_path=image1_path,
    image2_path=image2_path,
    prompt="slowly going down the street more",
)
t3 = time.time()
print("t3:", t3 - t2)

t0 = time.time()
image1_path = r"C:\workspace\cs231n\proj\data\kitti\TEST\2011_09_26_drive_0106_sync\2011_09_26_rad\2011_09_26_drive_0106_sync_red_flying_cam_pedestrinas\image_03\data\097_result.jpg"
image2_path = r"C:\workspace\cs231n\proj\data\kitti\TEST\2011_09_26_drive_0106_sync\2011_09_26_rad\2011_09_26_drive_0106_sync_red_flying_cam_pedestrinas\image_03\data\102_result.jpg"
res6 = p.predict(
    image1_path=image1_path,
    image2_path=image2_path,
    prompt="slowly going down the street",
)
t1 = time.time()
print("t1:", t1 - t0)

# overlap for recursice
t2 = time.time()
image1_path = r"C:\workspace\cs231n\proj\data\kitti\TEST\2011_09_26_drive_0106_sync\2011_09_26_rad\2011_09_26_drive_0106_sync_red_flying_cam_pedestrinas\image_03\data\102_result.jpg"
image2_path = r"C:\workspace\cs231n\proj\data\kitti\TEST\2011_09_26_drive_0106_sync\2011_09_26_rad\2011_09_26_drive_0106_sync_red_flying_cam_pedestrinas\image_03\data\107_result.jpg"
res7 = p.predict(
    image1_path=image1_path,
    image2_path=image2_path,
    prompt="slowly going down the street more",
)


t24 = time.time()
image1_path = r"C:\workspace\cs231n\proj\data\kitti\TEST\2011_09_26_drive_0104_sync_urban_2\2011_09_26\2011_09_26_drive_0104_sync\image_03\data\494_result.jpg"
image2_path = r"C:\workspace\cs231n\proj\data\kitti\TEST\2011_09_26_drive_0104_sync_urban_2\2011_09_26\2011_09_26_drive_0104_sync\image_03\data\499_result.jpg"
res23 = p.predict(
    image1_path=image1_path,
    image2_path=image2_path,
    prompt="slowly driving around the corner",
)
t23 = time.time()
print("t22 slowly driving around the corner:", t24 - t23)  # 36.447720527648926

image1_path = r"C:\workspace\cs231n\proj\data\kitti\TEST\2011_09_26_drive_0104_sync_urban_2\2011_09_26\2011_09_26_drive_0104_sync\image_03\data\499_result.jpg"
image2_path = r"C:\workspace\cs231n\proj\data\kitti\TEST\2011_09_26_drive_0104_sync_urban_2\2011_09_26\2011_09_26_drive_0104_sync\image_03\data\503_result.jpg"
res23 = p.predict(
    image1_path=image1_path,
    image2_path=image2_path,
    prompt="slowly driving around the corner more",
)
t23 = time.time()
print("t22 slowly driving around the corner:", t24 - t23)  # 36.447720527648926


t24 = time.time()
image1_path = r"C:\workspace\cs231n\proj\data\kitti\TEST\2011_09_26_drive_0117_sync_urban1\2011_09_26\2011_09_26_drive_0117_sync\image_03\data\318_result.jpg"
image2_path = r"C:\workspace\cs231n\proj\data\kitti\TEST\2011_09_26_drive_0117_sync_urban1\2011_09_26\2011_09_26_drive_0117_sync\image_03\data\323_result.jpg"
res23 = p.predict(
    image1_path=image1_path,
    image2_path=image2_path,
    prompt="slowly driving down in downtown",
)
t24 = time.time()
print("t22 slowly driving around the corner:", t24 - t23)  # 36.447720527648926

t23 = time.time()
image1_path = r"C:\workspace\cs231n\proj\data\kitti\TEST\2011_09_26_drive_0014_sync_follow\2011_09_26\2011_09_26_drive_0014_sync\image_03\data\210_result.jpg"
image2_path = r"C:\workspace\cs231n\proj\data\kitti\TEST\2011_09_26_drive_0014_sync_follow\2011_09_26\2011_09_26_drive_0014_sync\image_03\data\215_result.jpg"
res22 = p.predict(
    image1_path=image1_path,
    image2_path=image2_path,
    prompt="slowly driving on empty suburbian street, no cars",
)
t24 = time.time()
print(
    "slowly driving on empty suburbian street, no cars", t24 - t23
)  # 36.447720527648926


t25 = time.time()
image1_path = r"C:\workspace\cs231n\proj\data\kitti\TEST\2011_09_26_drive_0014_sync_follow\2011_09_26\2011_09_26_drive_0014_sync\image_03\data\216_result.jpg"
image2_path = r"C:\workspace\cs231n\proj\data\kitti\TEST\2011_09_26_drive_0014_sync_follow\2011_09_26\2011_09_26_drive_0014_sync\image_03\data\221_result.jpg"
res23 = p.predict(
    image1_path=image1_path,
    image2_path=image2_path,
    prompt="more slowly driving on empty suburbian street, no cars",
)
t26 = time.time()
print(
    "tmore slowly driving on empty suburbian street, no cars:", t26 - t25
)  # 36.53929042816162

t27 = time.time()
image1_path = r"C:\workspace\cs231n\proj\data\kitti\TEST\2011_09_26_drive_0014_sync_follow\2011_09_26\2011_09_26_drive_0014_sync\image_03\data\210_result.jpg"
image2_path = r"C:\workspace\cs231n\proj\data\kitti\TEST\2011_09_26_drive_0014_sync_follow\2011_09_26\2011_09_26_drive_0014_sync\image_03\data\221_result.jpg"
res24 = p.predict(
    image1_path=image1_path,
    image2_path=image2_path,
    prompt="slowly driving the suburbian street slightly faster, empty street",
)
t28 = time.time()


image1_path = os.path.join(img_folder, f, "seq/Ped_260.jpg")
image1_path = os.path.join(
    r"C:\workspace\cs231n\proj\data\kitti\TEST\2011_09_26_drive_0106_sync\2011_09_26_rad\2011_09_26_drive_0106_sync_red_flying_cam_pedestrinas\image_03\data\215_result.jpg"
)
image2_path = os.path.join(
    r"C:\workspace\cs231n\proj\data\kitti\TEST\2011_09_26_drive_0106_sync\2011_09_26_rad\2011_09_26_drive_0106_sync_red_flying_cam_pedestrinas\image_03\data\221_result.jpg"
)
res6 = p.predict(
    image1_path=image1_path,
    image2_path=image2_path,
    prompt="people walk by on a street, no wind",
)
res7 = p.predict(
    image1_path=image1_path, image2_path=image2_path, prompt="an empty road"
)
res8 = p.predict(
    image1_path=image1_path,
    image2_path=image2_path,
    prompt="remove all people from the street, keep camera still",
)


# The prompt like rotating view will make the corresponding camera motion.
t4 = time.time()
image1_path = r"C:\workspace\cs231n\proj\data\kitti\TEST\2011_09_26_drive_0106_sync\2011_09_26_rad\2011_09_26_drive_0106_sync_red_flying_cam_pedestrinas\image_03\data\102_result.jpg"
image2_path = r"C:\workspace\cs231n\proj\data\kitti\TEST\2011_09_26_drive_0106_sync\2011_09_26_rad\2011_09_26_drive_0106_sync_red_flying_cam_pedestrinas\image_03\data\107_result.jpg"
res7 = p.predict(
    image1_path=image1_path,
    image2_path=image2_path,
    prompt="slowly going down the street with a rotating view to the left",
)
t5 = time.time()
print("t4:", t5 - t4)
t6 = time.time()
image1_path = r"C:\workspace\cs231n\proj\data\kitti\TEST\image_03\data_strassenbahn\024_result.jpg"
image2_path = r"C:\workspace\cs231n\proj\data\kitti\TEST\image_03\data_strassenbahn\030_result.jpg"
res8 = p.predict(
    image1_path=image1_path, image2_path=image2_path, prompt="train approaches"
)
t7 = time.time()
print("t7 train approaches:", t6 - t7)


# people walk in camera direction
t8 = time.time()
image1_path = r"C:\workspace\cs231n\proj\data\kitti\TEST\2011_09_26_drive_0091_sync_pede_city\2011_09_26\2011_09_26_drive_0091_sync\image_03\data\012_result.jpg"
image2_path = r"C:\workspace\cs231n\proj\data\kitti\TEST\2011_09_26_drive_0091_sync_pede_city\2011_09_26\2011_09_26_drive_0091_sync\image_03\data\018_result.jpg"
res9 = p.predict(
    image1_path=image1_path,
    image2_path=image2_path,
    prompt="people slowly going down the street",
)  # TOD
t9 = time.time()
print("t9: people slowly going down the street", t9 - t8)

# people bikes pepindc
t10 = time.time()
image1_path = r"C:\workspace\cs231n\proj\data\kitti\TEST\2011_09_26_drive_0106_sync\2011_09_26_rad\2011_09_26_drive_0106_sync_red_flying_cam_pedestrinas\image_03\data\026_result.jpg"
image2_path = r"C:\workspace\cs231n\proj\data\kitti\TEST\2011_09_26_drive_0106_sync\2011_09_26_rad\2011_09_26_drive_0106_sync_red_flying_cam_pedestrinas\image_03\data\031_result.jpg"
res10 = p.predict(
    image1_path=image1_path,
    image2_path=image2_path,
    prompt="kids with bikes standing next to the street, keep camera still, dont add objects",
)
t11 = time.time()
print(
    "t11: kids with bikes standing still next to the road, no camera movement",
    t11 - t10,
)

# car drives in front off camera
t12 = time.time()
image1_path = r"C:\workspace\cs231n\proj\data\kitti\TEST\2011_09_26_drive_0057_sync_redcar\2011_09_26\2011_09_26_drive_0057_sync\image_03\data\292_result.jpg"
image2_path = r"C:\workspace\cs231n\proj\data\kitti\TEST\2011_09_26_drive_0057_sync_redcar\2011_09_26\2011_09_26_drive_0057_sync\image_03\data\298_result.jpg"
res10 = p.predict(
    image1_path=image1_path,
    image2_path=image2_path,
    prompt="waiting at the traffic light",
)
t13 = time.time()
print("t12: red car drives off", t13 - t12)
#
#
t14 = time.time()
image1_path = r"C:\workspace\cs231n\proj\data\kitti\TEST\2011_09_26_drive_0057_sync_redcar\2011_09_26\2011_09_26_drive_0057_sync\image_03\data\292_result.jpg"
image2_path = r"C:\workspace\cs231n\proj\data\kitti\TEST\2011_09_26_drive_0057_sync_redcar\2011_09_26\2011_09_26_drive_0057_sync\image_03\data\298_result.jpg"
res10 = p.predict(
    image1_path=image1_path,
    image2_path=image2_path,
    prompt="remove all non red cars from the street",
)
t15 = time.time()
print("t15: remove all cars from the street", t15 - t14)

t16 = time.time()
image1_path = r"C:\workspace\cs231n\proj\data\kitti\TEST\2011_09_26_drive_0057_sync_redcar\2011_09_26\2011_09_26_drive_0057_sync\image_03\data\297_result.jpg"
image2_path = r"C:\workspace\cs231n\proj\data\kitti\TEST\2011_09_26_drive_0057_sync_redcar\2011_09_26\2011_09_26_drive_0057_sync\image_03\data\297_result.jpg"
res7 = p.predict(
    image1_path=image1_path,
    image2_path=image2_path,
    prompt="camera moving up to the sky",
)
t17 = time.time()
print("t17:", t17 - t16)

# people walk in camera direction 056_result.jpg
t17 = time.time()
image1_path = r"C:\workspace\cs231n\proj\data\kitti\TEST\2011_09_26_drive_0060_sync_bike_static_cam\2011_09_26\2011_09_26_drive_0060_sync\image_03\data\050_result.jpg"
image2_path = r"C:\workspace\cs231n\proj\data\kitti\TEST\2011_09_26_drive_0060_sync_bike_static_cam\2011_09_26\2011_09_26_drive_0060_sync\image_03\data\056_result.jpg"
res9 = p.predict(
    image1_path=image1_path, image2_path=image2_path, prompt="an empty street, no cars"
)  # TOD0
t18 = time.time()
print("t18:", t18 - t17)

# speed up 2x
t19 = time.time()
image1_path = r"C:\workspace\cs231n\proj\data\kitti\TEST\2011_09_26_drive_0106_sync\2011_09_26_rad\2011_09_26_drive_0106_sync_red_flying_cam_pedestrinas\image_03\data\097_result.jpg"
image2_path = r"C:\workspace\cs231n\proj\data\kitti\TEST\2011_09_26_drive_0106_sync\2011_09_26_rad\2011_09_26_drive_0106_sync_red_flying_cam_pedestrinas\image_03\data\107_result.jpg"
res7 = p.predict(
    image1_path=image1_path,
    image2_path=image2_path,
    prompt="going down the street slightly faster",
)
t20 = time.time()
print("t20 going down the street slightly faster:", t20 - t19)

# slowed down
t19 = time.time()
image1_path = r"C:\workspace\cs231n\proj\data\kitti\TEST\2011_09_26_drive_0106_sync\2011_09_26_rad\2011_09_26_drive_0106_sync_red_flying_cam_pedestrinas\image_03\data\097_result.jpg"
image2_path = r"C:\workspace\cs231n\proj\data\kitti\TEST\2011_09_26_drive_0106_sync\2011_09_26_rad\2011_09_26_drive_0106_sync_red_flying_cam_pedestrinas\image_03\data\100_result.jpg"
res7 = p.predict(
    image1_path=image1_path,
    image2_path=image2_path,
    prompt="going down the street slightly slower",
)
t20 = time.time()
print("t20 going down the street slightly faster:", t20 - t19)

t21 = time.time()
image1_path = r"C:\workspace\cs231n\proj\data\kitti\TEST\2011_09_26_drive_0106_sync\2011_09_26_rad\2011_09_26_drive_0106_sync_red_flying_cam_pedestrinas\image_03\data\097_result.jpg"
image2_path = r"C:\workspace\cs231n\proj\data\kitti\TEST\2011_09_26_drive_0106_sync\2011_09_26_rad\2011_09_26_drive_0106_sync_red_flying_cam_pedestrinas\image_03\data\107_result.jpg"
res7 = p.predict(
    image1_path=image1_path,
    image2_path=image2_path,
    prompt="going down the street slightly faster",
)
t22 = time.time()
print("t20 going down the street slightly faster:", t22 - t21)


print(
    "t20 going down the street slightly faster:", t28 - t27
)  # 38.675254583358765 36.53929042816162  36.447720527648926

t23 = time.time()
image1_path = r"C:\workspace\cs231n\proj\data\kitti\TEST\2011_09_26_drive_0014_sync_follow\2011_09_26\2011_09_26_drive_0014_sync\image_03\data\226_result.jpg"
image2_path = r"C:\workspace\cs231n\proj\data\kitti\TEST\2011_09_26_drive_0014_sync_follow\2011_09_26\2011_09_26_drive_0014_sync\image_03\data\238_result.jpg"
res22 = p.predict(
    image1_path=image1_path,
    image2_path=image2_path,
    prompt="slowly going down the street while its rainig hard",
)
t24 = time.time()
print("t20 going down the street slightly faster:", t24 - t23)  # 36.447720527648926

t23 = time.time()
res22 = p.predict(
    image1_path=image1_path,
    image2_path=image2_path,
    prompt="slowly going down the street, add clouds to the sky",
)
t24 = time.time()
print("t20 going down the street slightly faster:", t24 - t23)  # 36.447720527648926

avg_time = (t28 - t0) / 29
print("avg_time", avg_time)

# C:\workspace\cs231n\proj\DynamiCrafter\output
# ffmpeg.exe -i videoToCompare.mp4 -i originalVideo.mp4 -lavfi ssim=stats_file=ssim_logfile.txt -f null -
# ffmpeg.exe -i videoToCompare.mp4 -i originalVideo.mp4 -lavfi psnr=stats_file=psnr_logfile.txt -f null -
# os.system("ffmpg")
# ffmpeg -r 1/5 -start_number 261 -i "C:\workspace\cs231n\proj\data\kitti\TEST\selected\2011_09_26_drive_0091_sync\seq\Ped%d.jpg" -c:v libx264 -r 30 -pix_fmt yuv420p out.mp4
# ffmpeg -i input.lowfps.hevc -filter:v "minterpolate='fps=8'" output.120fps.hevc
# ffmpeg -i input.hevc -filter "minterpolate='mi_mode=mci:mc_mode=aobmc:vsbmc=1'" output.hevc.
# The filter's documentation contains the description of the available parameters and their values. –
# ffmpeg -r 1/5 -start_number 0 -i C:\myimages\img%03d.png -c:v libx264 -r 30 -pix_fmt yuv420p out.mp4

# ffmpeg -i input1.ts -i input2.ts -i input3.ts -filter_complex "concat=n=3:v=1:a=0" -vn -y output.ts
# ffmpeg -i "C:\workspace\cs231n\proj\data\kitti\TEST\selected\2011_09_26_drive_0091_sync\seq\Ped%d.jpg"-filter:v fps=8  out.mp4

# ffmpeg.exe -i videoToCompare.mp4 -i originalVideo.mp4 -lavfi psnr=stats_file=psnr_logfile.txt -f null -
# ffmpeg.exe -i videoToCompare.mp4 -i originalVideo.mp4 -lavfi ssim=stats_file=ssim_logfile.txt -f null -
# [Parsed_psnr_0 @ 054271e0] PSNR y:11.261841 u:28.780037 v:29.014721 average:12.985472 min:12.693955 max:14.083181

# PSNR y:16.327098 u:31.281433 v:32.004562 average:18.024407 min:16.660268 max:42.886199
# PSNR y:inf u:inf v:inf average:inf min:inf max:inf
# log file will contain a frame-wise list of the MSE and the PSNR for the Luma and Chroma planes

# SSIM Y:0.221608 (1.088018) U:0.737887 (5.815110) V:0.796947 (6.923913) All:0.403545 (2.244220)
# SSIM Y:1.000000 (inf) U:1.000000 (inf) V:1.000000 (inf) All:1.000000 (inf)  match
# ffmpeg -start_number 24 -i "C:\workspace\cs231n\proj\data\kitti\TEST\image_03\data_strassenbahn\seq1\%d_result.jpg" -filter:v fps=10  "C:\workspace\cs231n\proj\data\kitti\TEST\image_03\data_strassenbahn\seq1\out10fps.mp4"
# 6 -> 16 2.6  = 27 fps
# -vf "minterpolate=fps=25:mi_mode=mci:mc_mode=aobmc:me_mode=bidir:vsbmc=1"
# ffmpeg -i  "C:\workspace\cs231n\proj\data\kitti\TEST\image_03\data_strassenbahn\seq1\out10fps.mp4" -vf  "minterpolate=fps=26:mi_mode=mci:mc_mode=aobmc:me_mode=bidir:vsbmc=1"  "C:\workspace\cs231n\proj\data\kitti\TEST\image_03\data_strassenbahn\seq1\out26fps.mp4"
# ffmpeg -start_number 24 -i "C:\workspace\cs231n\proj\data\kitti\TEST\image_03\data_strassenbahn\seq1\%d_result.jpg" -vf minterpolate=fps=26:mi_mode=mci:me_mode=bidir:mc_mode=obmc:me=ds:vsbmc=1 "C:\workspace\cs231n\proj\data\kitti\TEST\image_03\data_strassenbahn\seq1\out26fps.mp4"
# 512 320
# ffmpeg.exe -i "C:\workspace\cs231n\proj\data\kitti\TEST\image_03\data_strassenbahn\seq1\out26fps.mp4" -i   -lavfi psnr=stats_file=psnr_logfile.txt -f null -
# If your pixels are represented using 8 bits per sample, the maximum possible pixel value of the image is 255. 20*log10(255) = 48 dB the mean squared error (MSE) of noise is not considered yet.
#  The typical compression ratio of jpeg is no less than 7. In that case the MSE is around 0.224, and the corresponding PSNR is 54 dB. So you probably will not get the PSNR as high as 63 dB.
# mediainfo --Output="Video;%FrameCount%" input.avi
# PSNR y:14.828602 u:35.186791 v:36.502819 average:16.572168 min:15.438353 max:20.310102
# SSIM Y:0.401351 (2.228279) U:0.864741 (8.688329) V:0.891021 (9.626574) All:0.560194 (3.567393)
# ffmpeg -i input.mp4 -filter_complex "format=gbrp,tblend=all_mode=difference" output.mp4
# ffmpeg -i  "C:\workspace\cs231n\proj\data\kitti\TEST\image_03\data_strassenbahn\seq1\out10fps.mp4"  -i c:\workspace\cs231n\proj\DynamiCrafter\output\experiments\rec\train_approaches.mp4  -filter_complex "blend=all_mode=difference" -c:v libx265 -crf 18 -c:a copy c:\workspace\cs231n\proj\DynamiCrafter\output\experiments\rec\difference.mp4
# ffmpeg -y -i "%~1" -i "%~2" -filter_complex "[1:v]format=yuva444p,lut=c3=128,negate[video2withAlpha],[0:v][video2withAlpha]overlay[out]" -map [out] "%~n1-output%~x1"
# ffmpeg.exe -i videoToCompare.mp4 -i originalVideo.mp4 -lavfi libvmaf="model_path=vmaf_v0.6.1.pkl":log_path=vmaf_logfile.txt -f null -


# ffmpeg.exe -i videoToCompare.mp4 -i originalVideo.mp4 -lavfi libvmaf="model_path=vmaf_v0.6.1.pkl":log_path=vmaf_logfile.txt -f null -
# ffmpeg -i "c:\workspace\cs231n\proj\DynamiCrafter\output\experiments\rec\suburb_concatenated.mp4"  -vf "format=rgb24,histogram=display_mode=overlay" "C:\workspace\cs231n\proj\DynamiCrafter\output\experiments\histo.mp4"

# C:\workspace\cs231n\proj\data\kitti\TEST\2011_09_26_drive_0106_sync\2011_09_26_rad\2011_09_26_drive_0106_sync_red_flying_cam_pedestrinas\image_03\data\seq1
# ffmpeg -start_number 97 -i "C:\workspace\cs231n\proj\data\kitti\TEST\2011_09_26_drive_0106_sync\2011_09_26_rad\2011_09_26_drive_0106_sync_red_flying_cam_pedestrinas\image_03\data\seq1\%d_result.jpg" -filter:v fps=10  "C:\workspace\cs231n\proj\data\kitti\TEST\2011_09_26_drive_0106_sync\2011_09_26_rad\2011_09_26_drive_0106_sync_red_flying_cam_pedestrinas\image_03\data\seq1\out10fps.mp4"
# ffmpeg -i  "C:\workspace\cs231n\proj\data\kitti\TEST\2011_09_26_drive_0106_sync\2011_09_26_rad\2011_09_26_drive_0106_sync_red_flying_cam_pedestrinas\image_03\data\seq1\out10fps.mp4" -vf  "minterpolate=fps=26:mi_mode=mci:mc_mode=aobmc:me_mode=bidir:vsbmc=1" "C:\workspace\cs231n\proj\data\kitti\TEST\2011_09_26_drive_0106_sync\2011_09_26_rad\2011_09_26_drive_0106_sync_red_flying_cam_pedestrinas\image_03\data\seq1\out25fps.mp4"
# ffmpeg -i  "C:\workspace\cs231n\proj\data\kitti\TEST\2011_09_26_drive_0106_sync\2011_09_26_rad\2011_09_26_drive_0106_sync_red_flying_cam_pedestrinas\image_03\data\seq1\out25fps.mp4" -i  "C:\workspace\cs231n\proj\DynamiCrafter\output\experiments\rec\city_concatenated.mp4"  -filter_complex "format=gbrp,tblend=all_mode=difference" "C:\workspace\cs231n\proj\DynamiCrafter\output\experiments\rec\city_diff.mp4"
# ffmpeg.exe -i "C:\workspace\cs231n\proj\data\kitti\TEST\2011_09_26_drive_0106_sync\2011_09_26_rad\2011_09_26_drive_0106_sync_red_flying_cam_pedestrinas\image_03\data\seq1\out25fps.mp4" -i  "C:\workspace\cs231n\proj\DynamiCrafter\output\experiments\rec\city_concatenated.mp4" # -lavfi ssim=stats_file=ssim_logfile.txt -f null -
# ffmpeg.exe -i "C:\workspace\cs231n\proj\data\kitti\TEST\2011_09_26_drive_0106_sync\2011_09_26_rad\2011_09_26_drive_0106_sync_red_flying_cam_pedestrinas\image_03\data\seq1\out25fps.mp4" -i  "C:\workspace\cs231n\proj\DynamiCrafter\output\experiments\rec\city_concatenated.mp4"  -lavfi psnr=stats_file=psnr_logfile.txt -f null -traion

# C:\workspace\cs231n\proj\data\kitti\TEST\2011_09_26_drive_0014_sync_follow\2011_09_26\2011_09_26_drive_0014_sync\image_03\data\seq
# ffmpeg -start_number 210 -i "C:\workspace\cs231n\proj\data\kitti\TEST\2011_09_26_drive_0014_sync_follow\2011_09_26\2011_09_26_drive_0014_sync\image_03\data\seq\%d_result.jpg" -pix_fmt yuv420p  -filter:v fps=10  "C:\workspace\cs231n\proj\data\kitti\TEST\2011_09_26_drive_0014_sync_follow\2011_09_26\2011_09_26_drive_0014_sync\image_03\data\seq\out10fps.mp4"
# ffmpeg -i  "C:\workspace\cs231n\proj\data\kitti\TEST\2011_09_26_drive_0014_sync_follow\2011_09_26\2011_09_26_drive_0014_sync\image_03\data\seq\out10fps.mp4" -vf  "minterpolate=fps=26:mi_mode=mci:mc_mode=aobmc:me_mode=bidir:vsbmc=1" "C:\workspace\cs231n\proj\data\kitti\TEST\2011_09_26_drive_0014_sync_follow\2011_09_26\2011_09_26_drive_0014_sync\image_03\data\seq\out26fps.mp4"
# ffmpeg -i "c:\workspace\cs231n\proj\DynamiCrafter\output\experiments\rec\suburb_concatenated.mp4"  -vf "format=rgb24,histogram=display_mode=overlay" "C:\workspace\cs231n\proj\DynamiCrafter\output\experiments\histo.mp4"
# ffmpeg -i C:\workspace\cs231n\proj\DynamiCrafter\output\experiments\rec\slowly_going_down_the_suburbian_street.mp4 -i  C:\workspace\cs231n\proj\DynamiCrafter\output\experiments\rec\slowly_going_down_the_suburbian_street_m.mp4 -sar 1:1 -filter_complex "concat=n=2:v=1:a=0" -vn -y C:\workspace\cs231n\proj\DynamiCrafter\output\experiments\rec\suburb_concatenated.mp4
# ffmpeg -i  "C:\workspace\cs231n\proj\data\kitti\TEST\image_03\data_strassenbahn\seq1\out10fps.mp4" -vf  "minterpolate=fps=27:mi_mode=mci:mc_mode=aobmc:me_mode=bidir:vsbmc=1"  "C:\workspace\cs231n\proj\data\kitti\TEST\image_03\data_strassenbahn\seq1\out27fps.mp4"
# ffmpeg -i  "C:\workspace\cs231n\proj\data\kitti\TEST\2011_09_26_drive_0014_sync_follow\2011_09_26\2011_09_26_drive_0014_sync\image_03\data\seq\out10fps.mp4" -vf  "minterpolate=fps=27:mi_mode=mci:mc_mode=aobmc:me_mode=bidir:vsbmc=1"  "C:\workspace\cs231n\proj\data\kitti\TEST\2011_09_26_drive_0014_sync_follow\2011_09_26\2011_09_26_drive_0014_sync\image_03\data\seq\out27fps.mp4"
# ffmpeg -i  "C:\workspace\cs231n\proj\data\kitti\TEST\image_03\data_strassenbahn\seq1\out26fps.mp4"  -i c:\workspace\cs231n\proj\DynamiCrafter\output\experiments\rec\train_approaches.mp4  -filter_complex "blend=all_mode=difference" -c:v libx265 -crf 18 -c:a copy c:\workspace\cs231n\proj\DynamiCrafter\output\experiments\rec\difference_t27fps.mp4
# First input link top parameters (size 512x320, SAR 1:1) do not match the corresponding second input link bottom parameters (512x320, SAR 0:1
# ffmpeg -i  C:\workspace\cs231n\proj\data\kitti\TEST\2011_09_26_drive_0014_sync_follow\2011_09_26\2011_09_26_drive_0014_sync\image_03\data\seq\out26fps.mp4 -i c:\workspace\cs231n\proj\DynamiCrafter\output\experiments\rec\suburb_concatenated.mp4  -filter_complex "format=gbrp,blend=all_mode=difference" -c:v libx265 -crf 18 -c:a copy c:\workspace\cs231n\proj\DynamiCrafter\output\experiments\rec\difference_t26fps.mp4
# ffmpeg.exe -i  C:\workspace\cs231n\proj\data\kitti\TEST\2011_09_26_drive_0014_sync_follow\2011_09_26\2011_09_26_drive_0014_sync\image_03\data\seq\out26fps.mp4 -i c:\workspace\cs231n\proj\DynamiCrafter\output\experiments\rec\suburb_concatenated.mp4  -lavfi psnr=stats_file=psnr_logfile.txt -f null -
