from emanim import *
from math import sin, cos

class Dddx(EScene):
    def construct(self):
        self.start_lesson(file=__file__, type="y")
        self.multiSub(3)

        fx = MathTex("f(x)", color = GREEN).scale(5).shift(UP)
        ffx = MathTex("f'(x)", color = RED).scale(5).shift(UP+RIGHT*3)

        ax = Axes(
            x_range=[0, 20, 1],
            y_range=[-10, 10, 1],
            axis_config={"color": GREEN},
            tips=False
        ).shift(UP).scale(.9)
        labels = ax.get_axis_labels(x_label="x", y_label="f(x)")

        x11 = ax.plot(lambda x: x+sin(x)*3-10, color=BLUE, x_range=[0, 20.0, 0.01],)
        x12 = ax.plot(lambda x: 3*cos(x)+1, color=RED, x_range=[0, 20.0, 0.01],)

        slope = ax.get_secant_slope_group(
            x=12.0,
            graph=x11,
            dx=2.0,
            dx_label=Tex("dx = 1.0"),
            dy_label="dy",
            dx_line_color=GREEN_B,
            secant_line_length=4,
            secant_line_color=RED_D,
        )

        self.next_subt(Write(fx))
        self.play(fx.animate.shift(LEFT*3), Write(ffx))

        self.next_subt()
        self.next_subt(Unwrite(VGroup(fx, ffx)))


        self.drawer([ax, labels, x11, slope], 2)

        self.wait(3)
