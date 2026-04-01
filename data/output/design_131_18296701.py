import FreeCAD as App
import Part

doc = App.newDocument("PipeFlange")

# Pipe
outer = Part.makeCylinder(30, 200)
inner = Part.makeCylinder(25, 200)
pipe = outer.cut(inner)

# Flange (disc)
flange = Part.makeCylinder(60, 10)

# Move flange to pipe end
flange.translate(App.Vector(0, 0, 200))

# Fuse
result = pipe.fuse(flange)

Part.show(result)
doc.recompute()