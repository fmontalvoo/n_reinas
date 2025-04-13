import pygame
from n_reinas import NReinas


class Tablero:
    def __init__(self, ancho=800, alto=700, n=8):
        self.ancho = ancho
        self.alto = alto
        self.n = n
        self.n_reinas = NReinas(n)
        self.negro = (0, 0, 0)
        self.blanco = (255, 255, 255)
        self.reina = None
        self.pantalla = None
        self.juego_terminado = False
        self.reloj = None

    def inicializar(self):
        pygame.init()
        self.pantalla = pygame.display.set_mode((self.ancho, self.alto), pygame.RESIZABLE)
        pygame.display.set_caption("Tablero de N Reinas")
        self.reina = pygame.image.load('src/reina.png')
        self.reloj = pygame.time.Clock()

    def calcular_dimensiones(self):
        # Usar el tamaño completo de la ventana para el tablero
        return self.ancho / self.n, self.alto / self.n

    def dibujar_tablero(self):
        ancho_cuadro, alto_cuadro = self.calcular_dimensiones()
        self.pantalla.fill(self.blanco)
        color = 0
        for i in range(self.n):
            for j in range(self.n):
                x = i * ancho_cuadro
                y = j * alto_cuadro
                if color % 2 == 0:
                    pygame.draw.rect(
                        self.pantalla,
                        self.negro,
                        [x, y, ancho_cuadro + 1, alto_cuadro + 1],  # +1 para evitar espacios
                        0
                    )
                color += 1
            if self.n % 2 == 0:
                color += 1

        # Dibujar reinas
        tamano_reina = min(ancho_cuadro, alto_cuadro) * 0.8
        reina_escalada = pygame.transform.scale(
            self.reina, (int(tamano_reina), int(tamano_reina))
        )
        for row, col in self.n_reinas.soluciones:
            pos_y = row * alto_cuadro + (alto_cuadro - reina_escalada.get_height()) / 2
            pos_x = col * ancho_cuadro + (ancho_cuadro - reina_escalada.get_width()) / 2
            self.pantalla.blit(reina_escalada, (pos_x, pos_y))

    def ejecutar(self):
        self.inicializar()
        while not self.juego_terminado:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.juego_terminado = True
                elif evento.type == pygame.VIDEORESIZE:
                    self.ancho, self.alto = evento.size
                    self.pantalla = pygame.display.set_mode(
                        (self.ancho, self.alto), pygame.RESIZABLE
                    )

            self.dibujar_tablero()
            pygame.display.flip()
            self.reloj.tick(60)

        pygame.quit()