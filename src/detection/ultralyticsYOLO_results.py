from ultralytics import YOLO
import pandas as pd

# 1. 모델 로드
ov_model = YOLO("models/yolov8n_openvino_model")

# 2. 분석 실행 (stream=True를 사용해야 메모리 효율적으로 데이터를 가로챌 수 있습니다)
results = ov_model.track(source="data/raw/test01.mp4", imgsz=640, vid_stride=2, show=False, save=True, stream=True)

# 3. 데이터를 담을 리스트 초기화
extracted_data = []

print("데이터 분석 중...")

for r in results:
    # 프레임 정보 및 탐지된 박스 데이터 가져오기
    frame_idx = getattr(r, 'frame', 0) # 프레임 번호
    boxes = r.boxes
    
    for box in boxes:
        # ID, 좌표, 신뢰도, 클래스 추출
        track_id = int(box.id[0]) if box.id is not None else -1
        cls = int(box.cls[0])
        conf = float(box.conf[0])
        xywh = box.xywh[0].tolist() # 중심 x, y, 너비, 높이
        
        extracted_data.append({
            "Frame": frame_idx,
            "Track_ID": track_id,
            "Class": cls,
            "Confidence": conf,
            "X": xywh[0],
            "Y": xywh[1],
            "W": xywh[2],
            "H": xywh[3]
        })

# 4. Pandas를 이용해 CSV로 저장
if extracted_data:
    df = pd.DataFrame(extracted_data)
    df.to_csv("detection_results.csv", index=False, encoding="utf-8-sig")
    print(f"성공! {len(df)}개의 데이터가 'detection_results.csv'로 저장되었습니다.")
else:
    print("탐지된 데이터가 없습니다.")