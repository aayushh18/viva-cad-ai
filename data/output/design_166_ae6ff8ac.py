import FreeCAD as App
import Part

doc = App.newDocument("Plate")

# Plate dimensions
plate_width = 100
plate_height = 50
plate_thickness = 10

# Slot dimensions
slot_width = 20
slot_height = 30
slot_thickness = 5

# Boss dimensions
boss_radius = 10
boss_height = 20

# Create plate
plate = Part.makeBox(plate_width, plate_height, plate_thickness)

# Create slot
slot = Part.makeBox(slot_width, slot_height, slot_thickness)
slot.translate(App.Vector(plate_width / 2 - slot_width / 2, plate_height / 2 - slot_height / 2, 0))

# Create boss
boss = Part.makeCylinder(boss_radius, boss_height)
boss.translate(App.Vector(plate_width / 2, plate_height / 2, 0))

# Cut slot from plate
plate = plate.cut(slot)

# Fuse boss with plate
plate = plate.fuse(boss)

obj = doc.addObject("Part::Feature", "Plate")
obj.Shape = plate

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
