import FreeCAD as App
import Part

doc = App.newDocument("Plate")

# Plate
plate = Part.makeBox(150, 100, 10)

# Holes
hole_radius = 5
hole_positions = [
    App.Vector(10, 10, 0),
    App.Vector(140, 10, 0),
    App.Vector(10, 90, 0),
    App.Vector(140, 90, 0)
]
for pos in hole_positions:
    hole = Part.makeCylinder(hole_radius, 10)
    hole.translate(pos)
    plate = plate.cut(hole)

# Slot
slot_length = 60
slot_width = 12
slot = Part.makeBox(slot_length, slot_width, 10)
slot.translate(App.Vector(70, 50, 0))

# Boss
boss_radius = 15
boss_height = 30
boss = Part.makeCylinder(boss_radius, boss_height)
boss.translate(App.Vector(75, 50, 0))

# Fillet
fillet_radius = 2
plate = Part.makeFillet(plate, fillet_radius)

# Final shape
final_shape = plate.fuse(slot).fuse(boss)

# Add to document
obj = doc.addObject("Part::Feature", "Plate")
obj.Shape = final_shape

# Recompute
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
            Gui.ActiveDocument.ActiveView.fitAll()
except Exception:
    pass
