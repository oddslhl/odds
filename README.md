# 数据收集与标注

## 1. 数据收集
- 我一共拍摄了100张图片。
- 购买了两斤报纸和10本杂志。
- 挑选的页面Header、Text、Figure、Title、Foot信息分布比较偏矩形分布。
- 在光照条件较好，拍摄角度尽量在垂直的情况下进行拍摄采集。

## 2. 数据标注
- 使用labelImg工具进行标注。
- 用anaconda建立了虚拟环境并激活。
- 安装了对应的库，配置相应的图片和标注文件夹。
- 设置好文件保存格式后进行标注工作。
- 标签要用英文，并且首字母大写。
- 按照Header，Title，Text，Figure，Foot的顺序进行标注。

## 3. 模型训练
- 使用yolov10目标检测架构模型。
- 使用的预训练权重文件是yolov10n。
- 跳过了连接远程服务器的步骤，计划在本机上试跑。
- 下载YOLOv10源码并解压并以此作为项目文件。
- 下载模型预训练权重文件，将权重文件放置在项目文件夹中。
- 按格式准备数据集文件夹，然后上传数据集。
- 在数据集文件夹下新增一个yaml文件，定义数据集的路径和类别名称。
- ![image](https://github.com/user-attachments/assets/3d7803ff-fd66-443a-9d19-48740dd986a9)
- LabelImg标注的数据为.xml格式，YOLO无法直接使用，需要将.xml转换成.txt格式。
- 编写了一个脚本，用xml.etree.ElementTree模块转换格式。
- 模型开始训练时，总是报错。
- ![image](https://github.com/user-attachments/assets/05ba12ad-6c86-4892-841b-71716ac10385)
- 问题出在没有在之前增加的yaml文件里设置nc的值（也就是要检查的目标的个数）。改正错误后进行训练，其中epochs=200 batch=16 device=0，在本机上成功跑完，训练过程耗时六个多小时，得到best.pt文件。
- ![image](https://github.com/user-attachments/assets/591ef425-1c81-4e15-a5e6-3302ab44281c)
- ![image](https://github.com/user-attachments/assets/d0e81377-e545-49ec-89f0-6636443a698b)



### 训练命令
```bash
- yolo detect train data=E:\下载\yolov10-main\yolov10-main\a_tb_data\a_tb.yaml model=yolov10n.pt epochs=200 batch=16 imgsz=640 device=0




