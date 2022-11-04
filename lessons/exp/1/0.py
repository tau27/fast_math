from emanim import *
from math import sin, asin

class Perdel(EScene):
    def construct(self):
        self.start_lesson(file=__file__)
        lim = MathTex(r"\lim_{x \to x_0} f(x) = a").scale(3)
        mod_lim = MathTex(r"f(x) \xrightarrow[x \to x_0]{} L").scale(3)
        hard = MathTex(
            r"\forall \varepsilon > 0\ \exists\delta > 0\ \forall x\in\mathbb{R}",
            r":",
            r"|x - x_0| < \delta",
            r"\Rightarrow",
            r"|f(x) - L| < \varepsilon",
        ).scale(1)
        f_box1 = SurroundingRectangle(hard[0], buff=.1)
        f_box2 = SurroundingRectangle(hard[2], buff=.1)
        f_box3 = SurroundingRectangle(hard[4], buff=.1)
        self.next_subt(FadeIn(lim))
        self.next_subt(ReplacementTransform(lim, mod_lim))
        self.next_subt(ReplacementTransform(mod_lim, hard))
        #obsStart
        ax = Axes(
            x_range=[0, 20, 1],
            y_range=[0, 20, 1],
            axis_config={"color": GREEN},
            tips=False
        ).shift(UP).scale(0.8)
        labels = ax.get_axis_labels(x_label="x", y_label="f(x)")

        x11 = ax.plot(lambda x: x+sin(x)*3, color=BLUE, x_range=[0, 20.0, 0.01],)
        t_label = ax.get_T_label(x_val=8, graph=x11, label=MathTex("x_0"), triangle_size=0)
        pnt = [ax.i2gp(8, x11)[0], ax.i2gp(8, x11)[1], 0]
        aline = ax.get_horizontal_line(ax.i2gp(8, x11))
        lll = MathTex(r"L").next_to(aline, LEFT)
        aax = VGroup(ax, labels, x11)
        hard_m = hard.copy().scale(.6).shift(UP*3.5)
        self.next_subt()
        self.play(FadeOut(hard))
        self.next_subt(FadeIn(aax))
        self.next_subt(FadeIn(t_label, aline, lll, hard_m))

        #eps

        f_box1 = SurroundingRectangle(hard_m[0], buff=.05)
        f_box2 = SurroundingRectangle(hard_m[2], buff=.05)
        f_box3 = SurroundingRectangle(hard_m[4], buff=.05)
        self.next_subt()
        self.drawer([f_box1, f_box3])

        eps = ValueTracker(2)
        epsmin = always_redraw(lambda: DashedLine(
            ax.c2p(0, 8+sin(8)*3 - eps.get_value(), 0),
            ax.c2p(20, 8+sin(8)*3 - eps.get_value(), 0),
            stroke_width=2,
            dash_length=.2,
            color=GREEN_B
        ))

        epsmax = always_redraw(lambda: DashedLine(
            ax.c2p(0, 8+sin(8)*3 + eps.get_value(), 0),
            ax.c2p(20, 8+sin(8)*3 + eps.get_value(), 0),
            stroke_width=2,
            dash_length=.2,
            color=GREEN_B
        ))

        erct = always_redraw(lambda: Polygon(
            ax.c2p(0, 8+sin(8)*3 - eps.get_value(), 0),
            ax.c2p(20, 8+sin(8)*3 - eps.get_value(), 0),
            ax.c2p(20, 8+sin(8)*3 + eps.get_value(), 0),
            ax.c2p(0, 8+sin(8)*3 + eps.get_value(), 0),
            stroke_opacity=0,
            fill_opacity=.5,
            fill_color=GREEN_B
        ))

        lemin = always_redraw(lambda: MathTex(r"L - \varepsilon").next_to(epsmin))
        lemax = always_redraw(lambda: MathTex(r"L + \varepsilon").next_to(epsmax))
        ebrace = always_redraw(lambda: Brace(Line(
            ax.c2p(20, 8+sin(8)*3 - eps.get_value(), 0),
            ax.c2p(20, 8+sin(8)*3 + eps.get_value(), 0)
            )
        ))
        etext = ebrace.get_tex(r"2\varepsilon")

        self.next_subt(Create(VGroup(epsmin, epsmax, erct, lemax, lemin)), Uncreate(VGroup(f_box1, f_box3)))
        self.next_subt(Create(f_box2))
        self.play(Uncreate(f_box2))
        b = ValueTracker(1)

        dmin = always_redraw(lambda: ax.get_vertical_line(ax.i2gp(8 - b.get_value(), x11)))
        dmax = always_redraw(lambda: ax.get_vertical_line(ax.i2gp(8 + b.get_value(), x11)))
        dbrace = always_redraw(lambda: Brace(Line(dmin.start, dmax.start)))
        dtext = dbrace.get_tex(r"2\delta")
        self.next_subt(ReplacementTransform(t_label, VGroup(dbrace, dtext, dmax, dmin)))
        self.next_subt(b.animate.set_value(2), eps.animate.set_value(3))
        self.wait()
        self.play(b.animate.set_value(0.5), eps.animate.set_value(1))
        self.wait()
        self.next_subt(Indicate(lll))
        self.play(Uncreate(aline))
        self.next_subt(FadeOut(VGroup(ax, epsmax, epsmin, lemax, lemin, lll, dmin, dmax, x11, erct, labels, hard_m, dbrace, dtext)), Write(lim))
        self.outro(lim)
