from manim import *
import numpy as np
from templ import *

class Banner(MScene):
    def construct(self):
        f = Tex("Wir müssen wissen", " — ", "wir werden wissen!")
        dh = Tex("— David Hilbert").next_to(f, DOWN).to_edge(RIGHT)
        f[0].set_color(BLUE)
        f[2].set_color("#56E3A7")
        self.add(f, dh)