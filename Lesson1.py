from manim import *
import numpy as np
from templ import *

class Lesson(MScene):
    def construct(self):
        self.mConfig["subfile"] = open("Subtitles/Lesson1.txt", mode="rt", encoding='utf-8' )
        self.default()


        #region Car
        #dSt16
        def func(x):
            e = x + np.sin(x)
            return e
        self.dSt()
        ax = self.defgraph()
        graph = ax.plot(func, color = BLUE)
        gbuf = ax.plot(lambda x: x, color = BLUE)
        labels = ax.get_axis_labels()
        self.dGraph([ax, gbuf, labels])
        self.dSt()
        self.wait()
        self.play(ReplacementTransform(gbuf, graph))
        self.dSt()
        self.wait()
        self.dSt()

        dx = ValueTracker(1)
        x = ValueTracker(5)

        slope = always_redraw(lambda: ax.get_secant_slope_group(
            x = x.get_value(),
            dx = dx.get_value(),
            graph=graph,
            dx_label="dx",
            dy_label="dy",
            dx_line_color=GREEN_B,
            secant_line_length=10,
            secant_line_color=RED_D,
            )
        )

        self.play(Create(slope))
        self.subw(7)
        self.play(x.animate.set_value(3))
        self.wait()
        self.play(x.animate.set_value(6))
        self.wait()
        self.play(x.animate.set_value(5))
        self.wait()
        self.dSt()
        self.play(dx.animate.set_value(0.5))
        self.wait()
        self.play(dx.animate.set_value(0.1))
        self.subw(4)
        #endregion
        
        self.outro(VGroup(slope, ax, graph, labels))
        self.wait()