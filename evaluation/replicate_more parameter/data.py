

# 10 biking along a wall    C:\workspace\cs231n\proj\data\kitti\videos\TRAIN\2011_09_26\2011_09_26_drive_0002_sync\image_03\data\001_result.jpg
ffmpeg  -start_number 1 -i "C:\workspace\cs231n\proj\data\kitti\videos\TRAIN\2011_09_26\2011_09_26_drive_0002_sync\image_03\data\%d_result.jpg" -c:v libx264 -r 10 -pix_fmt yuv420p "C:\workspace\cs231n\proj\DynamiCrafterLora\data\driving\videos\0-1000\10.mp4"
ffmpeg -i "C:\workspace\cs231n\proj\data\kitti\videos\TRAIN\2011_09_26\2011_09_26_drive_0002_sync\image_03\data\%03d_result.jpg" -filter:v fps=10 "C:\workspace\cs231n\proj\DynamiCrafterLora\data\driving\videos\0-1000\10.mp4"
# start_number 100 and -frames:v 101 %0d
# street grass trees, bus industrial
ffmpeg -i "C:\workspace\cs231n\proj\data\kitti\videos\TRAIN\2011_09_26\2011_09_26_drive_0011_sync\image_03\data\%03d_result.jpg" -filter:v fps=10 "C:\workspace\cs231n\proj\DynamiCrafterLora\data\driving\videos\0-1000\11.mp4"
# bridge trees
ffmpeg -i "C:\workspace\cs231n\proj\data\kitti\videos\TRAIN\2011_09_26\2011_09_26_drive_0013_sync\image_03\data\%03d_result.jpg" -filter:v fps=10 "C:\workspace\cs231n\proj\DynamiCrafterLora\data\driving\videos\0-1000\12.mp4"

# 297
# along train line, grass
ffmpeg -i "C:\workspace\cs231n\proj\data\kitti\TRAIN\2011_09_26\2011_09_26_drive_0015_sync\image_03\data\%03d_result.jpg" -filter:v fps=10 "C:\workspace\cs231n\proj\DynamiCrafterLora\data\driving\videos\0-1000\13.mp4"

# 114
#  crossing cars
ffmpeg -i "C:\workspace\cs231n\proj\data\kitti\TRAIN\2011_09_26\2011_09_26_drive_0017_sync\image_03\data\%03d_result.jpg" -filter:v fps=10 "C:\workspace\cs231n\proj\DynamiCrafterLora\data\driving\videos\0-1000\14.mp4"

#  2 lanes countryside, traffic lights
# 270
ffmpeg -i "C:\workspace\cs231n\proj\data\kitti\TRAIN\2011_09_26\2011_09_26_drive_0018_sync\image_03\data\%03d_result.jpg" -filter:v fps=10 "C:\workspace\cs231n\proj\DynamiCrafterLora\data\driving\videos\0-1000\15.mp4"


# 481 overland drive
ffmpeg -i "C:\workspace\cs231n\proj\data\kitti\TRAIN\2011_09_26\2011_09_26_drive_0019_sync\image_03\data\%03d_result.jpg" -filter:v fps=10 "C:\workspace\cs231n\proj\DynamiCrafterLora\data\driving\videos\0-1000\16.mp4"


# 86 trees suburban biker
ffmpeg -i "C:\workspace\cs231n\proj\data\kitti\TRAIN\2011_09_26\2011_09_26_drive_0020_sync\image_03\data\%03d_result.jpg" -filter:v fps=10 "C:\workspace\cs231n\proj\DynamiCrafterLora\data\driving\videos\0-1000\17.mp4"

# 800, suburbanm grass
ffmpeg -i "C:\workspace\cs231n\proj\data\kitti\TRAIN\2011_09_26\2011_09_26_drive_0022_sync\image_03\data\%03d_result.jpg" -filter:v fps=10 "C:\workspace\cs231n\proj\DynamiCrafterLora\data\driving\videos\0-1000\18.mp4"


# 474 suburban some traffic
ffmpeg -i "C:\workspace\cs231n\proj\data\kitti\TRAIN\2011_09_26\2011_09_26_drive_0023_sync\image_03\data\%03d_result.jpg" -filter:v fps=10 "C:\workspace\cs231n\proj\DynamiCrafterLora\data\driving\videos\0-1000\19.mp4"

#  188 forest single lane 
ffmpeg -i "C:\workspace\cs231n\proj\data\kitti\TRAIN\2011_09_26\2011_09_26_drive_0027_sync\image_03\data\%03d_result.jpg" -filter:v fps=10 "C:\workspace\cs231n\proj\DynamiCrafterLora\data\driving\videos\0-1000\20.mp4"


