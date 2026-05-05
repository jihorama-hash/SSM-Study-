# 검은 화면 탈출을 위한 테스트 코드 (배율 조정)
# H 행렬 하단에 아래 연산을 추가하여 도로 1m를 20픽셀로 크게 키워봅니다.
import numpy as np
import cv2

# 1. 이전에 구했던 Homography 행렬 (H) 값을 여기에 정의합니다.
H = np.array([
    [-2.52365931e-01,  7.09779180e-02,  3.00000000e+01],
    [-6.72975815e-02,  1.89274448e-02,  8.00000000e+00],
    [-8.41219769e-03,  2.36593060e-03,  1.00000000e+00]
])

# 2. 배율 설정 (scale_factor)
scale_factor = 20 
S = np.array([[scale_factor, 0, 0], [0, scale_factor, 0], [0, 0, 1]])

# 3. 행렬 곱셈 실행
H_scaled = S @ H  

print("배율이 조정된 행렬 H_scaled:")
print(H_scaled)