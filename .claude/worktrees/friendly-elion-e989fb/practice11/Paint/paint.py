import math
import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600
FPS = 60
BACKGROUND_COLOR = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Practice 11 - Paint")
clock = pygame.time.Clock()

font_ui = pygame.font.SysFont("Verdana", 20)
font_small = pygame.font.SysFont("Verdana", 16)

BLACK   = (0, 0, 0)
WHITE   = (255, 255, 255)
GRAY    = (160, 160, 160)
RED     = (255, 0, 0)
GREEN   = (0, 180, 0)
BLUE    = (0, 0, 255)
YELLOW  = (255, 255, 0)
ORANGE  = (255, 165, 0)
PURPLE  = (128, 0, 128)
PINK    = (255, 105, 180)
BROWN   = (139, 69, 19)

color_map = {
    pygame.K_0: BLACK,
    pygame.K_1: RED,
    pygame.K_2: GREEN,
    pygame.K_3: BLUE,
    pygame.K_4: YELLOW,
    pygame.K_5: ORANGE,
    pygame.K_6: PURPLE,
    pygame.K_7: PINK,
    pygame.K_8: BROWN,
    pygame.K_9: GRAY,
}

color_name_map = {
    pygame.K_0: "BLACK",
    pygame.K_1: "RED",
    pygame.K_2: "GREEN",
    pygame.K_3: "BLUE",
    pygame.K_4: "YELLOW",
    pygame.K_5: "ORANGE",
    pygame.K_6: "PURPLE",
    pygame.K_7: "PINK",
    pygame.K_8: "BROWN",
    pygame.K_9: "GRAY",
}

tool = "pen"
current_color = BLACK
current_color_name = "BLACK"
thickness = 4

drawing = False
start_pos = None
prev_pos = None
current_pos = None

base_layer = pygame.Surface((WIDTH, HEIGHT))
base_layer.fill(BACKGROUND_COLOR)

print("--- Instructions ---")
print("W - Pen")
print("R - Rectangle")
print("S - Square")
print("C - Circle")
print("T - Right triangle")
print("F - Equilateral triangle")
print("D - Rhombus")
print("E - Eraser")
print("+ - Increase thickness")
print("- - Decrease thickness")
print("SPACE - Clear canvas")
print("------ Colors ------")
print("0 - Black")
print("1 - Red")
print("2 - Green")
print("3 - Blue")
print("4 - Yellow")
print("5 - Orange")
print("6 - Purple")
print("7 - Pink")
print("8 - Brown")
print("9 - Gray")
print("-------------------")


def calculate_rect(start, end):
    x1, y1 = start
    x2, y2 = end

    left = min(x1, x2)
    top = min(y1, y2)
    width = abs(x2 - x1)
    height = abs(y2 - y1)

    return pygame.Rect(left, top, width, height)


def calculate_square(start, end):
    x1, y1 = start
    x2, y2 = end

    size = min(abs(x2 - x1), abs(y2 - y1))

    left = x1 - size if x2 < x1 else x1
    top = y1 - size if y2 < y1 else y1

    return pygame.Rect(left, top, size, size)


def draw_circle_by_points(surface, color, start, end, width=0):
    cx, cy = start
    ex, ey = end

    radius = int(math.hypot(ex - cx, ey - cy))

    if radius > 0:
        pygame.draw.circle(surface, color, (cx, cy), radius, width)


def draw_right_triangle(surface, color, start, end, width):
    x1, y1 = start
    x2, y2 = end

    points = [(x1, y1), (x2, y1), (x1, y2)]
    pygame.draw.polygon(surface, color, points, width)


