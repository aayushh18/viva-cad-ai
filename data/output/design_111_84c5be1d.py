import FreeCAD as App
import Part
import math
import Import

doc = App.newDocument("Plate")

plate = Part.makeBox(50, 50, 10)

for i in range(4):
    angle = math.radians(i * 90)
    x = 15 * math.cos(angle) + 25
    y = 15 * math.sin(angle) + 25
    hole = Part.makeCylinder(3, 10)
    hole.Placement.Base = App.Vector(x, y, 0)
    plate = plate.cut(hole)

boss = Part.makeCylinder(10, 10)
boss.Placement.Base = App.Vector(25, 25, 0)
plate = plate.cut(boss)

obj = doc.addObject("Part::Feature", "Plate")
obj.Shape = plate
doc.recompute()
Import.export(doc.Objects, "../data/output/design_111_84c5be1d.step")
import FreeCAD
if FreeCAD.GuiUp:
    import FreeCADGui
    try:
        FreeCADGui.activeDocument().activeView().viewIsometric()
        FreeCADGui.SendMsgToActiveView('ViewFit')
    except Exception:
        pass
