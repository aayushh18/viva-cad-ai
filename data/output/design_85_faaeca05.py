import FreeCAD as App
import Part
import math
import Import

doc = App.newDocument("Plate")
plate = Part.makeBox(100, 50, 10)

# Slot
slot_width = 20
slot_depth = 10
slot_length = 50
slot = Part.makeBox(slot_width, 10, slot_depth)
slot.Placement.Base = App.Vector(25, 25, 0)
plate = plate.cut(slot)

# Boss
boss_radius = 20
boss_height = 10
boss = Part.makeCylinder(boss_radius, boss_height)
boss.Placement.Base = App.Vector(75, 25, 0)
plate = plate.cut(boss.fuse(Part.makeCylinder(boss_radius, boss_height)))

obj = doc.addObject("Part::Feature", "Plate")
obj.Shape = plate
doc.recompute()
Import.export(doc.Objects, "../data/output/design_85_faaeca05.step")
import FreeCAD
if FreeCAD.GuiUp:
    import FreeCADGui
    try:
        FreeCADGui.activeDocument().activeView().viewIsometric()
        FreeCADGui.SendMsgToActiveView('ViewFit')
    except Exception:
        pass
