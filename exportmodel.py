from ultralytics import YOLOv10
# Load a pretrained YOLOv10n model
model = YOLOv10('yolov10n.pt')
model = YOLOv10(r"E:\\下载\\yolov10-main\\runs\\detect\\train2\\weights\\best.pt")

model.export(format='onnx')