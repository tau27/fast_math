
        #dSt3
        self.dSt()

        def func(x):
            return x**2
        ax1 = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 50, 10],
            x_axis_config={
                "numbers_to_include": np.arange(0, 10.01, 1)
            },
            y_axis_config={
                "numbers_to_include": np.arange(0, 50.01, 10)
            },
            tips = False
        ).shift(UP).scale(0.9)
        labels = ax1.get_axis_labels(x_label="x", y_label="y")
        ex = ax1.plot(func, color = BLUE)

        self.dGraph(VGroup(ax1, ex, labels))
        
        t = ValueTracker(2)

        slope = always_redraw(lambda : ax1.get_secant_slope_group(
            x=4.0,
            graph=ex,
            dx=t.get_value(),
            dx_label="dx",
            dy_label="dy",
            dx_line_color=GREEN_B,
            secant_line_length=4,
            secant_line_color=RED_D,
        ))
        self.play(Create(slope))
        self.wait()
        self.play(t.animate.set_value(1))
        self.dSt()
        self.wait()
        self.dSt()
        self.wait()
        self.play(FadeOut(VGroup(slope, ax1, ex, labels)))
        #endregion