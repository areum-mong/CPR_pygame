# 두쫀쿠 박자 판정 및 점수 로직

import time
from config import BPM

class RhythmEngine:
    def __init__(self):
        self.beat_interval = 60 / BPM  # 110 BPM 기준 약 0.545초
        self.start_time = 0
        self.is_running = False
        
        # 판정 범위 설정 (초 단위)
        self.PERFECT_RANGE = 0.12  # ±0.12초 이내
        self.GREAT_RANGE = 0.22    # ±0.22초 이내

    def start(self):
        """음악 시작 시점을 기록합니다."""
        self.start_time = time.time()
        self.is_running = True

    def get_judgment(self):
        """사용자가 누른 시점을 판정합니다."""
        if not self.is_running: return None, 0

        current_time = time.time()
        elapsed = current_time - self.start_time
        
        # 현재 가장 가까운 박자 위치 계산
        closest_beat = round(elapsed / self.beat_interval)
        target_time = closest_beat * self.beat_interval
        
        # 오차(오프셋) 계산
        offset = abs(elapsed - target_time)

        if offset <= self.PERFECT_RANGE:
            return "PERFECT", 100
        elif offset <= self.GREAT_RANGE:
            return "GREAT", 50
        else:
            return "MISS", 0