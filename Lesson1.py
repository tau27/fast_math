from manim import *
import numpy as np
from Templ import *

class Lesson(MScene):
    def construct(self):
        self.default(file=__file__, type="y")


        #region Car
        #dSt16
        def func(x):
            e = x + np.sin(x)
            return e
        self.dSt()#2
        ax = self.defgraph()
        graph = ax.plot(func, color = BLUE)
        gbuf = ax.plot(lambda x: x, color = BLUE)
        labels = ax.get_axis_labels()
        self.dGraph([ax, gbuf, labels])
        self.dSt()#3
        self.wait(WAITT)
        self.play(ReplacementTransform(gbuf, graph))
        self.subw(2)#4-5
        #speed = MathTex("S = ?").to_edge(DR).scale(0.9).shift((DOWN + LEFT) * 0.5)
        #self.play(Write(speed))

        dx = ValueTracker(1)
        x = ValueTracker(5)

        slope = always_redraw(lambda: ax.get_secant_slope_group(
            x = x.get_value(),
            dx = dx.get_value(),
            graph=graph,
            dx_label="dx",
            dy_label="dy",
            dx_line_color=GREEN_B,
            secant_line_length=11,
            secant_line_color=RED_D,
            )
        )

        self.play(Create(slope))
        self.subw(4, "note")#6-9
        self.subw(2)#10-11
        #self.play(Transform(speed, MathTex("\\frac{dy}{dx} = ?").to_edge(DR).scale(0.9).shift((DOWN + LEFT) * 0.5)))
        self.dSt()#12
        line = Line(start=ax.c2p(0, 0, 0), end=ax.c2p(10, 0, 0), color = RED)
        an = always_redraw(lambda: Angle(line, slope[4]))
        tex = always_redraw(lambda: DecimalNumber(Angle(
                line, slope[4]).get_value(), font_size=30).move_to(
            Angle(
                line, slope[4], radius=0.5 + 3 * SMALL_BUFF, other_angle=False
            ).point_from_proportion(0.5)
        )
        )
        self.play(Create(an))
        self.play(Write(tex))
        self.play(x.animate.set_value(4))
        self.wait()
        self.play(x.animate.set_value(6))
        self.wait()
        self.play(x.animate.set_value(5))
        self.wait()
        self.dSt()#13
        self.play(dx.animate.set_value(0.5))
        self.wait()
        self.play(dx.animate.set_value(0.1))
        self.subw(4)#14-17
        #self.play(Transform(speed, MathTex("\\frac{dy}{dx} = 6").to_edge(DR).scale(0.9).shift((DOWN + LEFT) * 0.5)))
        self.subw(3, "note")
        self.subw(3)#17-20
        #endregion
        
        self.outro(VGroup(slope, ax, graph, labels, an, tex))
        self.wait()
