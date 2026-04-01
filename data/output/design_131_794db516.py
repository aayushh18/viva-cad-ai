import FreeCAD as App
import Part

doc = App.newDocument("Pro_Elbow")

# Parameters
R = 50  # Bend radius
r_outer = 15 # Bahar ka radius
r_inner = 12 # Andar ka khali hissa (3mm wall thickness)

# Create two tori and subtract
outer = Part.makeTorus(R, r_outer, App.Vector(0,0,0), App.Vector(0,0,1), 0, 90)
inner = Part.makeTorus(R, r_inner, App.Vector(0,0,0), App.Vector(0,0,1), 0, 90)
elbow = outer.cut(inner)

Part.show(elbow)
doc.recompute()