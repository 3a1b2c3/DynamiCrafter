import os, time
from cog import BasePredictor, Input, Path
import sys

sys.path.append(r"C:\workspace\cs231n\proj\DynamiCrafter")
os.chdir(r"C:\workspace\cs231n\proj\DynamiCrafter")
ckpt = r"C:\workspace\cs231n\proj\DynamiCrafter\checkpoints\dynamicrafter_256_v1\dynamicrafter_512_interp_v1.ckpt"
# C:\workspace\cs231n\proj\DynamiCrafter\configs\training_512_v1.0\config_interp.yaml

from PIL import Image
import numpy as np
import torch
from scripts.gradio.i2v_test_application import Image2Video


class Predictor(BasePredictor):
    def setup(self) -> None:
        directory = r"C:\workspace\cs231n\proj\DynamiCrafter\output"
        if not os.path.exists(directory):
            os.mkdir(directory)
        self.image2video = Image2Video(
            r"C:\workspace\cs231n\proj\DynamiCrafter\output", resolution="320_512"
        )

    def predict(
        self,
        image1_path: Path = Input(description="Input Image 1"),
        image2_path: Path = Input(description="Input Image 2"),
        prompt: str = Input(default="a smiling girl"),
        steps: int = Input(default=50),
        cfg_scale: float = Input(default=7.5),
        eta: float = Input(default=1.0),
        fs: int = Input(default=5),
        seed: int = Input(default=12306),
    ) -> Path:
        image1 = Image.open(image1_path)
        if image1.mode == "RGBA":
            image1 = image1.convert("RGB")
        image2 = Image.open(image2_path)
        if image2.mode == "RGBA":
            image2 = image2.convert("RGB")
        image1_np = np.array(image1)
        image2_np = np.array(image2)
        i2v_output_video = self.image2video.get_image(
            image=image1_np,
            prompt=prompt,
            steps=steps,
            cfg_scale=cfg_scale,
            eta=eta,
            fs=fs,
            seed=seed,
            image2=image2_np,
        )
        print("_____________i2v_output_video", i2v_output_video)
        return i2v_output_video


p = Predictor()
p.setup()
img_folder = r"C:\workspace\cs231n\proj\data\kitti\selected"
img_folder_kitti = r"C:\workspace\cs231n\proj\data\kitti"
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
# linear
# camera only
t0 = time.time()
image1_path = r"C:\workspace\cs231n\proj\data\kitti\2011_09_26_drive_0106_sync\2011_09_26_rad\2011_09_26_drive_0106_sync_red_flying_cam_pedestrinas\image_03\data\0000000097_result.jpg"
image2_path = r"C:\workspace\cs231n\proj\data\kitti\2011_09_26_drive_0106_sync\2011_09_26_rad\2011_09_26_drive_0106_sync_red_flying_cam_pedestrinas\image_03\data\0000000102_result.jpg"
res6 = p.predict(
    image1_path=image1_path,
    image2_path=image2_path,
    prompt="slowly going down the street",
)
t1 = time.time()
print("t1:", t1 - t0)

# overlap for recursice
t2 = time.time()
image1_path = r"C:\workspace\cs231n\proj\data\kitti\2011_09_26_drive_0106_sync\2011_09_26_rad\2011_09_26_drive_0106_sync_red_flying_cam_pedestrinas\image_03\data\0000000102_result.jpg"
image2_path = r"C:\workspace\cs231n\proj\data\kitti\2011_09_26_drive_0106_sync\2011_09_26_rad\2011_09_26_drive_0106_sync_red_flying_cam_pedestrinas\image_03\data\0000000107_result.jpg"
res7 = p.predict(
    image1_path=image1_path,
    image2_path=image2_path,
    prompt="slowly going down the street more",
)
t3 = time.time()
print("t3:", t3 - t2)
# The prompt like rotating view will make the corresponding camera motion.
t4 = time.time()
image1_path = r"C:\workspace\cs231n\proj\data\kitti\2011_09_26_drive_0106_sync\2011_09_26_rad\2011_09_26_drive_0106_sync_red_flying_cam_pedestrinas\image_03\data\0000000102_result.jpg"
image2_path = r"C:\workspace\cs231n\proj\data\kitti\2011_09_26_drive_0106_sync\2011_09_26_rad\2011_09_26_drive_0106_sync_red_flying_cam_pedestrinas\image_03\data\0000000107_result.jpg"
res7 = p.predict(
    image1_path=image1_path,
    image2_path=image2_path,
    prompt="slowly going down the street with a rotating view to the left",
)
t5 = time.time()
print("t4:", t5 - t4)
# in camera direction C:\workspace\cs231n\proj\data\kitti\image_03\data_strassenbahn\
t6 = time.time()
image1_path = r"C:\workspace\cs231n\proj\data\kitti\image_03\data_strassenbahn\0000000024_result.jpg"
image2_path = r"C:\workspace\cs231n\proj\data\kitti\image_03\data_strassenbahn\0000000030_result.jpg"
res8 = p.predict(
    image1_path=image1_path, image2_path=image2_path, prompt="train approaches"
)
t7 = time.time()
print("t7 train approaches:", t6 - t7)


