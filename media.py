from emanim import *

class Banner(Scene):
    def construct(self):
        text = Tex("Fast", " ", "Math")
        text.set_color_by_tex_to_color_map({"Fast" : "#56E3A7","Math" : "#58C4DD"})
        text.scale(5)
        self.add(text)
