ffmpeg -i testvideo.mp4 -filter:v "select='gt(scene\,0.4)',showinfo" -vsync vfr -f null - 2> ffout
ffmpeg -i testvideo.mp4 -filter:v "select='gt(scene\,0.4)'" -vsync vfr frame%d.png

grep showinfo ffout | puf "[x.split('pts_time:')[1].split('pos')[0].strip() for x in lines if 'pts_time:' in x]" >timestamps

