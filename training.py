from ultralytics import YOLO

model = YOLO("yolov8m.pt")
model.train(data="datasets/data.yaml", epochs=30, imgsz=256, batch=2)