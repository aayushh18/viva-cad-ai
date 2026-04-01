import FreeCAD as App
import Part

doc = App.newDocument("Pro_Pressure_Gauge")

# 1. Gauge Body (The Dial Case)
case_out = Part.makeCylinder(25, 10)
case_in = Part.makeCylinder(23, 10)
case = case_out.cut(case_in)
case.translate(App.Vector(0,0,5))

# 2. Back Plate (The Face)
face = Part.makeCylinder(23, 2)
face.translate(App.Vector(0,0,5))

# 3. Needle (Indicator)
needle = Part.makeBox(18, 1, 1)
needle.translate(App.Vector(0, -0.5, 7))

# 4. Socket (The connection part at bottom)
socket = Part.makeCylinder(5, 15)
socket.rotate(App.Vector(0,0,0), App.Vector(1,0,0), 90)
socket.translate(App.Vector(0, -25, 10))

gauge = case.fuse(face).fuse(needle).fuse(socket)
Part.show(gauge)
doc.recompute()