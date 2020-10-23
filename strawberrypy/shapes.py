#  ##### BEGIN GPL LICENSE BLOCK #####
# 
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# ##### END GPL LICENSE BLOCK #####

import pygame


class Layer:
    def __init__(self):
        self.shapes = []

    def __repr__(self):
        return f"""StrawberryPy Layer object:
Shapes: {len(self.shapes)}"""

    def Add(self, shape):
        self.shapes.append(shape)

    def Render(self, resolution):
        surface = pygame.Surface(resolution)
        for s in self.shapes:
            s.Draw(surface)

        return surface


class Polygon:
    def __init__(self, verts, color):
        self.type = "POLYGON"
        self.verts = verts
        self.color = color

    def __repr__(self):
        return f"""StrawberryPy Polygon Shape object:
Verts: {self.verts}
Color: {self.color}"""

    def Draw(self, surface):
        pygame.draw.polygon(surface, self.color, self.verts)


class Circle:
    def __init__(self, loc, radius, color):
        self.type = "CIRCLE"
        self.loc = loc
        self.radius = radius
        self.color = color

    def __repr__(self):
        return f"""StrawberryPy Circle Shape object:
Location: {self.loc}
Radius: {self.radius}
Color: {self.color}"""

    def Draw(self, surface):
        pygame.draw.circle(surface, self.color, self.loc, self.radius)