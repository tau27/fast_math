from manim import *
import numpy as np
from Media import *
from os import path
from Templ import *

class SusTest(MScene):
    def construct(self):
        text = MathTex(r"\mathbb{TRIVIAL}").scale(5)
        self.play(Write(text))
