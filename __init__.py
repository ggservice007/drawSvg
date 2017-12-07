'''
A library for creating SVG files or just drawings that can be displayed in
iPython notebooks

Example:
```
    d = draw.Drawing(200, 100, origin='center')

    d.append(draw.Lines(-80, -45,
                        70, -49,
                        95, 49,
                        -90, 40,
                        close=False,
                fill='#eeee00',
                stroke='black'))

    d.append(draw.Rectangle(0,0,40,50, fill='#1248ff'))
    d.append(draw.Circle(-40, -10, 30,
                fill='red', stroke_width=2, stroke='black'))

    p = draw.Path(stroke_width=2, stroke='green',
                  fill='black', fill_opacity=0.5)
    p.M(-30,5)
    p.l(60,30)
    p.h(-70)
    p.Z()
    d.append(p)

    d.append(draw.ArcLine(60,-20,20,60,270,
                stroke='red', stroke_width=5, fill='red', fill_opacity=0.2))
    d.append(draw.Arc(60,-20,20,60,270,cw=False,
                stroke='green', stroke_width=3, fill='none'))
    d.append(draw.Arc(60,-20,20,270,60,cw=True,
                stroke='blue', stroke_width=1, fill='black', fill_opacity=0.3))

    d.setPixelScale(2)  # Set number of pixels per geometry unit
    #d.setRenderSize(400,200)  # Alternative to setPixelScale
    d.saveSvg('example.svg')

    d  # Display in iPython notebook
```
'''

from .drawing import Drawing
from .elements import *

