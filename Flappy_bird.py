import pygame
import sys

# InicializaÃ§Ã£o do Pygame
pygame.init()

# ConfiguraÃ§Ãµes do jogo
largura_tela = 400
altura_tela = 600
cor_fundo = (255, 255, 255)
cor_passaro = (255, 0, 0)
gravidade = 1
pulo = -15

# ConfiguraÃ§Ã£o do pÃ¡ssaro
passaro_raio = 20
passaro_x = largura_tela // 4
passaro_y = altura_tela // 2
velocidade_y = 0

# ConfiguraÃ§Ã£o dos canos
cano_largura = 50
cano_altura = 300
distancia_canos = 200
cano_velocidade = 5
cano_posicao_x = largura_tela

# ConfiguraÃ§Ã£o da tela
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Flappy Bird")

# FunÃ§Ã£o para desenhar o pÃ¡ssaro na tela
def desenhar_passaro(x, y):
    pygame.draw.circle(tela, cor_passaro, (x, y), passaro_raio)

# FunÃ§Ã£o para desenhar os canos na tela
def desenhar_canos(x, altura_superior, altura_inferior):
    pygame.draw.rect(tela, (0, 128, 0), [x, 0, cano_largura, altura_superior])
    pygame.draw.rect(tela, (0, 128, 0), [x, altura_tela - altura_inferior, cano_largura, altura_inferior])

# Loop principal do jogo
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                velocidade_y = pulo

    # Atualizar posiÃ§Ã£o do pÃ¡ssaro
    passaro_y += velocidade_y
    velocidade_y += gravidade

    # Atualizar posiÃ§Ã£o dos canos
    cano_posicao_x -= cano_velocidade
    if cano_posicao_x < -cano_largura:
        cano_posicao_x = largura_tela
        # Gera novas alturas para os canos
        altura_cano_superior = pygame.time.get_ticks() % 200 + 50
        altura_cano_inferior = altura_tela - altura_cano_superior - distancia_canos

    # Verificar colisÃµes com os canos
    if passaro_x < cano_posicao_x + cano_largura and \
       passaro_x + passaro_raio > cano_posicao_x and \
       (passaro_y - passaro_raio < altura_cano_superior or \
        passaro_y + passaro_raio > altura_tela - altura_cano_inferior):
        pygame.quit()
        sys.exit()

    # Preencher a tela com a cor de fundo
    tela.fill(cor_fundo)

    # Desenhar pÃ¡ssaro e canos
    desenhar_passaro(passaro_x, passaro_y)
    desenhar_canos(cano_posicao_x, altura_cano_superior, altura_cano_inferior)

    # Atualizar a tela
    pygame.display.flip()

    # Controlar a taxa de atualizaÃ§Ã£o
    pygame.time.Clock().tick(30)
