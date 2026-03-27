import glfw
from OpenGL.GL import *
import math
import numpy as np

# Vértices base 
p1 = np.array([-0.1, -0.1, 1.0])
p2 = np.array([0.1, -0.1, 1.0])
p3 = np.array([0.0, 0.1, 1.0])

def get_rotation_matrix(theta):
    c, s = math.cos(theta), math.sin(theta)
    return np.array([[c, -s, 0], [s, c, 0], [0, 0, 1]])

def get_translation_matrix(dx, dy):
    return np.array([[1, 0, dx], [0, 1, dy], [0, 0, 1]])

def get_scale_matrix(sx, sy):
    return np.array([[sx, 0, 0], [0, sy, 0], [0, 0, 1]])

def desenhar_triangulo(matriz, cor):
    """Aplica a matriz nos vértices e desenha o triângulo com a cor escolhida."""
    tp1 = matriz @ p1
    tp2 = matriz @ p2
    tp3 = matriz @ p3

    glColor3f(cor[0], cor[1], cor[2])
    glBegin(GL_POINTS)
    t = 0.0
    while t <= 1.0:
        glVertex2f(tp1[0] + (tp2[0] - tp1[0]) * t, tp1[1] + (tp2[1] - tp1[1]) * t)
        glVertex2f(tp2[0] + (tp3[0] - tp2[0]) * t, tp2[1] + (tp3[1] - tp2[1]) * t)
        glVertex2f(tp3[0] + (tp1[0] - tp3[0]) * t, tp3[1] + (tp1[1] - tp3[1]) * t)
        t += 0.01
    glEnd()

def render():
    glClear(GL_COLOR_BUFFER_BIT)
    glPointSize(3)

    # 1. Triângulo MAIOR (Escala 3.0)
    # Posicionado um pouco à esquerda
    m_maior = get_translation_matrix(-0.5, 0.5) @ get_scale_matrix(3.0, 3.0)
    desenhar_triangulo(m_maior, (0, 0, 1)) # Azul

    # 2. Triângulo MENOR (Escala 0.5)
    # Posicionado um pouco abaixo
    m_menor = get_translation_matrix(0.0, -0.5) @ get_scale_matrix(0.5, 0.5)
    desenhar_triangulo(m_menor, (1, 0, 0)) # Vermelho

    # 3. Triângulo DE PONTA CABEÇA (Rotação 180 graus ou PI)
    # No centro da tela
    m_invertido = get_rotation_matrix(math.pi)
    desenhar_triangulo(m_invertido, (0, 1, 0)) # Verde

    # 4. Triângulo DO OUTRO LADO (Translação para a direita)
    m_outro_lado = get_translation_matrix(0.7, 0.0)
    desenhar_triangulo(m_outro_lado, (0, 0, 0)) # Preto

def main():
    if not glfw.init(): return
    window = glfw.create_window(800, 600, "Transformações Estáticas", None, None)
    glfw.make_context_current(window)
    glClearColor(1, 1, 1, 1)
    
    while not glfw.window_should_close(window):
        glfw.poll_events()
        render()
        glfw.swap_buffers(window)
    glfw.terminate()

if __name__ == "__main__":
    main()