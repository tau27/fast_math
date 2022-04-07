from manim import *
import numpy as np

class MScene(Scene):
    def dGraph(self, obj):
        for i in obj:
            self.play(Create(i), run_time=1)
    def dCoords(self, sx=-9, ex=8, sy=-4, ey=5):
        for x in range(sx, ex):
            for y in range(sy, ey):
                self.add(Dot(np.array([x, y, 0]), color=DARK_GREY))