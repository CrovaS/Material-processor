<p align='center'>
  <img src="https://user-images.githubusercontent.com/86072294/132429234-81836a8b-300d-4e76-a5e2-95c73cb023e6.PNG" width="250">
</p>
<h1 align='center'>  Material-Processor </h1>
<p align='center'>
  <a href="http://www.apache.org/licenses/LICENSE-2.0"><img src="https://img.shields.io/github/license/CrovaS/Material-processor"/></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3766AB?style=flat-square&logo=Python&logoColor=white"/></a>
</p>

## Update
This program is not complete.
Only minimal backend part has been made.

## Function
There are six function in the program.

### 1. PDF & PPT -> TXT (Mode 1: text)
교수님의 강의자료가 ppt나 pdf로 되어 있어 읽기 힘들다! \
그냥 하나로 모아서 텍스트로 쉽게 볼 수 있었으면 좋겠는데...
```
a) ppt폴더에는 ppt들, pdf 폴더에는 pdf들을 넣어놓는다.
b) 모듈 선택에서 (1)을 선택한 후 기다린다.
c) read 폴더에는 각 파일들에 있는 텍스트를 그대로 읽어온 파일들이 생성된다.
d) write 폴더에는 read에 있는 텍스트들에서 불필요한 부분들을 인식해 걸러준 파일들이 생성된다.
(반복적인 목차 표시, 표로 인식되어 나온 결과물 중 뭉개진 부분 등)
```

### 2. Youtube -> MP4 / MP3 (Mode 2: singlemode)
마음에 쏙 드는 영상을 발견했는데 영상이나 소리를 저장하고 싶다! \
다운로드 받아서 보고 싶은데...
```
a) 모듈 선택에서 (2)을 선택한 후 프로그램에서 물어보는 기본 정보들에 답변한다.
b) mp4 폴더나 mp3 폴더를 확인해보면 결과물이 생성된다.
```

## Work Flow
#### 1. Make six folders, it must be same with below:
<img src = "https://user-images.githubusercontent.com/86072294/132428343-ebfc63bd-5011-45e2-b9d2-e32f1580308e.png">
Name of the folder is mp3, mp4, pdf, ppt, read, write.

#### 2. Run main.py
```
python main.py
```
