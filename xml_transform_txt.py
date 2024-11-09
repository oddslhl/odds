import os
import xml.etree.ElementTree as ET

# 文件夹路径
image_dir = r'E:\下载\yolov10-main\yolov10-main\a_tb_data\train\images'  # 图片所在文件夹
label_dir = r'E:\下载\yolov10-main\yolov10-main\a_tb_data\train\label'  # 标签（.xml 文件）所在文件夹
output_dir = r'E:\下载\yolov10-main\yolov10-main\a_tb_data\train\labels'  # 输出的 .txt 标签文件

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 类别对应表，修改为你的类别
class_mapping = {
    "Header": 0,
    "Title": 1,
    "Text": 2,
    "Figure": 3,
    "Foot": 4
}

def convert_bbox(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[1]) / 2.0 - 1
    y = (box[2] + box[3]) / 2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    return (x * dw, y * dh, w * dw, h * dh)

def convert_annotation(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    filename = os.path.basename(xml_file).replace(".xml", ".txt")
    output_path = os.path.join(output_dir, filename)

    with open(output_path, 'w') as out_file:
        for obj in root.iter('object'):
            cls = obj.find('name').text
            if cls not in class_mapping:
                continue
            cls_id = class_mapping[cls]
            xmlbox = obj.find('bndbox')
            b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text),
                 float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
            bbox = convert_bbox((w, h), b)
            out_file.write(f"{cls_id} {' '.join(map(str, bbox))}\n")

# 转换所有 .xml 文件
for xml_file in os.listdir(label_dir):
    if xml_file.endswith(".xml"):
        convert_annotation(os.path.join(label_dir, xml_file))