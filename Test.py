from manim import *
import numpy as np
from Media import *
from os import path
from Templ import *

name = path.splitext(os.path.basename(__file__))[0]
print(name)
class SusTest(MScene):
    def construct(self):
        config["background_color"] = WHITE
        text = MathTex(r"\mathbb{TRIVIAL}", color = BLACK).scale(5)
        self.add(text)
