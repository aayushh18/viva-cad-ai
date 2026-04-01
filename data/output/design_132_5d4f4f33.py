import FreeCAD as App
import Part

doc = App.newDocument("Pro_FlowMeter_Fixed")

# 1. Meter Body (Hollow)
body = Part.makeCylinder(15, 80).cut(Part.makeCylinder(12, 80))
body.rotate(App.Vector(0,0,0), App.Vector(0,1,0), 90)

# 2. Flanges (Ends)
f1 = Part.makeCylinder(28, 8).cut(Part.makeCylinder(12, 8))
f1.rotate(App.Vector(0,0,0), App.Vector(0,1,0), 90)
f2 = f1.copy()
f2.translate(App.Vector(72, 0, 0))

# 3. Display Box (On Top)
box = Part.makeBox(30, 30, 20)
box.translate(App.Vector(25, -15, 15))

flow_meter = body.fuse(f1).fuse(f2).fuse(box)
Part.show(flow_meter)
doc.recompute()