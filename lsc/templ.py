from math import sin
from emanim import *

class Template(EScene):
    def construct(self):
        ax = Axes(
            x_range=[0, 20, 1],
            y_range=[0, 20, 1],
            axis_config={"color": GREEN},
            tips=False
        ).shift(UP*.75+LEFT*.5)
        labels = ax.get_axis_labels(x_label="x", y_label="f(x)")

        x11 = ax.plot(lambda x: x+sin(x)*3, color=BLUE, x_range=[0, 20.0, 0.01],)
        t_label = ax.get_T_label(x_val=8, graph=x11, label=MathTex("x_0"), triangle_size=0)
        pnt = [ax.i2gp(8, x11)[0], ax.i2gp(8, x11)[1], 0]
        eps = ValueTracker(2)
        epsmin = DashedLine(
            ax.c2p(0, 8+sin(8)*3 - eps.get_value(), 0),
            ax.c2p(20, 8+sin(8)*3 - eps.get_value(), 0),
            stroke_width=2,
            dash_length=.2,
            color=GREEN_B
        )
        epsmax = DashedLine(
            ax.c2p(0, 8+sin(8)*3 + eps.get_value(), 0),
            ax.c2p(20, 8+sin(8)*3 + eps.get_value(), 0),
            stroke_width=2,
            dash_length=.2,
            color=GREEN_B
        )
        erct = Polygon(
            ax.c2p(0, 8+sin(8)*3 - eps.get_value(), 0),
            ax.c2p(20, 8+sin(8)*3 - eps.get_value(), 0),
            ax.c2p(20, 8+sin(8)*3 + eps.get_value(), 0),
            ax.c2p(0, 8+sin(8)*3 + eps.get_value(), 0),
            stroke_opacity=0,
            fill_opacity=.5,
            fill_color=GREEN_B
        )
        lemin = MathTex(r"L - \varepsilon").next_to(epsmin)
        lemax = MathTex(r"L + \varepsilon").next_to(epsmax)
        aline = ax.get_horizontal_line(pnt)
        ebrace = Brace(VGroup(epsmax, epsmin))
        etext = ebrace.get_tex(r"2\varepsilon")
        lll = MathTex(r"L").next_to(aline, LEFT)

        b = ValueTracker(1)

        bmin = ax.get_vertical_line(ax.i2gp(8 - b.get_value(), x11))
        bmax = ax.get_vertical_line(ax.i2gp(8 + b.get_value(), x11))

        self.add(ax, labels, x11, t_label[0], aline, epsmin, epsmax, erct, etext, ebrace, lll, bmin, bmax)
        #self.play(ReplacementTransform(VGroup(lemax, lemax), VGroup(etext, ebrace)))
