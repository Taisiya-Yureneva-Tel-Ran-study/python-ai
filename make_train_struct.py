import os
BASE_ROOT = "datasets/"
BASE_IMAGES = BASE_ROOT + "images/"
BASE_LABELS = BASE_ROOT + "labels/"

os.makedirs(BASE_IMAGES + "train", exist_ok=True)
os.makedirs(BASE_LABELS + "train", exist_ok=True)
os.makedirs(BASE_IMAGES + "val", exist_ok=True)
os.makedirs(BASE_LABELS + "val", exist_ok=True)
