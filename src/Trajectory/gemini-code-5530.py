import numpy as np
import cv2

# 1. 좌표 재설정 (순서와 수치를 정밀하게 매칭)
src_pts = np.array([[98, 262], [185, 231], [756, 305], [761, 366]], dtype=np.float32)
# 실제 거리 (미터 단위). 4번째 점을 [30, 0]으로 분리했습니다.
dst_pts = np.array([[0, 0], [0, 8.0], [33.5, 8.0], [34.5, 0]], dtype=np.float32)

# 2. 새로운 Homography 행렬 계산
H = cv2.getPerspectiveTransform(src_pts, dst_pts)

# 3. 화면 안으로 끌어오기 위한 보정 행렬
# 1미터를 30픽셀로 표시하고, 화면 중앙(200, 200)으로 이동
scale = 30
offset_x, offset_y = 200, 200
T = np.array([[scale, 0, offset_x], [0, scale, offset_y], [0, 0, 1]])

H_final = T @ H

# 4. 이미지 변환 및 저장
img = cv2.imread("data/raw/op01.jpg")
if img is not None:
    # 넉넉한 크기의 캔버스에 그리기
    bev_img = cv2.warpPerspective(img, H_final, (1600, 1000))
    cv2.imwrite("bev_success_final.jpg", bev_img)
    print("성공: bev_success_final.jpg 파일을 확인하세요.")
else:
    print("이미지를 불러올 수 없습니다.")