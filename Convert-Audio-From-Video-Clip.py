# first you need to install moviepy.editor
# pip install moviepy

import moviepy.editor

video = moviepy.editor.VideoFileClip('file_name.mp4')

audio = video.audio

audio.write_audiofile('save_file.mp3')
# =-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
