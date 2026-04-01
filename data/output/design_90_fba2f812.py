import FreeCAD as App
import Part
import math
import Import

doc = App.newDocument("Holes")
plate = Part.makeBox(50, 50, 10)

for i in range(4):
    angle = math.radians(i * 90)
    x = 25 + 20 * math.cos(angle)
    y = 25 + 20 * math.sin(angle)
    hole = Part.makeCylinder(5, 10)
    hole.Placement.Base = App.Vector(x, y, 0)
    plate = plate.cut(hole)

obj = doc.addObject("Part::Feature", "Plate")
obj.Shape = plate
doc.recompute()
Import.export(doc.Objects, "../data/output/design_90_fba2f812.step")
import FreeCAD
if FreeCAD.GuiUp:
    import FreeCADGui
    try:
        FreeCADGui.activeDocument().activeView().viewIsometric()
        FreeCADGui.SendMsgToActiveView('ViewFit')
    except Exception:
        pass
