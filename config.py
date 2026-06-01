# 두쫀쿠 모든 설정값 및 경로 관리

import pygame
import os

# 1. 화면 및 게임 기본 설정
WIDTH, HEIGHT = 1024, 1024
FPS = 60

# 2. 색상 (가독성을 위해 사전 정의)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 50, 50)
GREEN = (50, 255, 50)
YELLOW = (255, 255, 50)

# 3. 의학적 고증: 110 BPM (가슴압박 속도)
BPM = 110
TIMER_LIMIT = 30  

# 4. 경로 설정 (파일이 없어도 에러가 나지 않게 관리)
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
IMG_PATH = os.path.join(BASE_PATH, "assets", "images")
SND_PATH = os.path.join(BASE_PATH, "assets", "sounds")