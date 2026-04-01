import FreeCAD as App
import Part

doc = App.newDocument("Valve")

# Pipe body
pipe1 = Part.makeCylinder(10, 40)
pipe2 = Part.makeCylinder(10, 40)
pipe2.translate(App.Vector(40,0,0))

# Valve body (middle box)
body = Part.makeBox(20, 30, 20)
body.translate(App.Vector(30, -15, 0))

# Handle
handle = Part.makeCylinder(3, 30)
handle.rotate(App.Vector(0,0,0), App.Vector(1,0,0), 90)
handle.translate(App.Vector(40, 0, 20))

valve = pipe1.fuse(pipe2).fuse(body).fuse(handle)

Part.show(valve)
doc.recompute()