## 430 forest single lane
ffmpeg -i "C:\workspace\cs231n\proj\data\kitti\TRAIN\2011_09_26\2011_09_26_drive_0028_sync\image_03\data\%03d_result.jpg" -filter:v fps=10 "C:\workspace\cs231n\proj\DynamiCrafterLora\data\driving\videos\0-1000\21.mp4"

## 430 empty country road
ffmpeg -i "C:\workspace\cs231n\proj\data\kitti\TRAIN\2011_09_26\2011_09_26_drive_0029_sync\image_03\data\%03d_result.jpg" -filter:v fps=10 "C:\workspace\cs231n\proj\DynamiCrafterLora\data\driving\videos\0-1000\22.mp4"

# 390 country road soem traffic
ffmpeg -i "C:\workspace\cs231n\proj\data\kitti\TRAIN\2011_09_26\2011_09_26_drive_0032_sync\image_03\data\%03d_result.jpg" -filter:v fps=10 "C:\workspace\cs231n\proj\DynamiCrafterLora\data\driving\videos\0-1000\23.mp4"


## 131 village
ffmpeg -i "C:\workspace\cs231n\proj\data\kitti\TRAIN\2011_09_26\2011_09_26_drive_0035_sync\image_03\data\%03d_result.jpg" -filter:v fps=10 "C:\workspace\cs231n\proj\DynamiCrafterLora\data\driving\videos\0-1000\24.mp4"


## 395 houses
ffmpeg -i "C:\workspace\cs231n\proj\data\kitti\TRAIN\2011_09_26\2011_09_26_drive_0020_sync\image_03\data\%03d_result.jpg" -filter:v fps=10 "C:\workspace\cs231n\proj\DynamiCrafterLora\data\driving\videos\0-1000\25.mp4"

## 125 traditional houses
ffmpeg -i "C:\workspace\cs231n\proj\data\kitti\TRAIN\2011_09_26\2011_09_26_drive_0046_sync\image_03\data\%03d_result.jpg" -filter:v fps=10 "C:\workspace\cs231n\proj\DynamiCrafterLora\data\driving\videos\0-1000\26.mp4"

# 438 country side some traffic
ffmpeg -i "C:\workspace\cs231n\proj\data\kitti\TRAIN\2011_09_26\2011_09_26_drive_0052_sync\image_03\data\%03d_result.jpg" -filter:v fps=10 "C:\workspace\cs231n\proj\DynamiCrafterLora\data\driving\videos\0-1000\27.mp4"

## 294 tree lined road 
ffmpeg -i "C:\workspace\cs231n\proj\data\kitti\TRAIN\2011_09_26\2011_09_26_drive_0056_sync\image_03\data\\%03d_result.jpg" -filter:v fps=10 "C:\workspace\cs231n\proj\DynamiCrafterLora\data\driving\videos\0-1000\28.mp4"

## 373  follow car therough village
ffmpeg -i "C:\workspace\cs231n\proj\data\kitti\TRAIN\2011_09_26\2011_09_26_drive_0059_sync\image_03\data\%03d_result.jpg" -filter:v fps=10 "C:\workspace\cs231n\proj\DynamiCrafterLora\data\driving\videos\0-1000\29.mp4"

##  645 residental multifloor buildings
ffmpeg -i "C:\workspace\cs231n\proj\data\malaga-urban-dataset-extract-04\TRAIN\malaga-urban-dataset-extract-04\l\%03d_result.jpg" -filter:v fps=20 "C:\workspace\cs231n\proj\DynamiCrafterLora\data\driving\videos\0-1000\30.mp4"
## 1855 countryside coonstruction
ffmpeg -i "C:\workspace\cs231n\proj\data\malaga-urban-dataset-extract-04\TRAIN\malaga-urban-dataset-extract-02\malaga-urban-dataset-extract-02\l\%03d_result.jpg" -filter:v fps=20 "C:\workspace\cs231n\proj\DynamiCrafterLora\data\driving\videos\0-1000\31.mp4"

## 822 resident blocks 20 fps 41
ffmpeg -i "C:\workspace\cs231n\proj\data\malaga-urban-dataset-extract-04\TRAIN\malaga-urban-dataset-extract-03\malaga-urban-dataset-extract-03\l\%03d_result.jpg" -filter:v fps=20 "C:\workspace\cs231n\proj\DynamiCrafterLora\data\driving\videos\0-1000\32.mp4"
## 111 crossing  https://ingmec.ual.es/~jlblanco/malaga-urban-dataset/extracts/malaga-urban-dataset-extract-15.zip
ffmpeg -i "C:\workspace\cs231n\proj\data\malaga-urban-dataset-extract-04\TRAIN\malaga-urban-dataset-extract-09\malaga-urban-dataset-extract-09\l\%03d_result.jpg" -filter:v fps=20 "C:\workspace\cs231n\proj\DynamiCrafterLora\data\driving\videos\0-1000\33.mp4"

