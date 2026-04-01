import FreeCAD as App
import Part
import math
import Import

doc = App.newDocument("Plate")
plate = Part.makeBox(100, 100, 10)

for i in range(4):
    angle = math.radians(i * 90)
    x = 50 * math.cos(angle) + 50
    y = 50 * math.sin(angle) + 50
    hole = Part.makeCylinder(5, 10)
    hole.Placement.Base = App.Vector(x, y, 0)
    plate = plate.cut(hole)

obj = doc.addObject("Part::Feature", "Plate")
obj.Shape = plate
doc.recompute()
Import.export(doc.Objects, "../data/output/design_75_1a8b607d.step")
import FreeCAD
if FreeCAD.GuiUp:
    import FreeCADGui
    try:
        FreeCADGui.activeDocument().activeView().viewIsometric()
        FreeCADGui.SendMsgToActiveView('ViewFit')
    except Exception:
        pass
