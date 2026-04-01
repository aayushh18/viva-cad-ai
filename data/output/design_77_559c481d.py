import FreeCAD as App
import Part
import math
import Import

doc = App.newDocument("Plate")

# Create rectangular plate
plate = Part.makeBox(100, 50, 10)

# Create corner holes
for i in range(4):
    angle = math.radians(i * 90)
    x = 25 * math.cos(angle) + 50
    y = 25 * math.sin(angle) + 25
    hole = Part.makeCylinder(5, 10)
    hole.Placement.Base = App.Vector(x, y, 0)
    plate = plate.cut(hole)

# Create slot
slot = Part.makeBox(10, 5, 10)
slot.Placement.Base = App.Vector(45, 25, 0)
plate = plate.cut(slot)

# Create cylindrical boss
boss = Part.makeCylinder(10, 10)
boss.Placement.Base = App.Vector(50, 25, 10)
plate = plate.cut(boss)

# Smooth edges
fillet = plate.makeFillet(2, plate.Edges)

obj = doc.addObject("Part::Feature", "Plate")
obj.Shape = fillet
doc.recompute()
Import.export(doc.Objects, "../data/output/design_77_559c481d.step")
import FreeCAD
if FreeCAD.GuiUp:
    import FreeCADGui
    try:
        FreeCADGui.activeDocument().activeView().viewIsometric()
        FreeCADGui.SendMsgToActiveView('ViewFit')
    except Exception:
        pass
