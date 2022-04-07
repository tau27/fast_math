from manim import *
import numpy as np
from Templ import *

class Lesson(MScene):
    def construct(self):
            self.dCoords()
            line = Line(start=np.array([0,0,0]))
            
            #region Animate
            self.play(Create(line))
            self.wait()
            #endregion