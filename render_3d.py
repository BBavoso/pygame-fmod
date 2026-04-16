from model_loader import load_model
import pygame
from pygame import Vector3, Vector2, Surface
import math

near_clip = 1
far_clip = 1000
line_color = "lawngreen"
line_width = 2


def project(input_in_3d: Vector3) -> Vector2:
    return Vector2(input_in_3d.x / input_in_3d.z, input_in_3d.y / input_in_3d.z)


def draw_3d_line(screen: Surface, start_pos: Vector3, end_pos: Vector3):
    if start_pos.z < near_clip or start_pos.z > far_clip:
        return
    if end_pos.z < near_clip or end_pos.z > far_clip:
        return

    start_pos_2d = project(start_pos)
    end_pos_2d = project(end_pos)

    start_pos_2d.x = ((start_pos_2d.x + 1) / 2) * screen.get_width()
    start_pos_2d.y = (1 - (start_pos_2d.y + 1) / 2) * screen.get_width()

    end_pos_2d.x = ((end_pos_2d.x + 1) / 2) * screen.get_width()
    end_pos_2d.y = (1 - (end_pos_2d.y + 1) / 2) * screen.get_width()

    pygame.draw.line(screen, line_color, start_pos_2d, end_pos_2d, line_width)


class Model:
    def __init__(self, model_obj_path: str, position: Vector3 = Vector3(0, 0, 0)):
        self.vertices, self.edges = load_model(model_obj_path)
        self.position = position

    def draw_wireframe(self, screen: Surface):
        for edge in self.edges:
            start_pos = Vector3(self.vertices[edge[0]]) + self.position
            end_pos = Vector3(self.vertices[edge[1]]) + self.position
            draw_3d_line(screen, start_pos, end_pos)

    def rotate_xz(self, angle_radians):
        s = math.sin(angle_radians)
        c = math.cos(angle_radians)

        for vertex in self.vertices:
            x_prime = vertex[0] * c - vertex[2] * s
            z_prime = vertex[0] * s + vertex[2] * c

            vertex[0] = x_prime
            vertex[2] = z_prime

    def rotate_yz(self, angle_radians):
        s = math.sin(angle_radians)
        c = math.cos(angle_radians)

        for vertex in self.vertices:
            y_prime = vertex[1] * c - vertex[2] * s
            z_prime = vertex[1] * s + vertex[2] * c

            vertex[1] = y_prime
            vertex[2] = z_prime
