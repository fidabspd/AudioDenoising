# denoise

import os

file_list = os.listdir('/home/audiofile/input')

for file in file_list:
    name = '.'.join(file.split('.')[:-1])
    os.system('ffmpeg -y -i /home/audiofile/input/{} -ar 48k -ac 1 -acodec pcm_s16le -f s16le /home/audiofile/pcm_before/{}.pcm'.format(file, name))
    os.system('/home/rnnoise/examples/rnnoise_demo /home/audiofile/pcm_before/{}.pcm /home/audiofile/pcm_after/{}_after.pcm'.format(name, name))
    os.system('ffmpeg -y -f s16le -ar 48k -ac 1 -i /home/audiofile/pcm_after/{}_after.pcm /home/audiofile/done/{}_after.wav'.format(name, name))