def draw_equilateral_triangle(surface, color, start, end, width):
    x1, y1 = start
    x2, y2 = end

    side = abs(x2 - x1)
    height = int(side * math.sqrt(3) / 2)

    if y2 < y1:
        height = -height

    points = [
        (x1, y1),
        (x1 - side // 2, y1 + height),
        (x1 + side // 2, y1 + height),
    ]
    pygame.draw.polygon(surface, color, points, width)


def draw_rhombus(surface, color, start, end, width):
    x1, y1 = start
    x2, y2 = end

    center_x = (x1 + x2) // 2
    center_y = (y1 + y2) // 2
    half_width = abs(x2 - x1) // 2
    half_height = abs(y2 - y1) // 2

    points = [
        (center_x, center_y - half_height),
        (center_x + half_width, center_y),
        (center_x, center_y + half_height),
        (center_x - half_width, center_y),
    ]
    pygame.draw.polygon(surface, color, points, width)


def get_draw_color():
    if tool == "eraser":
        return BACKGROUND_COLOR
    return current_color


def draw_ui():
    panel_rect = pygame.Rect(WIDTH - 240, 10, 220, 120)
    pygame.draw.rect(screen, (235, 235, 235), panel_rect)
    pygame.draw.rect(screen, BLACK, panel_rect, 2)

    tool_text = font_ui.render(f"Tool: {tool.upper()}", True, BLACK)
    screen.blit(tool_text, (WIDTH - 225, 20))

    thick_text = font_ui.render(f"Thickness: {thickness}", True, BLACK)
    screen.blit(thick_text, (WIDTH - 225, 50))

    color_text = font_ui.render(f"Color: {current_color_name}", True, BLACK)
    screen.blit(color_text, (WIDTH - 225, 80))

    outer_rect = pygame.Rect(WIDTH - 70, 78, 40, 40)
    inner_rect = pygame.Rect(WIDTH - 65, 83, 30, 30)
    pygame.draw.rect(screen, GRAY, outer_rect)
    pygame.draw.rect(screen, current_color, inner_rect)


SHAPE_TOOLS = ("rect", "square", "circle", "right_triangle", "equilateral_triangle", "rhombus")


def render_shape(surface, draw_color):
    if tool == "rect":
        rect = calculate_rect(start_pos, current_pos)
        pygame.draw.rect(surface, draw_color, rect, thickness)

    elif tool == "square":
        rect = calculate_square(start_pos, current_pos)
        pygame.draw.rect(surface, draw_color, rect, thickness)

    elif tool == "circle":
        draw_circle_by_points(surface, draw_color, start_pos, current_pos, thickness)

    elif tool == "right_triangle":
        draw_right_triangle(surface, draw_color, start_pos, current_pos, thickness)

    elif tool == "equilateral_triangle":
        draw_equilateral_triangle(surface, draw_color, start_pos, current_pos, thickness)

    elif tool == "rhombus":
        draw_rhombus(surface, draw_color, start_pos, current_pos, thickness)


def finalize_shape():
    if start_pos and current_pos:
        render_shape(base_layer, get_draw_color())


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                tool = "pen"
            elif event.key == pygame.K_r:
                tool = "rect"
            elif event.key == pygame.K_c:
                tool = "circle"
            elif event.key == pygame.K_e:
                tool = "eraser"
            elif event.key == pygame.K_s:
                tool = "square"
            elif event.key == pygame.K_t:
                tool = "right_triangle"
            elif event.key == pygame.K_f:
                tool = "equilateral_triangle"
            elif event.key == pygame.K_d:
                tool = "rhombus"

            elif event.key in (pygame.K_PLUS, pygame.K_EQUALS):
                thickness += 1
            elif event.key == pygame.K_MINUS:
                if thickness > 1:
                    thickness -= 1
            elif event.key == pygame.K_SPACE:
                base_layer.fill(BACKGROUND_COLOR)
            elif event.key in color_map:
                current_color = color_map[event.key]
                current_color_name = color_name_map[event.key]

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                drawing = True
                start_pos = event.pos
                prev_pos = event.pos
                current_pos = event.pos

                if tool in ("pen", "eraser"):
                    pygame.draw.circle(base_layer, get_draw_color(), event.pos, max(1, thickness // 2))

        elif event.type == pygame.MOUSEMOTION:
            if drawing:
                current_pos = event.pos

                if tool in ("pen", "eraser"):
                    pygame.draw.line(base_layer, get_draw_color(), prev_pos, current_pos, thickness)
                    prev_pos = current_pos

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                if drawing:
                    current_pos = event.pos

                    if tool in SHAPE_TOOLS:
                        finalize_shape()

                drawing = False
                start_pos = None
                prev_pos = None
                current_pos = None

    screen.blit(base_layer, (0, 0))

    if drawing and tool in SHAPE_TOOLS and start_pos and current_pos:
        render_shape(screen, get_draw_color())

    draw_ui()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
