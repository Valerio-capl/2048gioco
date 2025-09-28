import pygame,sys
from pygame.locals import *
from logic2048 import *
pygame.init()
display = pygame.display.set_mode((righe*100,col*100))
pygame.display.set_caption("2048")
nero = (0, 0, 0)

coloretabella1=(201,202,182)
coloretabella2=(128,129,111)
colori_num={"2" :(255,248,220),
           "4":(250,235,215),
           "8":(255,127,80),
           "16":(255,140,0),
           "32":(205,92,92),
           "64":(255,69,0),
           "128":(240,230,140),
           "256":np.random.randint(255,size=3),
           "512":np.random.randint(255,size=3),
           "1024":np.random.randint(255,size=3),
           "2048":np.random.randint(255,size=3),
           }
display.fill(coloretabella2)

g = grid()
g.inizio_g()

def disegna_tabella(griglia):
    griglia=np.flip(griglia,0)
    font = pygame.font.Font(None, 36)
    for c in range(col):
        for r in range(righe):
            val = griglia[r][c]
            if val == 0:
                colore = coloretabella1
            else:
                colore = colori_num[str(val)]
            
            pygame.draw.rect(display, colore, (c * 100, r * 100, 100, 100))
            pygame.draw.rect(display, coloretabella2, (c * 100, r * 100, 100, 100), 8, 4)
            
            if val != 0:
                text_surface = font.render(str(val), True, nero)
                text_rect = text_surface.get_rect(center=(c * 100 + 50, r * 100 + 50))
                display.blit(text_surface, text_rect)
                
    pygame.display.update()

disegna_tabella(g.griglia)
fine=False

while not fine:
    	
    for event in pygame.event.get():
        if event.type == QUIT:
            fine =True
            pygame.quit()
            sys.exit()
        elif event.type==KEYDOWN:
            if event.key == K_w:
                g.muovi("w")

            elif event.key == K_s:
                g.muovi("s")

            elif event.key == K_a:
                g.muovi("a")

            elif event.key == K_d:
                g.muovi("d")
            disegna_tabella(g.griglia)
    pygame.display.update()