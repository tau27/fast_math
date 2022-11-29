from math import sin
from emanim import *

class Template(EScene):
    def construct(self):
        li = MathTex(r"f(x) \xrightarrow[x \to x_0]{} L")


        self.add(li)
