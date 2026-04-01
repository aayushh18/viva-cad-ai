import FreeCAD as App
import Part

doc = App.newDocument("Pipe")

outer_radius = 30
inner_radius = 25
length = 200

outer = Part.makeCylinder(outer_radius, length)
inner = Part.makeCylinder(inner_radius, length)

pipe = outer.cut(inner)

Part.show(pipe)
doc.recompute()