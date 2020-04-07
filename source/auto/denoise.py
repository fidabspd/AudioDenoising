# denoise

import os
# input폴더에 있는 파일 목록을 받아옴 (미리 오디오 파일만 남겨둘 것)
file_list = os.listdir('/home/audiofile/input')

for file in file_list:
    # 확장자를 제외한 파일명을 name에 할당
    name = '.'.join(file.split('.')[:-1])
    # 원본파일을 denoise모델에 들어가게 하기 위해 pcm파일로 변환
    os.system('ffmpeg -y -i /home/audiofile/input/{} -ar 48k -ac 1 -acodec pcm_s16le -f s16le /home/audiofile/{}.pcm'.format(file, name))
    # denoise한 파일을 pcm파일로 리턴
    os.system('/home/rnnoise/examples/rnnoise_demo /home/audiofile/{}.pcm /home/audiofile/{}_after.pcm'.format(name, name))
    # denoise된 pcm파일을 wav파일로 변환
    os.system('ffmpeg -y -f s16le -ar 48k -ac 1 -i /home/audiofile/{}_after.pcm /home/audiofile/denoise/{}_denoise.wav'.format(name, name))
    # 임시 생성된 pcm파일 두개 삭제
    os.system('rm /home/audiofile/{}.pcm /home/audiofile/{}_after.pcm'.format(name, name))
