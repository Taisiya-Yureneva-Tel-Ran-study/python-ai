import cv2
import numpy as np

BASE_ROOT = "datasets/"
BASE_IMAGES = BASE_ROOT + "images/"
TRAIN_IMAGES = BASE_IMAGES + "train/"
BASE_LABELS = BASE_ROOT + "labels/"
TRAIN_LABELS = BASE_LABELS + "train/"
WIDTH  = 256
HEIGHT = 256
COUNT = 30
VAL_COUNT = 3

def make_label(xc, yc, r, path, type):
    x = xc / WIDTH
    y = yc / HEIGHT
    w = r * 2 / WIDTH
    h = r * 2 / HEIGHT
    typ = 1 if type == "rect" else 0 
    with open(path, 'w') as f:
         f.write(f"{typ} {x:.6f} {y:.6f} {w:.6f} {h:.6f}")

def make_figure(x1, y1, w, path, type: str = "rect"):
    im_arr: np = np.zeros((WIDTH, HEIGHT, 3), dtype=np.uint8)
    if type == "rect": #  x, y - center and w is side length / 2
        cv2.rectangle(im_arr, (x1-w, y1-w), (x1 + w, y1 + w), (0, 0, 200), -1)
    else:   #  x, y - center and w is radius
        cv2.circle(im_arr, (x1, y1), w, (0, 0, 200), -1)
    cv2.imwrite(path, im_arr)

def make_figure_with_label(x1, y1, w, path, type: str = "rect"):
    make_figure(x1, y1, w, path, type)
    make_label(x1, y1, w, path.replace("images", "labels").replace(".png", ".txt"), type)
    
def get_coordinates():
    w = np.random.randint(10, 100)
    x = np.random.randint(w, WIDTH-w) # so that figure is not out of image
    y = np.random.randint(w, HEIGHT-w)
    return (x, y, w)

if __name__ == "__main__":   
    for i in range(COUNT):
        x, y, w = get_coordinates()
        make_figure_with_label(x, y, w, TRAIN_IMAGES + f"rect_{i}.png", "rect")
        make_figure_with_label(x, y, w, TRAIN_IMAGES + f"circle_{i}.png", "circle")
    
    for i in range(VAL_COUNT):
        x, y, w = get_coordinates()
        make_figure_with_label(x, y, w, BASE_IMAGES + f"val/rect_{i}.png", "rect")
        make_figure_with_label(x, y, w, BASE_IMAGES + f"val/circle_{i}.png", "circle")
    