## 20 fps, 645 large residental buildings overcast 32.25
ffmpeg -i "C:\workspace\cs231n\proj\data\malaga-urban-dataset-extract-04\TRAIN\malaga-urban-dataset-extract-04\l\%03d_result.jpg" -filter:v fps=20 "C:\workspace\cs231n\proj\DynamiCrafterLora\data\driving\videos\0-1000\34.mp4"

## 20 fps, 4817 palmtrees overcast residental, 4 min 240.85
ffmpeg -i "C:\workspace\cs231n\proj\data\malaga-urban-dataset-extract-04\TRAIN\malaga-urban-dataset-extract-05\malaga-urban-dataset-extract-05\l\%03d_result.jpg" -filter:v fps=20 "C:\workspace\cs231n\proj\DynamiCrafterLora\data\driving\videos\0-1000\35.mp4"

## 20 fps, 10026 167.1 tower overcast 2m47
ffmpeg -i "C:\workspace\cs231n\proj\data\malaga-urban-dataset-extract-04\TRAIN\malaga-urban-dataset-extract-08\malaga-urban-dataset-extract-08\l\%03d_result.jpg" -filter:v fps=20 "C:\workspace\cs231n\proj\DynamiCrafterLora\data\driving\videos\0-1000\36.mp4"

## 20 fps 17306  288.43 residental trees   4min48
ffmpeg -i "C:\workspace\cs231n\proj\data\malaga-urban-dataset-extract-04\TRAIN\malaga-urban-dataset-extract-10\malaga-urban-dataset-extract-10\l\%03d_result.jpg" -filter:v fps=20 "C:\workspace\cs231n\proj\DynamiCrafterLora\data\driving\videos\0-1000\37.mp4"

## 20 fps, 2883 bridge, clouds 144.15  
ffmpeg -i "C:\workspace\cs231n\proj\data\malaga-urban-dataset-extract-04\TRAIN\malaga-urban-dataset-extract-11\malaga-urban-dataset-extract-11\l\%03d_result.jpg" -filter:v fps=20 "C:\workspace\cs231n\proj\DynamiCrafterLora\data\driving\videos\0-1000\38.mp4"

## 8861 20 fps  palm tree cloud buildings 443.05 7m23
ffmpeg -i "C:\workspace\cs231n\proj\data\malaga-urban-dataset-extract-04\TRAIN\malaga-urban-dataset-extract-12\malaga-urban-dataset-extract-12\l\%03d_result.jpg" -filter:v fps=20 "C:\workspace\cs231n\proj\DynamiCrafterLora\data\driving\videos\0-1000\39.mp4"

## 20 fps trees harsh light 2259 , 113s 
ffmpeg -i "C:\workspace\cs231n\proj\data\malaga-urban-dataset-extract-04\TRAIN\malaga-urban-dataset-extract-14\malaga-urban-dataset-extract-14\l\%03d_result.jpg" -filter:v fps=20 "C:\workspace\cs231n\proj\DynamiCrafterLora\data\driving\videos\0-1000\40.mp4"

## 20 fps 1397  69.85s bright traditional multi story buildings sunny
ffmpeg -i "C:\workspace\cs231n\proj\data\malaga-urban-dataset-extract-04\TRAIN\malaga-urban-dataset-extract-15\malaga-urban-dataset-extract-15\l\%03d_result.jpg" -filter:v fps=20 "C:\workspace\cs231n\proj\DynamiCrafterLora\data\driving\videos\0-1000\41.mp4"

## 20 fps, 659 leafy industrial settings
ffmpeg -i "C:\workspace\cs231n\proj\data\malaga-urban-dataset-extract-04\TRAIN\malaga-urban-dataset-extract-13\malaga-urban-dataset-extract-13\l\%03d_result.jpg" -filter:v fps=20 "C:\workspace\cs231n\proj\DynamiCrafterLora\data\driving\videos\0-1000\42.mp4"

##  20 fps, 31442 sculpture parking cars 1572s 26m 12s
ffmpeg -i "C:\workspace\cs231n\proj\data\malaga-urban-dataset-extract-04\TRAIN\malaga-urban-dataset-extract-13\malaga-urban-dataset-extract-13\l\%03d_result.jpg" -filter:v fps=10 "C:\workspace\cs231n\proj\DynamiCrafterLora\data\driving\videos\0-1000\43.mp4"

