import math
import FreeCAD as App
import Part

doc = App.newDocument("Gate_Valve")

# 1. Valve Body (Hollow)
body_out = Part.makeSphere(22)
body_in = Part.makeSphere(19)
valve_body = body_out.cut(body_in)

# 2. Stem and Handwheel
stem = Part.makeCylinder(4, 30)
stem.translate(App.Vector(0,0,15))
wheel = Part.makeTorus(18, 3)
wheel.translate(App.Vector(0,0,45))

# 3. Gate (Connected to Stem)
gate = Part.makeBox(20, 10, 10)
gate.translate(App.Vector(0, 0, 30))

# 4. Flanges (Ends)
f1 = Part.makeCylinder(28, 8).cut(Part.makeCylinder(12, 8))
f1.rotate(App.Vector(0,0,0), App.Vector(0,1,0), 90)
f2 = f1.copy()
f2.translate(App.Vector(72, 0, 0))

valve = valve_body.fuse(stem).fuse(wheel).fuse(gate).fuse(f1).fuse(f2)

Part.show(valve)
doc.recompute()
doc.recompute()

try:
    import Part
    import FreeCAD as App
    doc = App.ActiveDocument
    if doc:
        objs = [obj for obj in doc.Objects if hasattr(obj, 'Shape') and obj.Shape is not None]
        if objs:
            Part.export(objs, r'../data/output/design_52_ce13add8.step')
        doc.saveAs(r'../data/output/design_52_ce13add8.FCStd')
except Exception as e:
    print("Export Failed:", e)
