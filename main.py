# 두쫀쿠 씬 매니저 역할
# 전체 흐름을 제어 파일 

import pygame
import sys
from config import *
from rhythm_engine import RhythmEngine

class DujjonkuGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("두쫀쿠 CPR - 110 BPM 리듬 테스트")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("malgungothic", 80, bold=True)
        
        # 엔진 및 상태 변수
        self.engine = RhythmEngine()
        self.judgment_text = ""
        self.judgment_color = WHITE
        self.score = 0
        self.is_playing = False
        
        # 캐릭터 상태 (DA의 chr_cpr_1, 2 대용 임시 변수)
        self.is_pressing = False

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not self.is_playing:
                        self.engine.start() # 첫 스페이스바를 누르면 시작
                        self.is_playing = True
                    else:
                        # 리듬 판정 수행
                        res, points = self.engine.get_judgment()
                        self.judgment_text = res
                        self.score += points
                        
                        # 색상 결정
                        if res == "PERFECT": self.judgment_color = GREEN
                        elif res == "GREAT": self.judgment_color = YELLOW
                        else: self.judgment_color = RED
                        
                        self.is_pressing = True # 누른 효과
                
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    self.is_pressing = False # 떼는 효과

    def draw(self):
        self.screen.fill(BLACK)
        
        # 1. 캐릭터(Placeholder) 그리기
        color = GREEN if not self.is_pressing else RED
        pygame.draw.rect(self.screen, color, (WIDTH//2 - 100, HEIGHT//2 - 100, 200, 200))
        
        # 2. 판정 텍스트 그리기
        if self.judgment_text:
            text_surf = self.font.render(self.judgment_text, True, self.judgment_color)
            text_rect = text_surf.get_rect(center=(WIDTH//2, HEIGHT//2 - 250))
            self.screen.blit(text_surf, text_rect)
            
        # 3. 점수 표시
        score_surf = self.font.render(f"SCORE: {self.score}", True, WHITE)
        self.screen.blit(score_surf, (50, 50))
        
        # 가이드 메시지
        if not self.is_playing:
            guide = pygame.font.SysFont("malgungothic", 30).render("SPACE를 눌러 CPR을 시작하세요!", True, WHITE)
            self.screen.blit(guide, (WIDTH//2 - 200, HEIGHT//2 + 150))

        pygame.display.flip()

    def run(self):
        while True:
            self.handle_events()
            self.draw()
            self.clock.tick(FPS)

if __name__ == "__main__":
    game = DujjonkuGame()
    game.run()