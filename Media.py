from manim import *
from matplotlib.pyplot import axes
import numpy as np
from pyparsing import col
from templ import *

class Banner(MScene):
    def construct(self):
        self.logo.set_color_by_tex(r"vec{F}", BLUE)
        self.logo.set_color_by_tex("m", "#56E3A7")
        self.logo.to_edge(UL)
        m = 3
        sus = Text("Выпуск 1.", color=BLUE).scale(m).shift(UP)
        sus2 = Text("Производная", color="#56E3A7").scale(m).next_to(sus, DOWN)
        self.add(sus, sus2, self.logo)
