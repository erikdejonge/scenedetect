# scenedetect
Detect scenes and extract them

# before use

## install brew
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

## install mkvtoolkit
brew install mkvtoolnix

## python 3
brew install python3
pip3 install opencv-python

## ffmpeg
brew install ffmpeg


# alternative

## python scenedetect
wget https://github.com/Breakthrough/PySceneDetect/archive/v0.4.tar.gz
tar -xvf v0.4.tar.gz&&rm v0.4.tar.gz
cd PySceneDetect-0.4
python3 setup.py install

## execute
scenedetect -i ./testvideo.mp4 -o scenes_list.csv -d content -si -df 4



