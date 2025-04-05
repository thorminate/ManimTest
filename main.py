from manim import *


class MathScene(Scene):
    def construct(self):
        # Create a title with LaTeX
        title = Text("Manim's pretty math!", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Section 1: Simple equation
        equation = Tex(r"E = mc^2", tex_environment="math")
        equation.next_to(title, DOWN, buff=0.5)
        self.play(Write(equation))
        self.wait(1)

        # Section 2: Quadratic equation
        quadratic_eq = Tex(r"ax^2 + bx + c = 0", tex_environment="math")
        quadratic_eq.next_to(equation, DOWN, buff=0.5)
        self.play(Write(quadratic_eq))
        self.wait(1)

        # Section 3: Quadratic formula
        quadratic_formula = Tex(
            r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}", tex_environment="math"
        )
        quadratic_formula.next_to(quadratic_eq, DOWN, buff=0.5)
        self.play(Write(quadratic_formula))
        self.wait(1)

        # Section 4: Matrix
        matrix = Matrix(
            [
                [r"a_{11}", r"a_{12}", r"a_{13}"],
                [r"a_{21}", r"a_{22}", r"a_{23}"],
                [r"a_{31}", r"a_{32}", r"a_{33}"],
            ]
        )
        matrix.scale(0.5)
        matrix.next_to(quadratic_formula, DOWN, buff=0.5)
        self.play(Write(matrix))
        self.wait(1)

        # Section 5: Vector
        vector = Tex(
            r"\mathbf{v} = \begin{pmatrix} x \\ y \\ z \end{pmatrix}",
            tex_environment="math",
        )
        vector.next_to(matrix, DOWN, buff=0.5)
        self.play(Write(vector))
        self.wait(1)

        # Final pause to view the full scene
        self.wait(2)