##  10 fps, 1106, 110 s narrow redidental inner city neigbourhood
ffmpeg -i "C:\workspace\cs231n\proj\data\kitti\TRAIN\2011_09_30\2011_09_30_drive_0027_sync\image_03\data\%03d_result.jpg" -filter:v fps=10 "C:\workspace\cs231n\proj\DynamiCrafterLora\data\driving\videos\0-1000\44.mp4" 

## 29 fps  48s traffic california highway
#ffmpeg -i "C:\workspace\cs231n\proj\data\kitti\TRAIN\2011_09_30\2011_09_30_drive_0027_sync\image_03\data\%03d_result.jpg" -filter:v fps=10 "C:\workspace\cs231n\proj\DynamiCrafterLora\data\driving\videos\0-1000\45.mp4"
ffmpeg -i  C:\workspace\cs231n\proj\data\comma2k19\Chunk_1\Chunk_1\b0c9d2329ad1606b_2018-08-17--14-55-39\9\video.hevc -r 30000/1001 -filter:v "scale=532:-1,crop=512:350,crop=w=512:h=320:x=0:y=0" -c:v libx265 -crf 28 -preset slow -c:a aac -b:a 128k -movflags +faststart "C:\workspace\cs231n\proj\DynamiCrafterLora\data\driving\videos\0-1000\45.mp4"

## 29 fps 48s  , faster highway overcast
ffmpeg -i  C:\workspace\cs231n\proj\data\comma2k19\Chunk_4\Chunk_4\99c94dc769b5d96e_2018-07-02--19-08-27\9\video.hevc -r 30000/1001 -filter:v "scale=532:-1,crop=512:350,crop=w=512:h=320:x=0:y=0" -c:v libx265 -crf 28 -preset slow -c:a aac -b:a 128k -movflags +faststart "C:\workspace\cs231n\proj\DynamiCrafterLora\data\driving\videos\0-1000\46.mp4"

## 29 fps 48s  fps night  highway
ffmpeg -i  C:\workspace\cs231n\proj\data\comma2k19\Chunk_4\Chunk_4\99c94dc769b5d96e_2018-06-18--21-20-21\9\video.hevc -r 30000/1001 -filter:v "scale=532:-1,crop=512:350,crop=w=512:h=320:x=0:y=0" -c:v libx265 -crf 28 -preset slow -c:a aac -b:a 128k -movflags +faststart "C:\workspace\cs231n\proj\DynamiCrafterLora\data\driving\videos\0-1000\47.mp4"

## 29 fps night  highway
ffmpeg -i  C:\workspace\cs231n\proj\data\comma2k19\Chunk_4\Chunk_4\99c94dc769b5d96e_2018-06-18--21-20-21\37\video.hevc -r 30000/1001 -filter:v "scale=532:-1,crop=512:350,crop=w=512:h=320:x=0:y=0" -c:v libx265 -crf 28 -preset slow -c:a aac -b:a 128k -movflags +faststart "C:\workspace\cs231n\proj\DynamiCrafterLora\data\driving\videos\0-1000\48.mp4"

## 29 fps 
ffmpeg -i  C:\workspace\cs231n\proj\data\comma2k19\Chunk_7\Chunk_7\99c94dc769b5d96e_2018-08-03--14-04-02\26\video.hevc -r 30000/1001 -filter:v "scale=532:-1,crop=512:350,crop=w=512:h=320:x=0:y=0" -c:v libx265 -crf 28 -preset slow -c:a aac -b:a 128k -movflags +faststart "C:\workspace\cs231n\proj\DynamiCrafterLora\data\driving\videos\0-1000\49.mp4"

## 29 fps
ffmpeg -i  C:\workspace\cs231n\proj\data\comma2k19\Chunk_4\Chunk_4\99c94dc769b5d96e_2018-06-18--21-20-21\9\video.hevc -r 30000/1001 -filter:v "scale=532:-1,crop=512:350,crop=w=512:h=320:x=0:y=0" -crf 28 -preset slow "C:\workspace\cs231n\proj\DynamiCrafterLora\data\driving\videos\0-1000\50.mp4"

## 10 fps tokyo, 25s shoppers walk down a back alley
ffmpeg -i "C:\workspace\cs231n\proj\data\titan_data\dataset\images_anonymized\images_anonymized\clip_1\images\%03d_result.jpg" -filter:v fps=10 "C:\workspace\cs231n\proj\DynamiCrafterLora\data\driving\videos\0-1000\51.mp4" 

