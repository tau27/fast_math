from manim import *
import numpy as np

WAITTIME = 1.5
class RoundedTriangle(Triangle):
    def __init__(self, corner_radius=0.18, **kwargs):
        super().__init__(**kwargs)
        self.corner_radius = corner_radius

class MScene(Scene):
    mod_templ = TexTemplate()
    mod_templ.default_preamble = r"""
\usepackage[russian, english]{babel}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[T2A]{fontenc}
\usepackage{amsmath}
\usepackage{amssymb}
"""
    logo = Tex(r"$\vec{F}$", r"(m)", substrings_to_isolate="m")
    subCounter = Integer(1).to_edge(DL)
    subId = 1
    st1 = VGroup()
    st2 = VGroup()

    files = {}

    subtitles = []

    stConfig = {
        "FSD" : 30,
        "MAXS" : 60,
        "DEFSUBCOLOR" : WHITE,
        "LANG" : "ru"
    }

    subConfig = {
        "default" : [WHITE, NORMAL, NORMAL],
        "note" : [YELLOW, NORMAL, ITALIC]
    }

    customConfig = {}

    def initFiles(self):
        sLang = self.stConfig["LANG"]
        self.files['config'] = open(__file__.replace('lessons', 'config').replace('py', 'txt') , mode="rt", encoding='utf-8' )
        self.files['subtitles'] = open(__file__.replace('lessons', f'subtitles/{sLang}').replace('py', 'txt'), mode="rt", encoding='utf-8' )
        self.sudtitles = self.files['subtitles'].readlines()

    def confReader(self, file):
        conf = file.readlines()
        for i in range(0, len(conf)):
            conf[i] = conf[i][:-1]
        result = {}
        buf = {}

        conf[0] = conf[0].replace('[', '')
        conf[0] = conf[0].replace(']', '')
        module = conf[0]
        conf.pop(0)

        for line in conf:
            if line[0] == '[':
                result[module] = buf.copy()
                buf.clear()

                line = line.replace('[', '')
                line = line.replace(']', '')
                module = line
            else:
                num = line.find(':')
                key = line[:num]
                value = line[num + 1:]
                buf[key] = value

        result[module] = buf.copy()
        return(result)
    def getBanner(self, type):
        if type == "y":
            rect = RoundedRectangle(corner_radius=0.23, height=1, width=1.41)
            rect.scale(4).set_fill("#da271e", 1).set_stroke(width=0)
            tri = RoundedTriangle() 
            tri.stretch(factor=1.15, dim=1)
            tri.rotate(-PI/2).set_stroke(width=0)
            tri.set_fill(WHITE, 1).move_to(rect.get_center())
            you = Text("YouTube Edition", font="YouTube Sans", color=WHITE)         
            you.rescale_to_fit(rect.get_width()*0.9, 0).next_to(rect, DOWN)
            banner = VGroup(rect, tri, you)
        elif type == "d":
            logo = Text("", font="Font Awesome").scale(7)
            textb = Text("Debug Mode", font="YouTube Sans", color=WHITE)         
            textb.rescale_to_fit(logo.get_width()*0.9, 0).next_to(logo, DOWN)
            banner = VGroup(logo, textb)
        
        else:
            banner = VGroup()
        return(banner)


    def startLess(self, type="d"):
        self.initFiles()   

        #Objs Init
        self.logo.set_color_by_tex(r"vec{F}", BLUE)
        self.logo.set_color_by_tex("m", "#56E3A7")
        self.customConfig = self.confReader(self.files['config'])
        self.type = type
        banner = self.getBanner(type)

        self.play(FadeIn(banner))
        self.wait(WAITTIME)
        self.play(FadeOut(banner))
        self.play(Write(self.logo.scale(7)), run_time=3)
        self.wait()
        self.play(self.logo.animate.scale(0.1).to_edge(DL))
        self.line = Line(start=np.array([-8, -2.5, 0]), end=np.array([9, -2.5, 0]))
        self.play(Create(self.line))

        stext = self.subtitles[0]

        self.st1 = Text(stext, font="Lucida Grande", font_size=self.stConfig["FSD"]).shift(np.array([0, -3, 0]))
        self.st2 = Text(" ", font="Lucida Grande", font_size=self.stConfig["FSD"]).shift(np.array([0, -3, 0]))
        self.play(Write(VGroup(self.st1, self.st2)))

    def drawer(self, objs, time = 1):
        for i in objs:
            self.play(Create(i), run_time = time)

    def dCoords(self, sx=-7, ex=8, sy=-4, ey=4):
        for x in range(sx, ex):
            for y in range(sy, ey):
                self.add(Dot(np.array([x, y, 0]), color=GREY))
    
    def dSt(self, *funcs, type = "default", waiter = 0.5):
        conf = self.subConfig[type]
        id = self.subId
        stext = self.subtitles[id]
        self.subId += 1

        if len(stext) >= self.stConfig["MAXS"]:
            ind = stext.rfind(" ", 0, round(len(stext)/2) + 2)
            stext1 = stext[:ind]
            stext2 = stext[ind:]
        else:
            stext1 = stext
            stext2 = " "
        st1 = Text(stext1, font_size=self.stConfig["FSD"], font="Lucida Grande", color=conf[0], weight=conf[1], slant=conf[2]).shift(np.array([0, -3, 0]))
        st2 = Text(stext2, font_size=self.stConfig["FSD"], font="Lucida Grande", color=conf[0], weight=conf[1], slant=conf[2]).next_to(st1, DOWN)

        self.play(Transform(self.st1, st1), Transform(self.st2, st2), *funcs)
        self.wait(waiter)

    def multiSub(self, num, type="default"):
        for _ in range(0, num):
            self.dSt(type = type)
            self.wait(WAITTIME)

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
