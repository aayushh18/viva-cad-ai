import FreeCAD as App
import Part

doc = App.newDocument("Pro_Flow_Meter")

# 1. Meter Body (Hollow Pipe with Flanges)
p_out = Part.makeCylinder(15, 60)
p_in = Part.makeCylinder(12, 70)
p_in.translate(App.Vector(0,0,-5))
body = p_out.cut(p_in)

# 2. Transmitter Box (The Electronics on top)
box = Part.makeBox(25, 25, 20)
box.translate(App.Vector(-12.5, -12.5, 15))

# 3. Display Screen (Small cut on the box)
screen = Part.makeBox(15, 2, 10)
screen.translate(App.Vector(-7.5, 11, 20))
transmitter = box.cut(screen)

# 4. Flanges at ends
f1 = Part.makeCylinder(25, 5)
f2 = f1.copy()
f2.translate(App.Vector(0,0,55))

flow_meter = body.fuse(transmitter).fuse(f1).fuse(f2)
Part.show(flow_meter)
doc.recompute()