# people walk in camera direction
t8 = time.time()
image1_path = r"C:\workspace\cs231n\proj\data\kitti\2011_09_26_drive_0091_sync_pede_city\2011_09_26\2011_09_26_drive_0091_sync\image_03\data\0000000012_result.jpg"
image2_path = r"C:\workspace\cs231n\proj\data\kitti\2011_09_26_drive_0091_sync_pede_city\2011_09_26\2011_09_26_drive_0091_sync\image_03\data\0000000018_result.jpg"
res9 = p.predict(
    image1_path=image1_path,
    image2_path=image2_path,
    prompt="people slowly going down the street",
)  # TOD
t9 = time.time()
print("t9: people slowly going down the street", t9 - t8)

# people bikes pepindc
t10 = time.time()
image1_path = r"C:\workspace\cs231n\proj\data\kitti\2011_09_26_drive_0106_sync\2011_09_26_rad\2011_09_26_drive_0106_sync_red_flying_cam_pedestrinas\image_03\data\0000000026_result.jpg"
image2_path = r"C:\workspace\cs231n\proj\data\kitti\2011_09_26_drive_0106_sync\2011_09_26_rad\2011_09_26_drive_0106_sync_red_flying_cam_pedestrinas\image_03\data\0000000031_result.jpg"
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
image1_path = r"C:\workspace\cs231n\proj\data\kitti\2011_09_26_drive_0057_sync_redcar\2011_09_26\2011_09_26_drive_0057_sync\image_03\data\0000000292_result.jpg"
image2_path = r"C:\workspace\cs231n\proj\data\kitti\2011_09_26_drive_0057_sync_redcar\2011_09_26\2011_09_26_drive_0057_sync\image_03\data\0000000297_result.jpg"
res10 = p.predict(
    image1_path=image1_path, image2_path=image2_path, prompt="red car drives off"
)
t13 = time.time()
print("t12: red car drives off", t13 - t12)
#
#
t14 = time.time()
image1_path = r"C:\workspace\cs231n\proj\data\kitti\2011_09_26_drive_0057_sync_redcar\2011_09_26\2011_09_26_drive_0057_sync\image_03\data\0000000292_result.jpg"
image2_path = r"C:\workspace\cs231n\proj\data\kitti\2011_09_26_drive_0057_sync_redcar\2011_09_26\2011_09_26_drive_0057_sync\image_03\data\0000000297_result.jpg"
res10 = p.predict(
    image1_path=image1_path,
    image2_path=image2_path,
    prompt="remove all cars from the street",
)
t15 = time.time()
print("t15: remove all cars from the street", t15 - t14)

t16 = time.time()
image1_path = r"C:\workspace\cs231n\proj\data\kitti\2011_09_26_drive_0057_sync_redcar\2011_09_26\2011_09_26_drive_0057_sync\image_03\data\0000000297_result.jpg"
image2_path = r"C:\workspace\cs231n\proj\data\kitti\2011_09_26_drive_0057_sync_redcar\2011_09_26\2011_09_26_drive_0057_sync\image_03\data\0000000297_result.jpg"
res7 = p.predict(
    image1_path=image1_path,
    image2_path=image2_path,
    prompt="camera moving up to the sky",
)
t17 = time.time()
print("t17:", t17 - t16)

# people walk in camera direction 0000000056_result.jpg
t17 = time.time()
image1_path = r"C:\workspace\cs231n\proj\data\kitti\2011_09_26_drive_0060_sync_bike_static_cam\2011_09_26\2011_09_26_drive_0060_sync\image_03\data\0000000050_result.jpg"
image2_path = r"C:\workspace\cs231n\proj\data\kitti\2011_09_26_drive_0060_sync_bike_static_cam\2011_09_26\2011_09_26_drive_0060_sync\image_03\data\0000000056_result.jpg"
res9 = p.predict(
    image1_path=image1_path,
    image2_path=image2_path,
    prompt="people crossing an empty street, no cars",
)  # TOD0
t18 = time.time()
print("t18:", t18 - t17)

