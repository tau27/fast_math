from manim import *
import numpy as np
import sys
import emanim

class sus(Scene):
    def construct(self):
        derero = TexTemplate()
        derero.default_preamble = r"""
\usepackage[russian,english]{babel}
\usepackage[utf8]{inputenc}
\usepackage[T1,T2A]{fontenc}
        """
        text = Tex(r"СССР", tex_template=derero)
        self.play(Write(text))
        self.wait(99)
