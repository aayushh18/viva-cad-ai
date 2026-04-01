import FreeCAD as App
import Part

doc = App.newDocument("Lid")

# Lid plate
lid = Part.makeCylinder(100, 10)

# Handle
handle = Part.makeCylinder(5, 40)
handle.translate(App.Vector(0,0,10))

# Knob
knob = Part.makeSphere(10)
knob.translate(App.Vector(0,0,50))

cover = lid.fuse(handle).fuse(knob)

Part.show(cover)
doc.recompute()