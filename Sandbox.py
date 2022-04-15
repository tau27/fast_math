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
        l1 = ax.get_vertical_line(ax.i2gp(-1, sin), color=BLUE)
        l2 = ax.get_vertical_line(ax.i2gp(1, sin), color=BLUE)
        tirm = ValueTracker(-1)
        tarm = ValueTracker(1)
        ter = always_redraw(lambda: ax.plot(lambda x: np.sin(x), x_range=np.array[tirm.get_value(), tarm.get_value(), 0], color=RED,))
        self.play(Create(VGroup(l1, l2, ter)))

        #endregion

        #self.outro(VGroup(ax, sin))
        self.wait()