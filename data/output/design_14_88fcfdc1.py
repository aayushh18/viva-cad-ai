import math
import FreeCAD as App
import Part

doc = App.newDocument("Plate")

# Plate dimensions
plate_width = 100
plate_height = 50

# Slot dimensions
slot_width = 20
slot_height = 10
slot_x = 30
slot_y = 20

# Boss dimensions
boss_radius = 10
boss_height = 5
boss_x = 70
boss_y = 25

# Create plate
plate = Part.makeBox(plate_width, plate_height, 1)

# Create slot
slot = Part.makeBox(slot_width, slot_height, 1)
slot.translate(App.Vector(slot_x, slot_y, 0))

# Create boss
boss = Part.makeCylinder(boss_radius, boss_height)
boss.translate(App.Vector(boss_x, boss_y, 0))

# Fuse plate, slot, and boss
result = plate.cut(slot).fuse(boss)

obj = doc.addObject("Part::Feature", "Plate")
obj.Shape = result

doc.recompute()
doc.recompute()

import FreeCAD
import Part

try:
    if 'result' in locals() and result is not None:
        try:
            Part.show(result)
        except Exception:
            pass
            
    if 'doc' in locals() and doc is not None:
        doc.recompute()
        
    if FreeCAD.GuiUp:
        import FreeCADGui as Gui
        if Gui.ActiveDocument and Gui.ActiveDocument.ActiveView:
            Gui.ActiveDocument.ActiveView.viewIsometric()
            Gui.SendMsgToActiveView("ViewFit")
except Exception:
    pass
