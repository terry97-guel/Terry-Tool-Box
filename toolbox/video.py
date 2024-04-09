# %%
from pathlib import Path
import cv2
def mp4_to_png(mp4_path, png_folder):
    mp4_path = Path(mp4_path)
    png_folder = Path(png_folder)
    assert mp4_path.exists()
    
    png_folder.mkdir(parents=True, exist_ok=True)
    vidcap = cv2.VideoCapture(str(mp4_path))
    success,image = vidcap.read()
    count = 0
    while success:
        cv2.imwrite(str(png_folder) + "/frame%d.png" % count, image)     # save frame as PNG file
        success,image = vidcap.read()
        count += 1
    print("Extracted %d frames from %s" % (count, mp4_path))

