from emanim import *

class Banner(Scene):
    def construct(self):
        num = 1
        type = "exp"
        name = "Предел"
        logo = Tex(r"$\vec{F}$", r"(m)", substrings_to_isolate="m")
        ban = Preview(num, type, name, logo, ["#56E3A7", "#58C4DD"], False)

        self.add(ban)
