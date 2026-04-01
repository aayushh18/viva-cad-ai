import FreeCAD as App
import Part

doc = App.newDocument("PipeFlange")

# 1. Pipe (Hollow)
p_out = Part.makeCylinder(30, 200)
p_in = Part.makeCylinder(25, 200)
pipe = p_out.cut(p_in)

# 2. Flange (Hollow Disc)
f_out = Part.makeCylinder(60, 10)
f_in = Part.makeCylinder(25, 12) # Same as pipe inner
flange = f_out.cut(f_in)

# Move flange to pipe end
flange.translate(App.Vector(0, 0, 200))

# Fuse them
result = pipe.fuse(flange)

Part.show(result)
doc.recompute()