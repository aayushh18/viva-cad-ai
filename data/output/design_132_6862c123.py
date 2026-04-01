import FreeCAD as App
import Part

doc = App.newDocument("Pro_Elbow_Fix")

R = 50 # Bend radius
r_out = 15 # Outer pipe radius
r_in = 12 # Inner pipe radius

# Parameters: (MajorRadius, MinorRadius, Center, Axis, CrossSectionStart, CrossSectionEnd, SweepAngle)
outer = Part.makeTorus(R, r_out, App.Vector(0,0,0), App.Vector(0,0,1), 0, 360, 90)
inner = Part.makeTorus(R, r_in, App.Vector(0,0,0), App.Vector(0,0,1), 0, 360, 90)
elbow = outer.cut(inner)

Part.show(elbow)
doc.recompute()