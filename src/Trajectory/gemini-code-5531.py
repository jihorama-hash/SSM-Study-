import numpy as np
import cv2

# 1. 좌표 재설정 (이미지 상의 점 순서와 실제 거리 순서를 엄격히 매칭)
# 점의 순서를 '좌상 -> 우상 -> 우하 -> 좌하' 시계방향으로 통일해 봅니다.
src_pts = np.array([[185, 231], [756, 305], [761, 366], [98,262]], dtype=np.float32)
dst_pts = np.array([[0, 0], [33.5, 0], [34.5, 8.0], [0, 8.0]], dtype=np.float32)

# 2. 새로운 Homography 행렬 계산
H = cv2.getPerspectiveTransform(src_pts, dst_pts)

# 3. 비현실적 비율 수정을 위한 개별 스케일 적용
# 세로가 너무 늘어났다면 scale_y를 scale_x보다 작게 조정하세요.
scale_x = 40  # 가로 1m당 40픽셀
scale_y = 15  # 세로 1m당 15픽셀 (늘어짐 방지를 위해 절반으로 줄임)

offset_x = 200 
offset_y = 1000

T = np.array([[scale_x, 0, offset_x], [0, scale_y, offset_y], [0, 0, 1]])

H_final = T @ H

# 4. 이미지 변환
img = cv2.imread("data/raw/op01.jpg")
width = 1600
height = 2000
if img is not None:
    # 뒤집힘 방지를 위해 필요시 아래 함수를 사용할 수 있지만, 
    # 위에서 점 순서(src_pts)를 조정하는 것이 가장 깔끔합니다.
    bev_img = cv2.warpPerspective(img, H_final, (1600, 2000))
    
    # 만약 결과가 여전히 뒤집혔다면 아래 주석을 해제하세요.
    # bev_img = cv2.flip(bev_img, 0) # 상하 반전
    
    cv2.imwrite("bev_final_fixed01.jpg", bev_img)
    print("성공: 비율과 방향이 보정된 bev_final_fixed01.jpg를 확인하세요.")