import math
import FreeCAD as App
import Part

doc = App.newDocument("FlowMeter")

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

obj = doc.addObject("Part::Feature", "FlowMeter")
obj.Shape = flow_meter

doc.recompute()
doc.recompute()

obj.purgeTouched()

# View Adjustment
import FreeCAD
if FreeCAD.GuiUp:
    import FreeCADGui as Gui
    if Gui.ActiveDocument and Gui.ActiveDocument.ActiveView:
        Gui.ActiveDocument.ActiveView.viewIsometric()
        Gui.ActiveDocument.ActiveView.fitAll()

try:
    import Part
    import FreeCAD as App
    doc = App.ActiveDocument
    if doc:
        objs = [obj for obj in doc.Objects if hasattr(obj, 'Shape') and obj.Shape is not None]
        if objs:
            Part.export(objs, r'../data/output/design_53_f3a0aada.step')
        doc.saveAs(r'../data/output/design_53_f3a0aada.FCStd')
except Exception as e:
    print("Export Failed:", e)
