from manim import *
import numpy as np
from os import path

WAITT = 1.5
class RoundedTriangle(Triangle):
    def __init__(self, corner_radius=0.18, **kwargs):
        super().__init__(**kwargs)
        self.corner_radius = corner_radius

class MScene(Scene):
    logo = Tex(r"$\vec{F}$", r"(m)", substrings_to_isolate="m")
    subCounter = Integer(1).to_edge(DL)
    ser = 1
    st1 = 0
    st2 = 0

    mConfig = {
        "subfile" : "",
        "FSD" : 30,
        "MAXS" : 60,
        "DEFSUBCOLOR" : WHITE,
        "LANG" : "ru"
    }

    subConfig = {
        "default" : [WHITE, NORMAL, NORMAL],
        "note" : [YELLOW, NORMAL, ITALIC]
    }

    def subw(self, num, type="default"):
        for i in range(0, num):
            self.dSt(type = type)
            self.wait(WAITT)

    def defgraph(self):
        graph = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 10, 1],
            x_axis_config={
                "numbers_to_include": np.arange(0, 10.01, 1)
            },
            y_axis_config={
                "numbers_to_include": np.arange(0, 10.01, 1)
            },
            tips = False
        ).shift(UP).scale(0.9)
        return graph

    def default(self, type="d", file=__file__):
        #region SubLoad
        name = path.splitext(os.path.basename(file))[0]
        sLang = self.mConfig["LANG"]
        self.mConfig["subfile"] = open(f"Subtitles/{sLang}/{name}.txt" , mode="rt", encoding='utf-8' )
        #endregion
        
        self.type = type
        if self.type == "y":
            rect = RoundedRectangle(corner_radius=0.23, height=1, width=1.41)
            rect.scale(4).set_fill("#da271e", 1).set_stroke(width=0)
            tri = RoundedTriangle() 
            tri.stretch(factor=1.15, dim=1)
            tri.rotate(-PI/2).set_stroke(width=0)
            tri.set_fill(WHITE, 1).move_to(rect.get_center())
            
            # Предварительно следует установить шрифт YouTube Sans,
            # но для пробы можете использовать любой другой
            you = Text("YouTube Edition", font="YouTube Sans", color=WHITE)         
            you.rescale_to_fit(rect.get_width()*0.9, 0).next_to(rect, DOWN)
            banner = VGroup(rect, tri, you)
        elif type == "d":
            logo = Text("", font="Font Awesome").scale(7)
            textb = Text("Debug Mode", font="YouTube Sans", color=WHITE)         
            textb.rescale_to_fit(logo.get_width()*0.9, 0).next_to(logo, DOWN)
            banner = VGroup(logo, textb)
        self.play(FadeIn(banner))
        self.wait(WAITT)
        self.play(FadeOut(banner))
        self.logo.set_color_by_tex(r"vec{F}", BLUE)
        self.logo.set_color_by_tex("m", "#56E3A7")
        self.play(Write(self.logo.scale(7)), run_time=3)
        self.wait()
        self.play(self.logo.animate.scale(0.1).to_edge(DL))
        self.line = Line(start=np.array([-8, -2.5, 0]), end=np.array([9, -2.5, 0]))
        self.play(Create(self.line))

        #if type == "d":
            #self.play(ReplacementTransform(self.logo, self.subCounter))

        stext = self.mConfig["subfile"].readline()

        self.st1 = Text(stext, font="Lucida Grande", font_size=self.mConfig["FSD"]).shift(np.array([0, -3, 0]))
        self.st2 = Text(" ", font="Lucida Grande", font_size=self.mConfig["FSD"]).shift(np.array([0, -3, 0]))
        self.play(Write(VGroup(self.st1, self.st2)))

    def dGraph(self, obj):
        for i in obj:
            self.play(Create(i), run_time=1)

    def dCoords(self, sx=-7, ex=8, sy=-4, ey=4):
        for x in range(sx, ex):
            for y in range(sy, ey):
                self.add(Dot(np.array([x, y, 0]), color=GREY))
    
    def dSt(self, *funcs, type = "default", waiter = 0.5):

        if self.type == "d":
            self.ser += 1
            self.play(Transform(self.subCounter, Integer(self.ser).to_edge(DL)))
        
        conf = self.subConfig

        stext = self.mConfig["subfile"].readline()

        if len(stext) >= self.mConfig["MAXS"]:
            ind = stext.rfind(" ", 0, round(len(stext)/2) + 2)
            stext1 = stext[:ind]
            stext2 = stext[ind:]
        else:
            stext1 = stext
            stext2 = " "
        st1 = Text(stext1, font_size=self.mConfig["FSD"], font="Lucida Grande", color=conf[type][0], weight=conf[type][1], slant=conf[type][2]).shift(np.array([0, -3, 0]))
        st2 = Text(stext2, font_size=self.mConfig["FSD"], font="Lucida Grande", color=conf[type][0], weight=conf[type][1], slant=conf[type][2]).next_to(st1, DOWN)

        self.play(Transform(self.st1, st1), Transform(self.st2, st2), *funcs)
        self.wait(waiter)

    def outro(self, ared, time=5):
        self.wait()
        ared.add(self.logo, self.line, self.st1, self.st2)
        self.play(FadeOut(ared))

        um = Tex(
            r"Music:\\",
            r"Boardroom Theme",
            " - ",
            r"Unicorn Heads\\",
            r"News Room News",
            " - ",
            r"Spence\\",
            r"Program:\\",
            r"ffmpeg\\",
            r"Manim"
            )
        um[1].set_color(BLUE)
        um[3].set_color("#56E3A7")
        um[4].set_color(BLUE)
        um[6].set_color("#56E3A7")
        um[8].set_color(BLUE)
        um[9].set_color("#56E3A7")
        self.play(FadeIn(um))
        self.wait()
        self.play(FadeOut(um))
        self.wait(0.5)

        f = Tex("Wir müssen wissen", " — ", "wir werden wissen!")
        dh = Tex("— David Hilbert").next_to(f, DOWN).to_edge(RIGHT)
        f[0].set_color(BLUE)
        f[2].set_color("#56E3A7")
        self.play(Write(f))
        self.wait(0.3)
        self.play(Write(dh))
        self.wait(time)
