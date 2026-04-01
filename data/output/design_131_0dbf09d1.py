import FreeCAD as App
import Part

doc = App.newDocument("Elbow")

# Parameters
R = 50      # bend radius
r = 10      # pipe radius

# Create torus (elbow)
elbow = Part.makeTorus(R, r, App.Vector(0,0,0), App.Vector(0,0,1), 0, 90)

Part.show(elbow)
doc.recompute()