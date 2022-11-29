from emanim import *

class Notation(EScene):
    def construct(self):
        self.start_lesson(file=__file__, type="y")
        self.next_subt()

        sf = 2
        n = MathTex(r"\mathbb{N}").scale(sf).shift(UL * 2 + UP)
        mn = Tex(r"$\mathbb{N}$aturalis").scale(sf).shift(UL * 2 + UP)
        z = MathTex(r"\mathbb{Z}").scale(sf).shift(UL + LEFT)
        mz = Tex(r"$\mathbb{Z}$ahlen").scale(sf).shift(UL + LEFT)
        q = MathTex(r"\mathbb{Q}").scale(sf).shift(DL + LEFT)
        mq = Tex(r"$\mathbb{Q}$uotient").scale(sf).shift(DL + LEFT)
        r = MathTex(r"\mathbb{R}").scale(sf).shift(UR * 2)
        mr = Tex(r"$\mathbb{R}$ealis").scale(sf).shift(UR * 2)
        c = MathTex(r"\mathbb{C}").scale(sf).shift(RIGHT * 2)
        mc = Tex(r"$\mathbb{C}$omplexus").scale(sf).shift(RIGHT * 2)
        self.next_subt(FadeIn(n, z, q, r, c, scale=0.5))
        self.next_subt(Transform(n, mn), Transform(z, mz))
        self.next_subt(Transform(q, mq))
        self.next_subt()
        self.next_subt(Transform(r, mr))
        self.next_subt()
        self.next_subt(Transform(c, mc))
        self.next_subt()
        self.play(FadeOut(n, z, q, r, c, scale=0.5))
        
        a = MathTex(r"\forall").scale(sf).shift(UL + LEFT)
        all = MathTex(r"{\forall}ll").scale(sf).shift(UL + LEFT)
        any = MathTex(r"{\forall}ny").scale(sf).shift(UL + LEFT)
        e = MathTex(r"\exists").scale(sf).shift(UR + RIGHT)
        exist = MathTex(r"{\exists}xist").scale(sf).shift(UR + RIGHT)
        eXist = MathTex(r"{\exists}!xist").scale(sf).shift(UR + RIGHT)

        self.next_subt(Write(VGroup(a, e)))
        self.next_subt(Transform(a, all))
        self.next_subt(Transform(a, any))
        self.next_subt()
        self.next_subt(Transform(e, exist))
        self.next_subt(Transform(e, eXist))
        self.play(Unwrite(VGroup(a, e)))

        text_pt = Tex(
                r"""Число $f(x_0)$ называют наибольшем значением функции\\$f$ 
                на множестве $M \subset D(f)$,\\если существует такое число $x_0 \in M$,\\
                что для всех $x \in M$ выполняется неравенство $f(x_0) \geqslant f(x)$"""
                )

        self.next_subt(Write(text_pt))

        self.wait(3)
