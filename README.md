# SSM-Study-
It's a test and pilot ......
YOLO 기반 교통안전 분석 프로젝트
1. 프로젝트 개요
목적: 교차로 영상 기반 위험도 분석
방법: YOLO + Tracking + SSM 분석
대상: 차량 / 보행자 / 이륜차

2. 데이터 정보
데이터 출처: (예: CCTV, 드론 영상 등)
해상도: 1920x1080
FPS: 30
데이터 수량: 총 120개 영상 (약 10시간)
클래스 정의
Class ID	Name
0	Car
1	Bus
2	Pedestrian
3	Bicycle

3. 모델 설정
모델: YOLOv8n
입력 크기: 640
Epoch: 100
Batch size: 16
from ultralytics import YOLO
model = YOLO("yolov8n.pt")
model.train(data="data.yaml", epochs=100, imgsz=640)

4. 학습 결과
성능 지표
Metric	Value
- mAP50	0.91
- Precision	0.88
- Recall	0.85

5. Tracking 및 Trajectory 생성 알고리즘: ByteTrack
출력:
object ID
trajectory (x, y, t)

6. SSM (Surrogate Safety Measure)
사용 지표:
  a. TTC (Time To Collision)
  b. PET (Post Encroachment Time)
계산 방식
  - TTC < 1.5 sec → 위험 이벤트
  - PET < 2.0 sec → 충돌 가능성

7. Risk Analysis
Heatmap 생성
방법: KDE (Kernel Density Estimation)
좌표 변환: Homography 적용

8. 결과 해석
위험 구간: 횡단보도 중앙
주요 원인:
좌회전 차량 vs 보행자 충돌 위험
신호 미준수

9. 실행 방법
git clone <repo_url> cd project
pip install -r requirements.txt
python train.py python detect.py

10. 재현 방법 (Reproducibility)
모델 버전: yolov8n.pt
데이터 버전: v1.2
코드 commit: abc123

## 사무실 작업
2026-04-29 Office 에서 테스트 Commit