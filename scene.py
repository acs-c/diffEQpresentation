from manim import *


class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle)) # show the circle on screen
        


class CreateText(Scene):
    def construct(self):
        text = Tex(r"$k' = k -> (1+g)k = (1-d)k + sak^b$",font_size = 32)
        self.play(Write(text))

class SolowSwan(Scene):
    def construct(self):
        self.wait(2)
        title = Text('The Solow-Swan Growth Model')
        self.play(Write(title))
        self.wait(5)
        
        names = Text('By Alex, Jak, and Jamie', font_size = 32)
        self.play(Transform(title,names,path_arc=0))
        self.wait(5)
        self.remove(title)

        self.wait(10)

        solowswaneq = Tex(r"$\frac{dk}{dt} = sf(k) - (\delta + n)k$",font_size = 32)
        ogsolowswaneq = Tex(r"$\frac{dk}{dt} = sf(k) - (\delta + n)k$",font_size = 32) # this is making a pointer, not a copy - need this to make a copy
        self.play(Write(solowswaneq))
        self.wait(30)

        derivative = Tex(r"$\frac{dk}{dt}$",font_size=64)
        ogderivative = Tex(r"$\frac{dk}{dt}$",font_size=64)
        self.play(Transform(solowswaneq,derivative,path_arc = 0))
        self.wait(10)

        xyderiv = Tex(r"$\frac{dx}{dy} \approx \frac{dk}{dt}$",font_size = 64)
        self.play(Transform(solowswaneq,xyderiv,path_arc = 0))
        self.wait(10)

        self.play(Transform(solowswaneq,ogderivative,font_size=64))
        self.wait(10)

        function = Tex(r"$sf(k)$",font_size=64)
        self.play(Transform(solowswaneq,function,path_arc=0))
        self.wait(10)
        
        delta = Tex(r"$(\delta + n)k$",font_size= 64)
        self.play(Transform(solowswaneq,delta,path_arc=0))
        self.wait(10)

        self.play(Transform(solowswaneq,ogsolowswaneq,path_arc=0))
        self.wait(10)

        self.remove(solowswaneq)
        self.wait(3)
        # ax = Axes (
          #  x_range = [0,3,0.5],
           # y_range = [0,18,3],
            # tips = True,
            # axis_config={"include_numbers":True}
        # )

        #graph = FunctionGraph(

        #)
        #dline = ax.plot