# src/prepare_data.py
import os
import random
from pathlib import Path
from shutil import copyfile
from PIL import Image

random.seed(42)

def is_image_valid(path):
    try:
        Image.open(path).verify()
        return True
    except Exception:
        return False

def prepare_split(root_raw, root_out, split_ratio=(0.7, 0.15, 0.15)):
    splits = ['train', 'val', 'test']
    for cat in ['Cat', 'Dog']:
        files = list((root_raw / cat).glob('*.jpg'))
        files = [f for f in files if f.stat().st_size > 0 and is_image_valid(f)]
        random.shuffle(files)
        n = len(files)
        counts = [int(n * r) for r in split_ratio]
        counts[2] = n - sum(counts[:2])  # adjust for rounding
        idx = 0
        for split, cnt in zip(splits, counts):
            out_dir = root_out / split / cat.lower()
            out_dir.mkdir(parents=True, exist_ok=True)
            for f in files[idx:idx+cnt]:
                copyfile(f, out_dir / f.name)
            idx += cnt
            print(f"{cat}: {n} files -> {dict(zip(splits, counts))}")

if __name__ == "__main__":
    raw = Path("data/raw/PetImages")
    out = Path("data/processed")
    prepare_split(raw, out)
    print("Dataset prepared!")
