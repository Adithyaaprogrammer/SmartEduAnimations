from manim import *

class TrigonometricIntegration(Scene):
    def construct(self):
        # Title
        title = Text("Integration of Trigonometric Functions").scale(0.8)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        
        # Create the axes
        axes = Axes(
            x_range=[0, 2*PI, PI/2],
            y_range=[-1.5, 1.5, 0.5],
            x_length=6,
            y_length=4,
            axis_config={"include_tip": False},
        )
        
        # Add x-axis labels
        x_labels = [
            MathTex("0").next_to(axes.c2p(0, 0), DOWN),
            MathTex("\\pi/2").next_to(axes.c2p(PI/2, 0), DOWN),
            MathTex("\\pi").next_to(axes.c2p(PI, 0), DOWN),
            MathTex("3\\pi/2").next_to(axes.c2p(3*PI/2, 0), DOWN),
            MathTex("2\\pi").next_to(axes.c2p(2*PI, 0), DOWN)
        ]
        axes_labels = VGroup(*x_labels)
        
        # Plot sin(x)
        sin_curve = axes.plot(lambda x: np.sin(x), x_range=[0, 2*PI], color=BLUE)
        sin_label = MathTex("y = \\sin(x)").next_to(sin_curve, UP).shift(RIGHT)
        
        # Show the curve and axes
        self.play(Create(axes), Create(axes_labels))
        self.play(Create(sin_curve), Write(sin_label))
        
        # Step 1: Explain area under curve
        step1_text = Text("Step 1: Integration finds the area under the curve").scale(0.6)
        step1_text.to_edge(DOWN, buff=0.5)
        
        area = axes.get_area(sin_curve, x_range=[0, PI], color=BLUE, opacity=0.3)
        
        self.play(Write(step1_text))
        self.play(FadeIn(area))
        self.wait(1)
        
        # Step 2: Approximate using rectangles
        step2_text = Text("Step 2: Approximate area using rectangles").scale(0.6)
        step2_text.to_edge(DOWN, buff=0.5)
        
        rectangles = axes.get_riemann_rectangles(
            sin_curve, x_range=[0, PI], dx=0.2, stroke_width=0.1, 
            stroke_color=WHITE, fill_opacity=0.5
        )
        
        self.play(ReplacementTransform(step1_text, step2_text))
        self.play(ReplacementTransform(area, rectangles))
        self.wait(1)
        
        # Step 3: Finer approximation
        step3_text = Text("Step 3: Finer approximation with more rectangles").scale(0.6)
        step3_text.to_edge(DOWN, buff=0.5)
        
        better_rectangles = axes.get_riemann_rectangles(
            sin_curve, x_range=[0, PI], dx=0.05, stroke_width=0.1,
            stroke_color=WHITE, fill_opacity=0.5
        )
        
        self.play(ReplacementTransform(step2_text, step3_text))
        self.play(ReplacementTransform(rectangles, better_rectangles))
        self.wait(1)
        
        # Step 4: Integration formulas
        step4_text = Text("Step 4: Basic trigonometric integration formulas").scale(0.6)
        step4_text.to_edge(DOWN, buff=0.5)
        
        trig_formulas = MathTex(
            "\\int \\sin(x) \\, dx &= -\\cos(x) + C \\\\",
            "\\int \\cos(x) \\, dx &= \\sin(x) + C"
        ).scale(0.8).next_to(step4_text, UP, buff=0.5)
        
        self.play(ReplacementTransform(step3_text, step4_text))
        self.play(Write(trig_formulas))
        self.wait(1)
        
        # Step 5: Apply to sin(x)
        step5_text = Text("Step 5: Applying the formula to sin(x)").scale(0.6)
        step5_text.to_edge(DOWN, buff=0.5)
        
        application = MathTex(
            "\\int_0^\\pi \\sin(x) \\, dx &= -\\cos(x) \\big|_0^\\pi \\\\",
            "&= -\\cos(\\pi) - (-\\cos(0)) \\\\",
            "&= -(-1) - (-1) = 2"
        ).scale(0.8).next_to(step5_text, UP, buff=0.5)
        
        self.play(ReplacementTransform(step4_text, step5_text))
        self.play(ReplacementTransform(trig_formulas, application))
        self.wait(1)
        
        # Final formulas section
        final_text = Text("Common Trigonometric Integration Formulas:").scale(0.7)
        final_text.to_edge(DOWN, buff=1.5)
        
        final_formulas = MathTex(
            "\\int \\sin(x) \\, dx &= -\\cos(x) + C \\\\",
            "\\int \\cos(x) \\, dx &= \\sin(x) + C \\\\",
            "\\int \\tan(x) \\, dx &= -\\ln|\\cos(x)| + C \\\\",
            "\\int \\sec^2(x) \\, dx &= \\tan(x) + C"
        ).scale(0.7).next_to(final_text, DOWN, buff=0.3)
        
        self.play(
            FadeOut(better_rectangles),
            FadeOut(sin_curve),
            FadeOut(sin_label),
            FadeOut(axes),
            FadeOut(axes_labels),
            FadeOut(step5_text),
            FadeOut(application),
            Write(final_text)
        )
        self.play(Write(final_formulas))
        
        highlight = SurroundingRectangle(final_formulas, color=YELLOW)
        self.play(Create(highlight))
        self.wait(2)