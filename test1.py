from ultralytics import YOLO

# 加载正确的 YOLO 模型
model = YOLO("yolov8n.pt")  # 使用轻量化 YOLOv8 模型

# 运行摄像头检测
results = model(source=0, stream=True)  # 0 表示默认摄像头

for result in results:
    # 处理检测结果并可视化
    result.plot()  # 绘制结果