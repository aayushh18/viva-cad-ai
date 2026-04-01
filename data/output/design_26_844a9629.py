import math
import FreeCAD as App
import Part

doc = App.newDocument("Plate")

# Plate
plate = Part.makeBox(100, 100, 10)

# Slot
slot_width = 20
slot_height = 50
slot_depth = 10
slot = Part.makeBox(slot_width, 10, slot_depth)
slot.translate(App.Vector(50, 50, 0))
plate = plate.cut(slot)

# Boss
boss_radius = 20
boss_height = 10
boss = Part.makeCylinder(boss_radius, boss_height)
boss.translate(App.Vector(50, 50, 0))
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
            Part.export(objs, r'../data/output/design_26_844a9629.step')
        doc.saveAs(r'../data/output/design_26_844a9629.FCStd')
except Exception as e:
    print("Export Failed:", e)
