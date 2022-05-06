from manim import *
import numpy as np
from Media import *
from os import path

name = path.splitext(os.path.basename(__file__))[0]
print(name)
class SusTest(MediaRender):
    def construct(self):
        text = Text("Тест1\nТест2")
        self.add(text)