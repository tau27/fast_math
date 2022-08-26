from emanim import *

class Notation(EScene):
    def construct(self):
        self.start_lesson(file=__file__)
        self.multiSub(4)
        pr_a = MathTex(r"\forall \quad \mathbb{N}").scale(7).shift(UP)
        self.next_subt(FadeIn(pr_a))
        self.wait(3)
