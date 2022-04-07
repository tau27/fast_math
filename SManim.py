from cmath import pi
from time import time
from manim import *
import numpy as np

class Amogus(Scene):
    def dr(self, ref):
        for i in ref:
            self.play(Create(i), run_time=1)
    def construct(self):
        #region Mobj
        ax = Axes(
            x_range=[0, 5],
            y_range=[0, 6],
            x_axis_config={"numbers_to_include": [1, 3]},
            tips=False,
        )
        curve_1 = ax.plot(lambda x: 4 - (x - 2)**2, x_range=[0, 4], color=BLUE_C)
        line1 = ax.get_vertical_line(ax.i2gp(1, curve_1), color=YELLOW)
        line2 = ax.get_vertical_line(ax.i2gp(3, curve_1), color=YELLOW)
        area1 = ax.get_riemann_rectangles(
            curve_1, x_range=[1, 3], dx=0.2, stroke_width=0.1, stroke_color=WHITE
        )
        area2 = ax.get_area(x_range=[1, 3], graph=curve_1)
        s = MathTex("S").align_to(area2)

        scen = VGroup(line1, line2)
        graphs = [curve_1, scen, area1, s]
        #endregion

        #region Anim
        self.play(Create(ax))
        self.dr(graphs)
        self.wait()
        self.play(Transform(area1, area2))
        self.wait()
        #endregion