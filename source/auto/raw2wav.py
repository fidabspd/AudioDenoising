# raw to wav (noise dataset)

import os

file_list = os.listdir('/home/audiofile/raw/')
file_list = [file for file in file_list if file.endswith('raw')]

for file in file_list:
    name = '.'.join(file.split('.')[:-1])
    os.system('ffmpeg -y -f s16le -ar 48k -ac 1 -i /home/audiofile/raw/{} /home/audiofile/wav/{}.wav'.format(file, name))
