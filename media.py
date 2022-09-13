from emanim import *

class Banner(Scene):
    def construct(self):
        title = Tex("Fast", " ", "Math").shift(UP)
        title.set_color_by_tex_to_color_map({"Fast" : "#56E3A7","Math" : "#58C4DD"})
        title.scale(5)

        quote = Tex("Wir müssen wissen,", " ", "wir werden wissen!").shift(DOWN*2)

        self.add(title, quote)