## 10 fps tokyo, 25s shoppers walk down a back alley 99
ffmpeg -i "C:\workspace\cs231n\proj\data\titan_data\dataset\images_anonymized\images_anonymized\clip_5\images\%03d_result.jpg" -filter:v fps=10 "C:\workspace\cs231n\proj\DynamiCrafterLora\data\driving\videos\0-1000\52.mp4" 

## 10 fps tokyo, 25s passants crossing in front of shops 99
ffmpeg -i "C:\workspace\cs231n\proj\data\titan_data\dataset\images_anonymized\images_anonymized\clip_315\images\%03d_result.jpg" -filter:v fps=10 "C:\workspace\cs231n\proj\DynamiCrafterLora\data\driving\videos\0-1000\53.mp4" 

## 10 fps tokyo, back alley biker 99
ffmpeg -i "C:\workspace\cs231n\proj\data\titan_data\dataset\images_anonymized\images_anonymized\clip_508\images\%03d_result.jpg" -filter:v fps=10 "C:\workspace\cs231n\proj\DynamiCrafterLora\data\driving\videos\0-1000\54.mp4" 

## 10 fps food stalls
ffmpeg -i "C:\workspace\cs231n\proj\data\titan_data\dataset\images_anonymized\images_anonymized\clip_480\images\%03d_result.jpg" -filter:v fps=10 "C:\workspace\cs231n\proj\DynamiCrafterLora\data\driving\videos\0-1000\55.mp4" 

## 10 fps   tokyo,construction site powerlines
ffmpeg -i "C:\workspace\cs231n\proj\data\titan_data\dataset\images_anonymized\images_anonymized\clip_486\images\%03d_result.jpg" -filter:v fps=10 "C:\workspace\cs231n\proj\DynamiCrafterLora\data\driving\videos\0-1000\56.mp4" 

## 10 fps  594 passants walking in a backlane
ffmpeg -i "C:\workspace\cs231n\proj\data\titan_data\dataset\images_anonymized\images_anonymized\clip_780\images\%03d_result.jpg" -filter:v fps=10 "C:\workspace\cs231n\proj\DynamiCrafterLora\data\driving\videos\0-1000\57.mp4" 

## 10 fps  backlane with a car driving off
ffmpeg -i "C:\workspace\cs231n\proj\data\titan_data\dataset\images_anonymized\images_anonymized\clip_697\images\%03d_result.jpg" -filter:v fps=10 "C:\workspace\cs231n\proj\DynamiCrafterLora\data\driving\videos\0-1000\58.mp4" 

## 10 fps  backlande with outdoor shops
ffmpeg -i "C:\workspace\cs231n\proj\data\titan_data\dataset\images_anonymized\images_anonymized\clip_701\images\%03d_result.jpg" -filter:v fps=10 "C:\workspace\cs231n\proj\DynamiCrafterLora\data\driving\videos\0-1000\59.mp4" 

## 10 fps  truck driving  in backlane
ffmpeg -i "C:\workspace\cs231n\proj\data\titan_data\dataset\images_anonymized\images_anonymized\clip_585\images\%03d_result.jpg" -filter:v fps=10 "C:\workspace\cs231n\proj\DynamiCrafterLora\data\driving\videos\0-1000\60.mp4" 


P = Period (start of duration spec)
T = Time (starts the time section)
00H = 0 Hours
00M = 0 Minutes
18S = 18 Seconds


ffmpeg -i input.hevc -c:v libx265 -crf 28 -preset slow -c:a aac -b:a 128k -movflags +faststart output.mp4

2.238

 -filter:v "crop=640:360:320:180" 
 C:\workspace\cs231n\proj\data\comma2k19\Chunk_1\Chunk_1\b0c9d2329ad1606b_2018-08-17--14-55-39\9\video.hevc
Video resolution: 1164x874, 29.97
Video resolution: 512x384

-vf "scale=256:160,crop=512:320:(in_w-512)/2:(in_h-320)/2"
ffmpeg -i  C:\workspace\cs231n\proj\data\comma2k19\Chunk_1\Chunk_1\b0c9d2329ad1606b_2018-08-17--14-55-39\9\video.hevc  -filter:v "scale=532:-1,crop=512:350,crop=w=512:h=320:x=0:y=0" -c:v libx265 -crf 28 -preset slow -c:a aac -b:a 128k -movflags +faststart C:\workspace\cs231n\proj\data\comma2k19\Chunk_1\Chunk_1\b0c9d2329ad1606b_2018-08-17--14-55-39\9\output.mp4
C:\workspace\cs231n\proj\data\comma2k19\Chunk_1\Chunk_1\b0c9d2329ad1606b_2018-08-17--14-55-39\8