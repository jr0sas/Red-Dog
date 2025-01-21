import pygame
import sys
import os
sys.path.append(os.path.dirname(__file__))
#from Logica_juego import crear_baraja, repartir_cartas, calcular_spread


pygame.init()

# dimension de la pantalla
SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Red Dog Game")

#colores  
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 180, 0)
RED = (180, 0, 0)
GRAY = (169, 169, 169)
BLUE = (0, 0, 180)
p_color = (132, 227, 244)

#cargo las imagenes
background_main = pygame.image.load("Assets/imagen_principal.PNG")
background_main = pygame.transform.scale(background_main, (SCREEN_WIDTH, SCREEN_HEIGHT))
background_game = pygame.image.load("Assets/mesa_fondo.PNG")

background_game = pygame.transform.scale(background_game, (SCREEN_WIDTH, SCREEN_HEIGHT))
#fuente de texto
font = pygame.font.Font(None, 50)

#funcion para mostrar texto
def draw_text(text, x, y, color=WHITE):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

#funcion para crear un boton
def draw_button(text, x, y, width, height, color, text_color):
    button_rect = pygame.Rect(x, y, width, height)
    pygame.draw.rect(screen, color, button_rect, border_radius=30)
    pygame.draw.rect(screen, WHITE, button_rect, 4, border_radius=30)
    draw_text(text, x + width // 3.75, y + height // 4.6, text_color)
    return button_rect

#bara de carga
def draw_loading_bar(progress, x, y, width, height):
    pygame.draw.rect(screen, GRAY, (x, y, width, height))  #fondo
    pygame.draw.rect(screen, RED, (x, y, int(width * progress), height))  #barra de progreso
    pygame.draw.rect(screen, BLACK, (x, y, width, height), 3)  #borde

#dibujar las posiciones de las cartas en la mesa
def draw_card_positions():
    #posiciones de las cartas
    card_width, card_height = 100, 150
    gap = 20  #espacio entre cartas
    start_x = SCREEN_WIDTH // 2 - (3 * card_width + 2 * gap) // 2  #centrado
    start_y = SCREEN_HEIGHT // 2 - card_height // 2

    for i in range(3): #dibujamos 3 posiciones
        x = start_x + i * (card_width + gap)
        y = start_y
        pygame.draw.rect(screen, p_color, (x, y, card_width, card_height), 5,border_radius=30)  # Bordes 

# Función para dibujar el mazo de cartas
def draw_deck():
    deck_x = SCREEN_WIDTH // 4  # Posición del mazo
    deck_y = SCREEN_HEIGHT // 2 - 75
    deck_width, deck_height = 100, 150
    pygame.draw.rect(screen, p_color, (deck_x, deck_y, deck_width, deck_height), 5, border_radius = 30)  # Borde del mazo
    draw_text("Mazo", deck_x + 5, deck_y + 55, RED)  # Etiqueta para el mazo
    

ruta_imagen = "Assets/packcartas/Back_Red_1.png"

def draw_card_deck(ruta_imagen="Assets/packcartas/Back_Red_1.png",x=320,y=285, w=100, h=150):
    
    # Cargar la imagen del mazo
    deck_image = pygame.image.load(ruta_imagen)
    deck_image = pygame.transform.scale(deck_image, (w,h))  # Escalar la imagen al tamaño deseado

    # Dibujar la imagen en la pantalla
    screen.blit(deck_image, (x, y))
    
def loading_screen():
    clock = pygame.time.Clock()
    progress = 0

    while progress < 1:
        screen.blit(background_main, (0, 0))  # Fondo de la pantalla principal
        draw_text("Cargando...", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 1.1 - 50)
        draw_loading_bar(progress, SCREEN_WIDTH // 4, SCREEN_HEIGHT // 1.15 + 20, SCREEN_WIDTH // 2, 30)
        progress += 0.01  # Incremento de la barra de carga

        pygame.display.flip()
        clock.tick(60)

# Pantalla de juego
def game_screen():
    clock = pygame.time.Clock()
    running = True

    while running:
        screen.blit(background_game, (0, 0))  # Fondo de la mesa de juego

        # Dibujar posiciones de cartas y mazo
        draw_card_positions()
        draw_deck()
        draw_card_deck()

        # Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.flip()
        clock.tick(60)

# Menú principal
def main_menu():
    clock = pygame.time.Clock()
    running = True

    while running:
        screen.blit(background_main, (0, 0))  # Fondo de la pantalla principal

        # Dibujar botones
        play_button = draw_button("Jugar", SCREEN_WIDTH // 2.55 - 100, SCREEN_HEIGHT // 2 + 80, 210, 62, BLACK, GREEN)
        quit_button = draw_button(" Salir", SCREEN_WIDTH // 1.75 - 100, SCREEN_HEIGHT // 2 + 80, 210, 62, BLACK, RED)

        # Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.collidepoint(event.pos):
                    #loading_screen()
                    game_screen()  # Cambiar a la pantalla del juego
                if quit_button.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()
        clock.tick(60)

# Programa principal
def main():
    main_menu()

if __name__ == "__main__":
    main()
