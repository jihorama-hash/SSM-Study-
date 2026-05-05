import cv2
import numpy as np
import os

# 1. 파일 경로 설정
input_path = "data/raw/op01.jpg"
output_path = "bev_result.jpg"

# 2. 이미지 불러오기
img = cv2.imread(input_path)
if img is None:
    print(f"에러: {input_path} 파일을 찾을 수 없습니다.")
else:
    # 3. 이미 제시된 Homography 행렬 (H) 입력
    # 제시해주신 행렬 값을 numpy array 형태로 정의합니다.
    H = np.array([
        [-2.52365931e-01,  7.09779180e-02,  3.00000000e+01],
        [-6.72975815e-02,  1.89274448e-02,  8.00000000e+00],
        [-8.41219769e-03,  2.36593060e-03,  1.00000000e+00]
    ])

    # 4. 출력 이미지 크기 설정 (가로, 세로 픽셀 수)
    # 실제 도로 영역을 적절히 표현할 수 있는 크기로 설정합니다. (임의 설정 가능)
    width, height = 800, 500 

    # 5. 이미지 변환 실행 (Warping)
    bev_img = cv2.warpPerspective(img, H, (width, height))

    # 6. 결과 저장 및 확인
    cv2.imwrite(output_path, bev_img)
    print(f"성공: BEV 변환 이미지가 '{output_path}'로 저장되었습니다.")
    
    # (선택 사항) 화면에 바로 띄워서 확인하고 싶을 때
    # cv2.imshow("BEV Result", bev_img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()