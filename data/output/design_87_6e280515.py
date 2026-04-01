import FreeCAD as App
import Part
import math
import Import

doc = App.newDocument("Pattern")
plate = Part.makeBox(50, 50, 10)

for i in range(4):
    angle = math.radians(i * 90)
    x = 15 * math.cos(angle) + 25
    y = 15 * math.sin(angle) + 25
    hole = Part.makeCylinder(3, 10)
    hole.Placement.Base = App.Vector(x, y, 0)
    plate = plate.cut(hole)

hole = Part.makeCylinder(15, 10)
hole.Placement.Base = App.Vector(50, 0, 0)
plate = plate.cut(hole)

obj = doc.addObject("Part::Feature", "Plate")
obj.Shape = plate
doc.recompute()
Import.export(doc.Objects, "../data/output/design_87_6e280515.step")
import FreeCAD
if FreeCAD.GuiUp:
    import FreeCADGui
    try:
        FreeCADGui.activeDocument().activeView().viewIsometric()
        FreeCADGui.SendMsgToActiveView('ViewFit')
    except Exception:
        pass
