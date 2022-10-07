from emanim import *

class Template(Scene):
    def construct(self):
        lim = MathTex(r"\lim_{x \to x_0} f(x) = A").scale(3)
        x0 = Tex("$x_0$ - число к которому стремиться $x$")
        Aa = Tex("$A$ - значение предела")
        self.play(FadeIn(lim))
        self.wait()
        self.play(lim.animate.shift(UP*2.5))

        self.wait(3)
