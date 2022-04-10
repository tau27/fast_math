from manim import *
import numpy as np

class MScene(Scene):
    mConfig = {
        "subfile" : "",
        "FSD" : 30,
        "MAXS" : 35
        }
    st1 = 0
    st2 = 0

    def debug(self):
        self.dCoords()

    def default(self):
        line = Line(start=np.array([-8, -2.5, 0]), end=np.array([9, -2.5, 0]))
        self.play(Create(line))
        stext = self.mConfig["subfile"].readline()
        if len(stext) >= self.mConfig["MAXS"]:
            ind = stext.rfind(" ", 0, self.mConfig["MAXS"])
            if ind == -1:
                stext1 = stext
                stext2 = ""
            else:
                stext1 = stext[:ind]
                stext2 = stext[ind:]
        else:
            stext1 = stext
            stext2 = ""
        self.st1 = Text(stext1, font_size=self.mConfig["FSD"]).shift(np.array([0, -3, 0]))
        self.st2 = Text(stext2, font_size=self.mConfig["FSD"]).next_to(self.st1, DOWN)
        stal = VGroup(self.st1, self.st2)
        self.play(Write(stal))

    def dGraph(self, obj):
        for i in obj:
            self.play(Create(i), run_time=1)

    def dCoords(self, sx=-7, ex=8, sy=-4, ey=4):
        for x in range(sx, ex):
            for y in range(sy, ey):
                self.add(Dot(np.array([x, y, 0]), color=DARK_GREY))
    
    def dSt(self):
        stext = self.mConfig["subfile"].readline()
        if len(stext) >= self.mConfig["MAXS"]:
            ind = stext.rfind(" ", 0, self.mConfig["MAXS"])
            if ind == -1:
                stext1 = stext
                stext2 = ""
            else:
                stext1 = stext[:ind]
                stext2 = stext[ind:]
        else:
            stext1 = stext
            stext2 = ""
        st1 = Text(stext1, font_size=self.mConfig["FSD"]).shift(np.array([0, -3, 0]))
        st2 = Text(stext2, font_size=self.mConfig["FSD"]).next_to(self.st1, DOWN)
        self.play(Transform(self.st1, st1))
        self.play(Transform(self.st2, st2))