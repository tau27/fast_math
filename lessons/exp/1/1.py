from manim import *
from Templ import *

class GeneralS(MScene):
    def construct(self):
        tex = Tex("Manim", color = BLUE).scale(4).shift(UP)
        text = Text("На русском языке", color = RED).shift(DOWN)
        self.play(Write(VGroup(tex, text).move_to(ORIGIN)))
