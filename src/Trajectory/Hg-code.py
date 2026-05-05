import cv2
import numpy as np

# 1. 이미지 상의 4개 점 (픽셀 좌표)
src_pts = np.array([[192, 260], [183, 228], [756, 304], [767, 302]], dtype=np.float32)

# 2. 실제 도로상의 4개 점 (미터 단위 좌표)
# 예: (0,0)을 기준으로 가로 8.0m, 세로 30m 구역이라면
dst_pts = np.array([[0, 0], [8.0, 0], [30.0, 8.0], [30.0, 8.0]], dtype=np.float32)

# 3. Homography 행렬 계산
H = cv2.getPerspectiveTransform(src_pts, dst_pts)
print("-" * 30)
print("계산된 Homography 행렬 (H):")
print(H)
print("-" * 30)