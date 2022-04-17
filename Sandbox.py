from manim import *
import numpy as np
from templ import *

class Lesson(MScene):
    def construct(self):
        #region def
        self.mConfig["subfile"] = open("Subtitles/Sandbox.txt", mode="rt", encoding='utf-8' )
        self.default()
        #endregion

        #region main
        #dSt0
        self.subw(2)
        ax = Axes(
            x_range=[-5, 5, np.pi],
            y_range=[-1, 1, 1],
            y_axis_config={
                "numbers_to_include": np.arange(-1.01, 1.01, 1)
            },
            y_length = 2,
            tips = False
        ).shift(UP*2).scale(0.9)
        ax2 = Axes(
            x_range=[-5, 5, np.pi],
            y_range=[-1, 1, 1],
            y_axis_config={
                "numbers_to_include": np.arange(-1.01, 1.01, 1)
            },
            y_length = 2,
            tips = False
        ).scale(0.9).next_to(ax, DOWN)
        sin = ax.plot(lambda x: np.sin(x), color = YELLOW_A)
        self.dGraph([ax, sin, ax2])
        tirm = ValueTracker(-0.5)
        tarm = ValueTracker(0.5)
        l1 = always_redraw(lambda: ax.get_vertical_line(ax.i2gp(tirm.get_value(), sin), color=BLUE))
        l2 = always_redraw(lambda: ax.get_vertical_line(ax.i2gp(tarm.get_value(), sin), color=BLUE))
        ter = always_redraw(lambda: ax.plot(
            lambda x: np.sin(x), 
            x_range=[tirm.get_value(), tarm.get_value(), .1], 
            color=RED,
            )
        )
        fbox = SurroundingRectangle(ax2, buff=.1)
        self.play(Create(fbox))
        self.dSt()
        self.wait()
        self.play(Uncreate(fbox))
        self.dSt()
        self.dGraph([l1, l2, ter])
        self.wait()
        line1 = ax2.plot(lambda x: 1, color=GREEN, x_range=[-0.5, 0.5, 1])
        self.dSt()
        self.dGraph(line1)
        self.wait()
        self.dSt()
        self.play(tirm.animate.set_value(0.5), tarm.animate.set_value(PI/2))
        #endregion

        #self.outro(VGroup(ax, sin))
        self.wait(5)