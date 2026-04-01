import math
import FreeCAD as App
import Part

doc = App.newDocument("Plate")

# Plate dimensions
plate_length = 100
plate_width = 80
plate_thickness = 10

# Slot dimensions
slot_length = 40
slot_width = 10

# Boss dimensions
boss_radius = 20
boss_height = 10

# Create plate
plate = Part.makeBox(plate_length, plate_width, plate_thickness)

# Create slot
slot = Part.makeBox(slot_length, slot_width, plate_thickness)
slot.translate(App.Vector(plate_length / 2 - slot_length / 2, plate_width / 2 - slot_width / 2, 0))

# Create boss
boss = Part.makeCylinder(boss_radius, boss_height)
boss.translate(App.Vector(plate_length / 2, plate_width / 2, plate_thickness))

# Cut slot from plate
plate = plate.cut(slot)

# Fuse boss with plate
plate = plate.fuse(boss)

obj = doc.addObject("Part::Feature", "Plate")
obj.Shape = plate

doc.recompute()
doc.recompute()

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
            Part.export(objs, r'../data/output/design_22_1300c4aa.step')
        doc.saveAs(r'../data/output/design_22_1300c4aa.FCStd')
except Exception as e:
    print("Export Failed:", e)
