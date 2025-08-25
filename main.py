import os
import shutil
from datetime import datetime

sourcedir = r"C:\Users\owner's\Downloads\testing"


destdir = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "files-python": [".py", ".ipynb"],
    "files-web": [".html", ".css", ".js"],
    "files-codingother": [".c", ".cpp", ".java", ".rb", ".go", ".rs"],
    "Exe": [".exe", ".msi"],
    "3d-Files": [".stl", ".obj", ".fbx"]
    }

def organize():
    for f in os.listdir(sourcedir):
        fpath = os.path.join(sourcedir, f)

        if os.path.isdir(fpath):
            continue

        x, ext = os.path.splitext(f)
        ext = ext.lower()

        move = False
        for i, j in destdir.items():
            if ext in j:
                target = os.path.join(sourcedir, i)
                os.makedirs(target, exist_ok=True)
                shutil.move(fpath, os.path.join(target, f))
                print(f"moved {f} to {i} folder!! now it looks clean")
                move = True
                break
        if not move: 
            target = os.path.join(sourcedir, "Others")
            os.makedirs(target, exist_ok=True)
            shutil.move(fpath, os.path.join(target, f))
            print(f"moved {f} to Others!! stop making random files!")

    print(f"CLUTTER CLEARED!!! on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    organize()
    