from emanim import *

class Perdel(EScene):
    def construct(self):
        self.start_lesson(file=__file__)
        self.next_subt()
        lim = MathTex(r"\lim_{x \to x_0} f(x) = a").scale(3)
        hard = MathTex(
            r"\forall \varepsilon > 0\ \exists n > 0\ \forall x\in\mathbb{R}",
            r":",
            r"|x - x_0| < n",
            r"\Rightarrow",
            r"|f(x) - a| < \varepsilon",
        ).scale(1)
        f_box1 = SurroundingRectangle(hard[0], buff=.1)
        f_box2 = SurroundingRectangle(hard[2], buff=.1)
        f_box3 = SurroundingRectangle(hard[4], buff=.1)
        self.next_subt(FadeIn(lim))
        self.next_subt(ReplacementTransform(lim, hard))
        self.next_subt(Create(f_box1))
        self.next_subt(ReplacementTransform(f_box1, f_box2))
        self.next_subt(ReplacementTransform(f_box2, f_box3))

        self.wait(3)