# speed up 2x
t19 = time.time()
image1_path = r"C:\workspace\cs231n\proj\data\kitti\2011_09_26_drive_0106_sync\2011_09_26_rad\2011_09_26_drive_0106_sync_red_flying_cam_pedestrinas\image_03\data\0000000097_result.jpg"
image2_path = r"C:\workspace\cs231n\proj\data\kitti\2011_09_26_drive_0106_sync\2011_09_26_rad\2011_09_26_drive_0106_sync_red_flying_cam_pedestrinas\image_03\data\0000000107_result.jpg"
res7 = p.predict(
    image1_path=image1_path,
    image2_path=image2_path,
    prompt="going down the street slightly faster",
)
t20 = time.time()
print("t20 going down the street slightly faster:", t20 - t19)

t21 = time.time()
image1_path = r"C:\workspace\cs231n\proj\data\kitti\2011_09_26_drive_0106_sync\2011_09_26_rad\2011_09_26_drive_0106_sync_red_flying_cam_pedestrinas\image_03\data\0000000097_result.jpg"
image2_path = r"C:\workspace\cs231n\proj\data\kitti\2011_09_26_drive_0106_sync\2011_09_26_rad\2011_09_26_drive_0106_sync_red_flying_cam_pedestrinas\image_03\data\0000000107_result.jpg"
res7 = p.predict(
    image1_path=image1_path,
    image2_path=image2_path,
    prompt="going down the street slightly faster",
)
t22 = time.time()
print("t20 going down the street slightly faster:", t22 - t21)

t23 = time.time()
image1_path = r"C:\workspace\cs231n\proj\data\kitti\2011_09_26_drive_0014_sync_follow\2011_09_26\2011_09_26_drive_0014_sync\image_03\data\0000000233_result.jpg"
image2_path = r"C:\workspace\cs231n\proj\data\kitti\2011_09_26_drive_0014_sync_follow\2011_09_26\2011_09_26_drive_0014_sync\image_03\data\0000000238_result.jpg"
res22 = p.predict(
    image1_path=image1_path,
    image2_path=image2_path,
    prompt="slowly going down the suburbian street",
)
t24 = time.time()
print("t20 going down the street slightly faster:", t24 - t23)
t25 = time.time()
image1_path = r"C:\workspace\cs231n\proj\data\kitti\2011_09_26_drive_0014_sync_follow\2011_09_26\2011_09_26_drive_0014_sync\image_03\data\0000000238_result.jpg"
image2_path = r"C:\workspace\cs231n\proj\data\kitti\2011_09_26_drive_0014_sync_follow\2011_09_26\2011_09_26_drive_0014_sync\image_03\data\0000000243_result.jpg"
res23 = p.predict(
    image1_path=image1_path,
    image2_path=image2_path,
    prompt="slowly going down the suburbian street more",
)
t26 = time.time()

print("t20 going down the street slightly faster:", t26 - t25)

t27 = time.time()
image1_path = r"C:\workspace\cs231n\proj\data\kitti\2011_09_26_drive_0014_sync_follow\2011_09_26\2011_09_26_drive_0014_sync\image_03\data\0000000233_result.jpg"
image2_path = r"C:\workspace\cs231n\proj\data\kitti\2011_09_26_drive_0014_sync_follow\2011_09_26\2011_09_26_drive_0014_sync\image_03\data\0000000243_result.jpg"
res24 = p.predict(
    image1_path=image1_path,
    image2_path=image2_path,
    prompt="going down the suburbian street lightly faster",
)
t28 = time.time()

print("t20 going down the street slightly faster:", t28 - t27)


avg_time = (t28 - t0) / 29
print("avg_time", avg_time)

# C:\workspace\cs231n\proj\DynamiCrafter\output
# ffmpeg.exe -i videoToCompare.mp4 -i originalVideo.mp4 -lavfi ssim=stats_file=ssim_logfile.txt -f null -
# ffmpeg.exe -i videoToCompare.mp4 -i originalVideo.mp4 -lavfi psnr=stats_file=psnr_logfile.txt -f null -
# os.system("ffmpg")
# ffmpeg -r 1/5 -start_number 261 -i "C:\workspace\cs231n\proj\data\kitti\selected\2011_09_26_drive_0091_sync\seq\Ped%d.jpg" -c:v libx264 -r 30 -pix_fmt yuv420p out.mp4
# ffmpeg -i input.lowfps.hevc -filter:v "minterpolate='fps=8'" output.120fps.hevc
# ffmpeg -i input.hevc -filter "minterpolate='mi_mode=mci:mc_mode=aobmc:vsbmc=1'" output.hevc. The filter's documentation contains the description of the available parameters and their values. –
# ffmpeg -r 1/5 -start_number 0 -i C:\myimages\img%03d.png -c:v libx264 -r 30 -pix_fmt yuv420p out.mp4
