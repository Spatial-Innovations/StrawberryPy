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
import shutil
import numpy
import cv2
from PIL import Image

class Engine:
    def __init__(self, resolution, fps):
        """
        Initializes engine.
        :param resolution: Reesolution (x, y) pixels of final video.
        :param fps: Frames per second of final video.
        """
        self.res = resolution
        self.fps = fps
        self.layers = []

    def Export(self, path):
        """
        Exports into a video file.
        :param path: Path (with extension, like .mp4) of final video.
        """
        # Initialize directory
        PARENT = os.path.dirname(__file__)
        tmpDir = os.path.join(PARENT, "tmp")
        os.makedirs(tmpDir, exist_ok=True)

        # Save images to frames
        for i, frame in enumerate(self.Render()):
            pixels = numpy.array(frame, dtype=numpy.uint8)
            Image.fromarray(pixels).save(os.path.join(PARENT, "tmp", f"{i}.jpg"))

        # Compile into video
        images = [img for img in os.listdir(tmpDir)]
        frame = cv2.imread(os.path.join(tmpDir, images[0]))
        height, width, layers = frame.shape
        video = cv2.VideoWriter(path, 0, self.fps, (width, height))
        for img in images:
            video.write(cv2.imread(os.path.join(tmpDir, img)))

        video.release()

        # Clean up
        cv2.destroyAllWindows()
        shutil.rmtree(tmpDir)

    def AddLayer(self, layer):
        self.layers.append(layer)