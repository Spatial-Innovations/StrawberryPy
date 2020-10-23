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

from . import export

class Engine:
    def __init__(self, resolution, fps):
        """
        Initializes engine.
        :param resolution: Reesolution (x, y) pixels of final video.
        :param fps: Frames per second of final video.
        """
        self.res = resolution
        self.fps = fps

    def Export(self, path):
        """
        Exports into a video file.
        :param path: Path (with extension, like .mp4) of final video.
        """
        export.Export(self, path)