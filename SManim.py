from time import time
from manim import *
import numpy as np

class Amogus(Scene):
    def construct(self):
        #region Mobj
        axes = Axes(x_range=[-10, 10, 1], y_range=[-10, 10, 1])
        #endregion

        #region Anim
        self.play(Create(axes))
        self.wait()
        #endregion