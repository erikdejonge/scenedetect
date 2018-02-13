# coding=utf-8
"""
Project examples

Usage:
  calculatedurations.py [options] <input>

Options:
  -h --help     Show this screen.

author  : rabshakeh (erik@a8.nl)
project : examples
created : 11/02/2018 / 23:03
"""
import sys
import os
import subprocess

from arguments import Arguments

if sys.version_info.major < 3:
    print("Python 3 is required, exiting")
    exit(1)

ffmpeg = "/usr/local/bin/ffmpeg"
if not os.path.exists(ffmpeg):
    print("ffmpeg not found at", ffmpeg, "exiting")
    exit(1)

class IArguments(Arguments):
    """
    IArguments
    """
    def __init__(self, doc):
        """
        __init__
        """
        self.help = False
        self.input = ""
        super().__init__(doc)


def isnum(x):
    """
    @type x: str
    @return: None
    """
    try:
        float(x)
        return True
    except ValueError:
        return False


def print_run(cmd):
    """
    @type cmd: str
    @return: None
    """
    print('\n', cmd)
    subprocess.run("pwd")

    subprocess.call(cmd, shell=True)


def main():
    """
    main
    """
    arguments = IArguments(__doc__)
    movie = os.path.join(os.getcwd(), arguments.input)

    if not os.path.exists(movie):
        print("File", movie, "can not be found, exiting.")
        return

    moviename = os.path.basename(movie)
    moviebasename = os.path.splitext(moviename)[0]
    print_run(ffmpeg +" -i " + movie + " -filter:v \"select='gt(scene,0.4)',showinfo\" -vsync vfr -f null - 2> ffout")
    print_run("grep showinfo ffout | puf \"[x.split('pts_time:')[1].split('pos')[0].strip() for x in lines if 'pts_time:' in x]\" >timestamps")

    print_run(ffmpeg +" -i " + moviename + " -filter:v \"select='gt(scene,0.4)'\" -vsync vfr " + moviebasename + "_frame_%d.png")
    print_run("mkdir " + moviebasename + "&&mv " + moviebasename + "*.png " + moviebasename)

    timestamps = open('timestamps').read()
    timestamps = [float(x) for x in timestamps.split("\n") if isnum(x)]

    timestamps.insert(0, 0)
    timestamps.reverse()
    timestamps2 = []
    prev = None

    for x in timestamps:
        if prev:
            timestamps2.append([str(x), '%.2f' % float(prev - x)])

        prev = x

    timestamps2.reverse()
    cnt = 0

    for x in timestamps2:
        print_run("ffmpeg -ss " + x[0] + " -i " + moviename + " -c copy -t " + x[1] + " " + moviebasename + "_scene_" + str(cnt) + ".mp4")
        cnt += 1

    return

# )


if __name__ == "__main__":
    main()
