import pygame
import random
import sys

# Inicializa o Pygame
pygame.init()

# Definição de cores
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# Configurações da janela
window_width = 600
window_height = 500
gameDisplay = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Adivinhe o Número')

# Configurações do jogo
clock = pygame.time.Clock()
font_size = 30
font = pygame.font.SysFont(None, font_size)
target_number = 0

# Carregar Imagens
genio = pygame.image.load("genio.png").convert_alpha()

def game_loop():
    global target_number

    # Gera um novo número aleatório
    target_number = random.randint(1, 100)

    guess = None

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and guess is not None:
                    check_guess(guess)
                    guess = None
                elif event.key == pygame.K_BACKSPACE:
                    guess = None
                elif event.key in [pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4,
                                   pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]:
                    if guess is None:
                        guess = int(pygame.key.name(event.key))
                    else:
                        guess = guess * 10 + int(pygame.key.name(event.key))

        # Desenha na tela
        gameDisplay.fill(white)
        display_text(f'Adivinhe o número de 0 a 100', 150, 30)
        display_text(f'Seu palpite: {guess if guess is not None else ""}', 230, 60)

        # Posiciona a imagem do gênio abaixo de tudo e centralizado
        genio_rect = genio.get_rect()
        genio_rect.center = (window_width // 2, window_height - genio_rect.height // 2)
        gameDisplay.blit(genio, genio_rect)

        pygame.display.update()
        clock.tick(30)

def display_text(text, x, y, color=black):
    text_surface = font.render(text, True, color)
    gameDisplay.blit(text_surface, (x, y))

def check_guess(guess):
    global target_number

    if guess == target_number:
        display_text(f'Parabéns! Você acertou. O próximo número foi gerado.', 30, 90, green)
        pygame.display.update()
        pygame.time.wait(2000)
        target_number = random.randint(1, 100)
    elif guess < target_number:
        display_text('O número é maior. Tente novamente.', 120, 90, red)
    elif guess > target_number:
        display_text('O número é menor. Tente novamente.', 120, 90, red)

    pygame.display.update()
    pygame.time.wait(2000)

# Inicia o loop do jogo
game_loop()
