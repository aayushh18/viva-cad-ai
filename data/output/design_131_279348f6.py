import FreeCAD as App
import Part

doc = App.newDocument("Support")

# Base plate
base = Part.makeBox(120, 120, 10)

# Legs
leg1 = Part.makeCylinder(5, 80)
leg1.translate(App.Vector(10,10,10))

leg2 = leg1.copy()
leg2.translate(App.Vector(100,0,0))

leg3 = leg1.copy()
leg3.translate(App.Vector(0,100,0))

leg4 = leg1.copy()
leg4.translate(App.Vector(100,100,0))

stand = base.fuse(leg1).fuse(leg2).fuse(leg3).fuse(leg4)

Part.show(stand)
doc.recompute()