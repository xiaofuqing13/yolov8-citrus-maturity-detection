from ultralytics import YOLO
import os

# 避免多线程冲突的环境变量配置
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
os.environ["OMP_NUM_THREADS"] = "1"

if __name__ == "__main__":
    # 加载 YOLO 模型
    model = YOLO("yolov8n.pt")  # 加载 YOLOv8 的 nano 模型权重

    # 开始训练
    model.train(
        data=r"C:\Users\1\PycharmProjects\PythonProject\基于机器视觉的柑橘成熟度检测\Original dataset\data.yaml",  # 数据集配置文件
        epochs=1000,          # 训练的 epoch 数
        batch=40,             # 批量大小
        device="cuda",        # 使用 GPU
        imgsz=640,            # 输入图片大小
        workers=4             # 数据加载线程数
    )