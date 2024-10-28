# -*- coding: utf-8 -*-

import subprocess
import os

def convert_wav(video_filename: str, _audio_extension: str = ".wav") -> str:
    new_filename = os.path.splitext(video_filename)[0] + _audio_extension
    command = ['ffmpeg', '-i', video_filename, '-ac', '1', '-ar', '16000', new_filename, '-y']

    subprocess.run(command)
    
    return new_filename