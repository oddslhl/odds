import os
from ultralytics import YOLOv10

# Load a pretrained YOLOv10n model
model = YOLOv10(r"E:\下载\yolov10-main\yolov10-main\runs\detect\train15\weights\best.pt")


image_folder = r"E:\下载\yolov10-main\yolov10-main\a_tb_data\val\val"
images = sorted([os.path.join(image_folder, f) for f in os.listdir(image_folder) if f.endswith((".jpg", ".png"))])

# 预测并保存结果
for image in images:
    model.predict(image, save=True)