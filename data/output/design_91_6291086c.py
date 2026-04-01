import FreeCAD as App
import Part
import math
import Import

doc = App.newDocument("Holes")

plate = Part.makeCircle(30)

for i in range(4):
    angle = math.radians(i * 90)
    x = 15 * math.cos(angle)
    y = 15 * math.sin(angle)
    hole = Part.makeCylinder(5, 10)
    hole.Placement.Base = App.Vector(x, y, 0)
    plate = plate.cut(hole)

obj = doc.addObject("Part::Feature", "Plate")
obj.Shape = plate
doc.recompute()
Import.export(doc.Objects, "../data/output/design_91_6291086c.step")
import FreeCAD
if FreeCAD.GuiUp:
    import FreeCADGui
    try:
        FreeCADGui.activeDocument().activeView().viewIsometric()
        FreeCADGui.SendMsgToActiveView('ViewFit')
    except Exception:
        pass
