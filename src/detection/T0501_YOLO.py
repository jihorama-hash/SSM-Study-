from ultralytics import YOLO

# 변환된 인텔 전용 모델을 사용합니다.
ov_model = YOLO("yolov8n_openvino_model")

# 종합 선물 세트 (프레임 건너뛰기 + 화면 끄기 + 최적화 모델)
ov_model.track(source="output01.mp4", imgsz=640, vid_stride=2, show=False, save=True)