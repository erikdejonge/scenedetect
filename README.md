# scenedetect
Detect scenes and extract them

# before use

## install brew
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

## install mkvtoolkit
brew install mkvtoolnix

## python 3
brew install python3<br>
pip3 install opencv-python

## ffmpeg
brew install ffmpeg


# Execute
> python3 scenedetect.py testvideo.mp4

# Result
Folder with name testvideo containing humbnails and movies


# Alternative
Alternative way via the scenedetect program
**this is not complete, only the points are given**
<br><br>
#### python scenedetect
wget https://github.com/Breakthrough/PySceneDetect/archive/v0.4.tar.gz<br>
tar -xvf v0.4.tar.gz&&rm v0.4.tar.gz<br>
cd PySceneDetect-0.4<br>
python3 setup.py install<br>

#### execute
scenedetect -i ./testvideo.mp4 -o scenes_list.csv -d content -si -df 4



