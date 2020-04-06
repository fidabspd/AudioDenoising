# Audio Denoising

## Study with <https://github.com/xiph/rnnoise>

rnnoise 코드를 윈도우에서 띄운 우분투 도커 환경에서 실행 할 수 있도록 만들었습니다.

## ! 주의 사항

해당 모델은 sampling rate 48000, mono 채널, 16 bit 파일에 맞춰져있습니다.\
(이에 맞게 변환하는 코드도 포함되어있음)

## 폴더 구성

- `audiofile`: denoise할 원본파일과 결과물이 저장되는 폴더
  - `input`: 원본파일
  - `pcm_before`: 원본파일을 .pcm확장자로 바꾼 것
  - `pcm_after`: denoise 완료한 .pcm파일
  - `done`: denoise 완료한 .pcm파일을 다시 wav파일로 변환한 것
  - `raw`: .wav로 변환하고자 하는 .raw파일이나 .pcm파일들
- `auto`: denoise 및 파일확장자 변경 자동화를 위한 코드
- `rnnoise`: rnnoise의 git clone + 컴파일 완료(denoise를 위한 바이너리 파일 생성)

### 1. Docker container 만들기

shell에서 `Dockerfile`과 `docker-compose.yml`이 있는 현재 디렉토리로 와서 다음 코드 실행

```powershell
docker build -t rnnoise .
docker-compose up
```

### 2. Denoising

denoise하고자 하는 원본 파일(.wav .m4a 등의 확장자)을 audiofile/input폴더 안에 넣고\
docker container의 shell을 attach, 다음코드 실행\
(denoise 완료 된 결과물은 done 폴더에 저장)

```powershell
python3 /home/auto/denoise.py
```

### 3. Convert raw to wav

마찬가지로 container안의 shell에서 다음 코드 실행\
(.wav로 변환 된 파일은 input 폴더에 저장)

```powershell
python3 /home/auto/raw2wav.py
```

### 다시 컨테이너를 실행하고 싶은 경우

```powershell
docker start rnnoise
```
