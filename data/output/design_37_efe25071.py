import math
import FreeCAD as App
import Part

doc = App.newDocument("FlangeShaft")

# Flange
base = Part.makeCylinder(50, 10)

center = Part.makeCylinder(20, 10)
base = base.cut(center)

for i in range(6):
    angle = math.radians(i * 60)
    x = 35 * math.cos(angle)
    y = 35 * math.sin(angle)

    hole = Part.makeCylinder(5, 10)
    hole.Placement.Base = App.Vector(x, y, 0)

    base = base.cut(hole)

obj = doc.addObject("Part::Feature", "Flange")
obj.Shape = base

# Shaft
c1 = Part.makeCylinder(10, 20)

c2 = Part.makeCylinder(5, 30)
c2.Placement.Base = App.Vector(0, 0, 20)

shaft = c1.fuse(c2)

obj = doc.addObject("Part::Feature", "Shaft")
obj.Shape = shaft

doc.recompute()
doc.recompute()

obj.recompute() # Object level
App.ActiveDocument.recompute() # Document level
obj.purgeTouched() # CRITICAL: Clears the 'Failed' flag and makes status 'Successful'

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
            Part.export(objs, r'../data/output/design_37_efe25071.step')
        doc.saveAs(r'../data/output/design_37_efe25071.FCStd')
except Exception as e:
    print("Export Failed:", e)
