from manim import *
import numpy as np
from Templ import *

class MediaRender(MScene):
    def vBanner(self, vNum="0", vName="Тест", lang="ru", colorTheme=[BLUE, "#56E3A7"]):
        if lang == "ru":
            number = Text(f"Выпуск {vNum}.", color=colorTheme[0])
            name  = Text(vName, color=colorTheme[1]).next_to(number, DOWN)
        banner = VGroup(number, name).move_to(ORIGIN)
        logo = self.logo.to_edge(UL)
        self.add(banner, logo)