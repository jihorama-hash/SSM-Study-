import numpy as np
import cv2
import os

# 1. 파일 경로 설정
input_path = "data/raw/op01.jpg"
output_path = "bev_final_check.jpg"

# 원본 이미지 불러오기
img = cv2.imread(input_path)
if img is None:
    print(f"에러: {input_path} 파일을 찾을 수 없습니다. 경로를 확인하세요.")
    exit()

# 2. 이전에 구했던 원본 Homography 행렬 (H) 정의
H = np.array([
    [3.84215397e+00,  1.07828192e+01, -3.20162972e+03],
    [1.86117708e+00, -1.18650039e+01,  2.92623567e+03],
    [4.29545967e-03,  2.78885415e-01,  1.00000000e+00]
])

# 3. [핵심] 검은 화면 탈출을 위한 복합 변환 행렬 생성

# A. 배율 조정: 실제 거리 1m를 20픽셀로 표현
scale_factor = 20 
S = np.array([[scale_factor, 0, 0], [0, scale_factor, 0], [0, 0, 1]])

# B. 평행 이동(Offset): 변환된 이미지를 화면 중앙으로 끌고 옵니다. (수치 조정 가능)
# X축으로 +600픽셀, Y축으로 +200픽셀 이동
offset_x, offset_y = 600, 200
T = np.array([[1, 0, offset_x], [0, 1, offset_y], [0, 0, 1]])

# C. 행렬 합성 (T @ S @ H): 원본 H에 배율과 평행이동을 한 번에 적용합니다.
H_scaled_shifted = T @ S @ H  

print("-" * 30)
print("배율과 이동이 모두 적용된 최종 행렬 H_final:")
print(H_scaled_shifted)
print("-" * 30)

# 4. [명령 추가] 최종 행렬을 사용하여 이미지 변환 실행 (Warping)
# 출력 이미지 크기를 넉넉하게 1200x1200으로 설정
width, height = 1200, 1200
bev_img = cv2.warpPerspective(img, H_scaled_shifted, (width, height))

# 5. [명령 추가] 결과 저장 및 확인
cv2.imwrite(output_path, bev_img)
print(f"성공: BEV 변환 이미지가 '{output_path}'로 저장되었습니다.")