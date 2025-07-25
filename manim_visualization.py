
from manim import *
import numpy as np

class CauchyRiemannProof(Scene):
    def construct(self):
        # Title
        title = Tex(r"\textbf{Cauchy-Riemann Equations Proof}", font_size=48)
        subtitle = Tex(r"$f(z)=u(x,y)+iv(x,y)$ analytic $\implies$ CR equations hold", font_size=32)
        subtitle.next_to(title, DOWN)
        self.play(Write(title), Write(subtitle))
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(subtitle))

        # Step 1: State the problem
        problem = VGroup(
            Tex(r"\textbf{Problem:}", font_size=40),
            Tex(r"Let $f(z)=u(x,y)+iv(x,y)$ be complex differentiable at $z_0$."),
            Tex(r"Prove the Cauchy-Riemann equations:"),
            Tex(r"\begin{align*}\frac{\partial u}{\partial x}&=\frac{\partial v}{\partial y}\\\frac{\partial v}{\partial x}&=-\frac{\partial u}{\partial y}\end{align*}")
        ).arrange(DOWN, aligned_edge=LEFT).to_edge(UP)
        self.play(Write(problem))
        self.wait(2.5)
        self.play(FadeOut(problem))

        # Step 2: Definition of derivative
        def_text = VGroup(
            Tex(r"\textbf{Step 1: Definition of derivative}", font_size=36),
            Tex(r"$f'(z_0)=\displaystyle\lim_{h\to 0}\frac{f(z_0+h)-f(z_0)}{h}$"),
            Tex(r"Limit must be same for all directions $h\to 0$")
        ).arrange(DOWN).to_edge(UP)
        self.play(Write(def_text))
        self.wait(2)
        self.play(FadeOut(def_text))

        # Step 3: Approach along real axis
        real_axis = VGroup(
            Tex(r"\textbf{Step 2: Approach along real axis}", font_size=36),
            Tex(r"Let $h=\Delta x\in\mathbb{R}$"),
            Tex(r"$f'(z_0)=\dfrac{\partial u}{\partial x}+i\dfrac{\partial v}{\partial x}$")
        ).arrange(DOWN).to_edge(UP)
        self.play(Write(real_axis))
        self.wait(2)
        self.play(FadeOut(real_axis))

        # Step 4: Approach along imaginary axis
        imag_axis = VGroup(
            Tex(r"\textbf{Step 3: Approach along imaginary axis}", font_size=36),
            Tex(r"Let $h=i\Delta y$"),
            Tex(r"$f'(z_0)=\dfrac{\partial v}{\partial y}-i\dfrac{\partial u}{\partial y}$")
        ).arrange(DOWN).to_edge(UP)
        self.play(Write(imag_axis))
        self.wait(2)
        self.play(FadeOut(imag_axis))

        # Step 5: Equating both expressions
        equating = VGroup(
            Tex(r"\textbf{Step 4: Equating both expressions}", font_size=36),
            Tex(r"$\dfrac{\partial u}{\partial x}+i\dfrac{\partial v}{\partial x}=\dfrac{\partial v}{\partial y}-i\dfrac{\partial u}{\partial y}$")
        ).arrange(DOWN).to_edge(UP)
        self.play(Write(equating))
        self.wait(2)

        # Highlight real and imaginary parts
        equation = Tex(r"$\dfrac{\partial u}{\partial x}+i\dfrac{\partial v}{\partial x}=\dfrac{\partial v}{\partial y}-i\dfrac{\partial u}{\partial y}$")
        equation.to_edge(UP)
        self.play(ReplacementTransform(equating, equation))
        self.wait(1)

        # Animate highlighting real and imaginary parts
        real_part = Tex(r"$\dfrac{\partial u}{\partial x}=\dfrac{\partial v}{\partial y}$")
        imag_part = Tex(r"$\dfrac{\partial v}{\partial x}=-\dfrac{\partial u}{\partial y}$")
        real_part.next_to(equation, DOWN, buff=1.5).shift(LEFT*2)
        imag_part.next_to(real_part, RIGHT, buff=2)

        # Boxes around real and imaginary parts
        box1 = SurroundingRectangle(real_part, color=YELLOW)
        box2 = SurroundingRectangle(imag_part, color=YELLOW)

        self.play(Write(real_part), Create(box1))
        self.wait(1)
        self.play(Write(imag_part), Create(box2))
        self.wait(2)

        # Step 6: Summary frame
        summary = VGroup(
            Tex(r"\textbf{Cauchy-Riemann Equations}", font_size=44),
            Tex(r"\begin{align*}\frac{\partial u}{\partial x}&=\frac{\partial v}{\partial y}\\\frac{\partial v}{\partial x}&=-\frac{\partial u}{\partial y}\end{align*}", font_size=40),
            Tex(r"\textbf{These must hold for $f(z)$ to be analytic}", font_size=32)
        ).arrange(DOWN)
        self.play(
            *[FadeOut(mob) for mob in [equation, real_part, imag_part, box1, box2]],
            FadeIn(summary)
        )
        self.wait(3)

        # Example verification
        example_title = Tex(r"\textbf{Example: Verify for }$f(z)=z^2$", font_size=36)
        example_title.to_edge(UP)
        self.play(ReplacementTransform(summary, example_title))
        self.wait(1)

        # Compute u and v
        uv_def = VGroup(
            Tex(r"$f(z)=z^2=(x+iy)^2$"),
            Tex(r"$u(x,y)=x^2-y^2$"),
            Tex(r"$v(x,y)=2xy$")
        ).arrange(DOWN).next_to(example_title, DOWN, buff=0.5)
        self.play(Write(uv_def))
        self.wait(2)

        # Compute partial derivatives
        derivatives = VGroup(
            Tex(r"\begin{align*}\frac{\partial u}{\partial x}&=2x\\\frac{\partial u}{\partial y}&=-2y\\\frac{\partial v}{\partial x}&=2y\\\frac{\partial v}{\partial y}&=2x\end{align*}")
        ).next_to(uv_def, DOWN)
        self.play(Write(derivatives))
        self.wait(2)

        # Check equations
        check = VGroup(
            Tex(r"\textbf{Check CR equations:}", font_size=32),
            Tex(r"\begin{align*}\frac{\partial u}{\partial x}&=\frac{\partial v}{\partial y}\implies 2x=2x\quad\checkmark\\\frac{\partial v}{\partial x}&=-\frac{\partial u}{\partial y}\implies 2y=-(-2y)\quad\checkmark\end{align*}", font_size=28)
        ).arrange(DOWN).next_to(derivatives, DOWN, buff=0.5)
        self.play(Write(check))
        self.wait(3)

        # Final summary
        final = VGroup(
            Tex(r"\textbf{Conclusion:}", font_size=36),
            Tex(r"$f(z)=z^2$ satisfies the Cauchy-Riemann equations", font_size=32),
            Tex(r"and is analytic everywhere", font_size=32)
        ).arrange(DOWN)
        self.play(
            *[FadeOut(mob) for mob in [example_title, uv_def, derivatives, check]],
            FadeIn(final)
        )
        self.wait(4)