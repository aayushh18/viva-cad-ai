import FreeCAD as App
import Part
import math
import Import

doc = App.newDocument("Flange")
base = Part.makeCylinder(50, 10)
center = Part.makeCylinder(20, 10)
base = base.cut(center)

angle = math.radians(360 / 8)
x = 35 * math.cos(angle)
y = 35 * math.sin(angle)
hole = Part.makeCylinder(5, 10)
hole.Placement.Base = App.Vector(x, y, 0)
base = base.cut(hole)

for i in range(1, 8):
    angle = math.radians(i * 360 / 8)
    x = 35 * math.cos(angle)
    y = 35 * math.sin(angle)
    hole = Part.makeCylinder(5, 10)
    hole.Placement.Base = App.Vector(x, y, 0)
    base = base.cut(hole)

obj = doc.addObject("Part::Feature", "Flange")
obj.Shape = base
doc.recompute()
Import.export(doc.Objects, "../data/output/design_97_4796ae1d.step")
import FreeCAD
if FreeCAD.GuiUp:
    import FreeCADGui
    try:
        FreeCADGui.activeDocument().activeView().viewIsometric()
        FreeCADGui.SendMsgToActiveView('ViewFit')
    except Exception:
        pass
