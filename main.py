import pygame
import sys
import math
import random

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
width, height = 500, 500
screen = pygame.display.set_mode((width, height))
font= pygame.font.SysFont("Consolas",20)
font2= pygame.font.SysFont("Consolas",10)
pygame.display.set_caption("Dance ball")

# Cargar el ícono
icon = pygame.image.load('icono.png')
pygame.display.set_icon(icon)
# Colores
white = (255, 255, 255)
black = (0, 0, 0)
gray = (100, 100, 100)
red = (255,0,0)
green = (0,255,0)

#pantallas
play=True
intro=True
game=False
end=False
win=False
while play:
    # Parámetros iniciales
    speed=3
    colision=0
    health=300
    circle_radius = 150
    ball_radius = 5
    radius=5
    speedP = 0
    speedE = 5
    posx,posy=width/2,height/2
    angleP=0
    angleE=0
    direction=True
    points= 0
    movement=0
    clock = pygame.time.Clock()

    while intro:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        # Dibujar fondo
        screen.fill(black)

        # Texto titulo
        text=font.render("Dance ball",1,white)
        screen.blit(text, (width/2-(text.get_width()//2), height/4.4))

        # Texto Instrucciones
        text=font.render("Tutorial",1,white)
        screen.blit(text, (width/2-(text.get_width()//2), 300))

        # Texto velocidad
        text=font2.render("Utiliza las teclas de izquierda y derecha para modificar la velocidad de la pelota",1,white)
        screen.blit(text, (width/2-(text.get_width()//2), 330))

        # Texto tamaño
        text=font2.render("Utiliza las teclas de arriba y abajo para modificar el de la pelota",1,white)
        screen.blit(text, (width/2-(text.get_width()//2), 350))

        # Texto tamaño 2
        text=font2.render("esto te dara mas puntos pero tambien será mas dificil",1,white)
        screen.blit(text, (width/2-(text.get_width()//2), 360))

        # Texto Iniciar
        text=font.render("Presiona 'Enter' para empezar",1,white)
        screen.blit(text, (width/2-(text.get_width()//2), 400))

        # Texto esquivar
        text=font2.render("Esquiva la pelota roja para acumular puntos",1,white)
        screen.blit(text, (width/2-(text.get_width()//2), 430))

        # Texto puntos
        text=font2.render("Consigue 1000 puntos para ganar",1,white)
        screen.blit(text, (width/2-(text.get_width()//2), 450))
        # Dibujar circulo
        pygame.draw.circle(screen, white, (width/2, height/4), 100, 4)

        # Actualizar posición de la pelota en movimiento circular
        x = int(width/2 + 100 * math.cos(math.radians(angleP)))
        y = int(height/4 + 100 * math.sin(math.radians(angleP)))

        # Dibujar pelota
        pygame.draw.circle(screen, white, (x, y), radius)    

        # Actualizar ángulo para el próximo fotograma
        angleP += speed

        # Manejar entrada del teclado
        keys = pygame.key.get_pressed()
        # Modificar Velocidad
        if keys[pygame.K_LEFT]:
            if speed==1:
                speed-=2
            elif speed>-5:
                speed -= 1
        if keys[pygame.K_RIGHT]:
            if speed==-1:
                speed+=2
            elif speed<5:
                speed += 1
        # Modificar Tamaño
        if keys[pygame.K_UP]:
            if radius<10:
                radius += 1
        if keys[pygame.K_DOWN]:
            if radius>5:
                radius -= 1
        # Empezar juego
        if keys[pygame.K_RETURN]:
            angleP=0
            intro=False
            game=True

        pygame.display.flip()

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Actualizar posición de la pelota en movimiento circular
        x = int(width/2 + circle_radius * math.cos(math.radians(angleP)))
        y = int(height/2 + circle_radius * math.sin(math.radians(angleP)))

        # Actualizar posición de el enemigo
        posx = int(width/2 + movement * math.cos(math.radians(angleE)))
        posy = int(height/2 + movement * math.sin(math.radians(angleE)))

        # Dibujar fondo
        screen.fill(black)

        #hitbox pelota
        hitboxP=(x-6-ball_radius+4,y-6-ball_radius+4,12+ball_radius,12+ball_radius)

        # Dibujar pelota
        pygame.draw.circle(screen, white, (x, y), ball_radius)

        #hitbox enemigo
        hitboxE=(posx-6-ball_radius+4,posy-6-ball_radius+4,12+ball_radius,12+ball_radius)

        # Dibujar Enemigo
        pygame.draw.circle(screen, red, (posx, posy),ball_radius)

        # Dibujar círculo
        pygame.draw.circle(screen, white, (width/2, height/2), circle_radius, 4)

        # Manejar entrada del teclado
        keys = pygame.key.get_pressed()
        # Modificar Velocidad
        if keys[pygame.K_LEFT]:
            if speedP==1:
                speedP-=2
            elif speedP>-5:
                speedP -= 1
        if keys[pygame.K_RIGHT]:
            if speedP==-1:
                speedP+=2
            elif speedP<5:
                speedP += 1
        # Modificar Tamaño
        if keys[pygame.K_UP]:
            if ball_radius<10:
                ball_radius += 1
        if keys[pygame.K_DOWN]:
            if ball_radius>5:
                ball_radius -= 1

        # texto puntuacion
        text_surface = font.render(f"{points}", True, white)
        screen.blit(text_surface, (width/2.2, 50))

        # Dibujar vida
        pygame.draw.rect(screen,white,(100,450,(health),30))
        
        # Actualizar ángulo para el próximo fotograma
        angleP += speedP

        #Colisiones
        if (hitboxP[0]+hitboxP[2]>hitboxE[0]) and (hitboxP[0]<hitboxE[0]+hitboxE[2]) and (hitboxP[1]<hitboxE[1]+hitboxE[3]) and (hitboxP[1]+hitboxP[3]>hitboxE[1]):
            health-=20
        
        # Actualizar velocidad
        if points%100==0:
            speedE+=3

        # Actualizar puntuacion
        if points<1000:
            points+=1

        # Actualizar linea
        if direction==True:
            movement+=abs(speedE)
            if movement>=circle_radius:
                direction=False
        else:
            movement-=abs(speedE)
            if movement<0:
                angleE=random.randint(angleP-30,angleP+30)
                direction=True

        # Muerte
        if health<=0:
            game=False
            end=True
        pygame.display.flip()

        #victoria
        if points>=1000:
            game=False
            win=True
        # Limitar la velocidad de fotogramas
        clock.tick(30)

    while end:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        # Dibujar fondo
        screen.fill(black)

        # Texto game over
        text=font.render("Has perdido",1,white)
        screen.blit(text, (width/2-(text.get_width()//2), 100))

        # Texto puntuacion
        text=font.render(f"Puntuacion final: {points}",1,white)
        screen.blit(text, (width/2-(text.get_width()//2), 250))

        # Texto reintentar
        text=font.render(f"Para reintentar pulsa 'R'",1,white)
        screen.blit(text, (width/2-(text.get_width()//2), 350))

        # Texto salir
        text=font.render(f"Para salir pulsa 'Esc'",1,white)
        screen.blit(text, (width/2-(text.get_width()//2), 400))

        # Manejar entrada del teclado
        keys = pygame.key.get_pressed()
        # Repetir juego
        if keys[pygame.K_r]:
            points=0
            game=True
            intro=False
            end=False
        # Salir del juego
        elif keys[pygame.K_ESCAPE]:
            intro=False
            game=False
            end=False
            play=False
        pygame.display.flip()

    while win:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        # Dibujar fondo
        screen.fill(black)    
        
        # Texto win
        text=font.render("Felicidades, Has ganado",1,white)
        screen.blit(text, (width/2-(text.get_width()//2), 100))

        # Texto puntuacion
        text=font.render(f"Puntuacion final: {points}",1,white)
        screen.blit(text, (width/2-(text.get_width()//2), 250))

        # Texto reintentar
        text=font.render(f"Para volver a jugar pulsa 'R'",1,white)
        screen.blit(text, (width/2-(text.get_width()//2), 350))

        # Texto salir
        text=font.render(f"Para salir pulsa 'Esc'",1,white)
        screen.blit(text, (width/2-(text.get_width()//2), 400))

        # Manejar entrada del teclado
        keys = pygame.key.get_pressed()
        # Repetir juego
        if keys[pygame.K_r]:
            points=0
            game=True
            win=False
            intro=False
            end=False
        # Salir del juego
        elif keys[pygame.K_ESCAPE]:
            win=False
            intro=False
            game=False
            end=False
            play=False
        
        pygame.display.flip()