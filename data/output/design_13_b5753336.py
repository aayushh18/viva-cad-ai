import math
import FreeCAD as App
import Part

doc = App.newDocument("Plate")

# Plate dimensions
plate_length = 100
plate_width = 80
plate_thickness = 10

# Slot dimensions
slot_length = 50
slot_width = 10
slot_depth = 5

# Boss dimensions
boss_radius = 10
boss_height = 5

# Create plate
plate = Part.makeBox(plate_length, plate_width, plate_thickness)

# Create slot
slot = Part.makeBox(slot_length, slot_width, slot_depth)
slot.translate(App.Vector(25, 40, 0))

# Create boss
boss = Part.makeCylinder(boss_radius, boss_height)
boss.translate(App.Vector(50, 40, 0))

# Fuse plate, slot, and boss
result = plate.cut(slot).fuse(boss)

obj = doc.addObject("Part::Feature", "Plate")
obj.Shape = result

doc.recompute()
doc.recompute()

obj.purgeTouched()

import FreeCADGui as Gui
Gui.ActiveDocument.ActiveView.viewIsometric()
Gui.ActiveDocument.ActiveView.fitAll()

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


try:
    import Part
    import FreeCAD as App
    doc = App.ActiveDocument
    if doc:
        objs = [obj for obj in doc.Objects if hasattr(obj, 'Shape') and obj.Shape is not None]
        if objs:
            Part.export(objs, r'../data/output/design_13_b5753336.step')
        doc.saveAs(r'../data/output/design_13_b5753336.FCStd')
except Exception as e:
    print("Export Failed:", e)
