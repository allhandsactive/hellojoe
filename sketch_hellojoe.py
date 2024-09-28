import vsketch
import math
import numpy as np


class HellojoeSketch(vsketch.SketchClass):
    c1_dia = vsketch.Param(2.0, step = .1 )
    c1_speed = vsketch.Param(1, step=.1)
    c2_dia = vsketch.Param(2.5, step=.1)
    c2_speed = vsketch.Param(9, step=1,)
    smoothness = vsketch.Param(20, step=1,)

    def draw(self, vsk: vsketch.SketchClass) -> None:
        vsk.size("10cm","10cm")
        vsk.scale("cm")
        x = self.c1_dia+self.c2_dia #calculate the starting point
        y = 0

        gcd = math.gcd(self.c1_speed, self.c2_speed)
        print (f'Greatest common divisor: {gcd}')
        # dividing the speeds by the gcd reduces the total number of points to plot
        # speeds 10 and 40 produce the same plot as speeds 1 and 4
        self.c1_speed = self.c1_speed/gcd
        self.c2_speed = self.c2_speed/gcd
        
        # now calculate how many revolutions are needed before we end up back
        # at the start of the pattern
        lcm = math.lcm(int(self.c1_speed), int(self.c2_speed))
        print(f' least common multiple: {lcm}')

        #calculate the spacing between points based on the smoothness number
        spacing = 1/(max(self.c1_speed, self.c2_speed)*self.smoothness)
        print(f'number of points: {lcm/spacing}')

        #draw the points
        #this is triginometery - you can review the unit circle or trust that it works
        #np.arange creates evenly spaced values but handles non-integer values
        #unlike range()
        for n in np.arange(0,lcm+1, spacing):
            new_x = self.c1_dia*math.cos(self.c1_speed*2*math.pi * n)+self.c2_dia*math.cos(self.c2_speed*2*math.pi * n)
            new_y = self.c1_dia*math.sin(self.c1_speed*2*math.pi * n)+self.c2_dia*math.sin(self.c2_speed*2*math.pi * n)
            vsk.line(x,y,new_x,new_y)
            x=new_x
            y=new_y

    def finalize(self, vsk: vsketch.Vsketch) -> None:
        vsk.vpype("linemerge linesimplify reloop linesort")


if __name__ == "__main__":
    HellojoeSketch.display()
