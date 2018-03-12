# Default Python Environment for AjouCV

If you are already familiar with Python, use your favorite environments and tools. **But same versions of python and libraries are recommended for reducing compatibility problem between students and professor and TA.**
- 이미 파이썬에 익숙하신 분이라면 본인에게 편한 툴과 환경을 사용해도 무관합니다. 하지만 되도록이면 파이썬이나 라이브러리 버전은 본 환경과 통일하기를 권장합니다. 채점 과정에서 버전으로 인해 발생하는 문제를 최소화하기 위함입니다.

When you use your own favorite environment and tools that we didn't recomend, ***DO NOT ASK*** ABOUT YOUR VERSION AND COMPATIBILITY OF OS, PYTHON, IDE and ETC...
- ~~It's your own problem.~~


## Environment Setting
- Install Newest Anaconda (Mandatory)
  - https://www.anaconda.com/download/
  - DO NOT ALLOW ADMINISTRATOR PRIVILEGE IN WINDOWS INSTALL WIZARD.
- Create your python virtual environment in your Termianl or CMD
  - <code>conda create -n ajoucv python=3.6.4</code>
- Install PyCharm IDE (Recommended)
  - https://www.jetbrains.com/pycharm/
- Create your PyCharm project with <code>ajoucv</code> environment.
  - See the below figures
  - You can find your path of virtual environment with command <code>conda info -e</code> in your terminal.
  
  
  

## How to Install
- Install newest Anaconda version
- create virtual environment with ```python 3.6.4```
  - You can encounter utf-8 encoding problem in windows if you use 3.5 or under versions.
- ```pip install -r requirements.txt```
- ***DO NOT ASK*** ABOUT YOUR VERSION AND COMPATIBILITY OF OS, PYTHON, IDE and ETC...


## Installed Library
This project includes almost useful library for this course. 
 - selective search
   - https://github.com/AlpacaDB/selectivesearch
 - tensorflow 1.4.0
 - pyqt5
 - jupyter
 - keras
 - pycv2
 - numpy
 - scipy
 - scikit-learn
 - scikit-image
 - pandas
 - mglearn
 - matplotlib
 - pillow
 - ... 
 