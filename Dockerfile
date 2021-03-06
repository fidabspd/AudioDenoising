# base image
FROM ubuntu:18.04

# update package list
RUN apt-get update && apt-get upgrade -y
# install vim (윈도우와 리눅스의 개행문자 차이 수정을 위함)
RUN apt-get install vim -y
# install libtool
RUN apt-get install libtool -y
# install autoconf
RUN apt-get install autoconf -y
# install git
RUN apt-get install git -y
# install sox
RUN apt-get install sox -y
# install ffmpeg
RUN apt-get install ffmpeg -y

# install python3.6 and pip3
RUN apt-get install python3.6 python3-pip -y

# 로컬의 requirements.txt를 컨테이너의 home 폴더에 복사한다
COPY ./source/requirements.txt ./home/

# install packages
RUN pip3 install -r ./home/requirements.txt
# /root/.jupyter/jupyter_notebook_config.py 파일 생성
RUN jupyter notebook --generate-config
# 브라우저을 열지않게 설정
RUN echo "c.NotebookApp.open_browser = False" >> /root/.jupyter/jupyter_notebook_config.py
# 비밀번호 설정 (접속할 때 실제 사용하는 비밀번호에서 암호화 된 비밀번호를 써야함)
RUN echo "c.NotebookApp.password = u'sha1:d5d29dc31a19:0fa77a3d46fb6bae4d7f595d0984b6d7f385221f'" >> /root/.jupyter/jupyter_notebook_config.py

# home에서 jupyter notebook 실행 (루트 권한을 주고 8888포트에서 실행한다)
WORKDIR /home/
ENTRYPOINT jupyter notebook --allow-root --ip=0.0.0.0 --port=8888
