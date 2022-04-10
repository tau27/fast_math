from manim import *
import numpy as np
from Templ import *

class Lesson(MScene):
    def construct(self):
        #region def
        self.mConfig["subfile"] = open("Subtitles/Sandbox.txt", mode="rt", encoding='utf-8' )
        self.default()
        #endregion
