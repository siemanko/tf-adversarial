import tempfile
import subprocess
import shutil
import base64
import os

from IPython.display import HTML


def make_video(frames, out_file="out.mp4"):
    with tempfile.TemporaryDirectory() as d:
        frame_files = []
        for i, frame in enumerate(frames):
            file_name = os.path.join(d, "frame_%06d.png" % (i,))
            frame.save(file_name)
            frame_files.append(file_name)
        x = subprocess.check_output(["ffmpeg", "-r", "24", "-pattern_type", "glob","-i",
                                     '*.png', "-c:v", "libx264", out_file], cwd=d) 
        shutil.move(os.path.join(d, out_file), out_file)

def display_video(fname):
    return HTML("""<video width="400" height="222" controls="controls">
      <source src="%s" type="video/mp4" />
    </video>""" % (fname,))

