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

import os
import numpy
from PIL import Image

def Export(data, path):
    PARENT = os.path.dirname(__file__)
    tmpDir = os.path.join(PARENT, "tmp")
    os.makedirs(tmpDir, exist_ok=True)

    for i, frame in enumerate(data.Render()):
        pixels = numpy.array(frame, dtype=numpy.uint8)
        Image.fromarray(pixels).save(os.path.join(PARENT, "tmp", f"{i}.jpg"))