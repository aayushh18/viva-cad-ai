import math
import FreeCAD as App
import Part

doc = App.newDocument("Plate")

# Create plate
plate = Part.makeBox(150, 100, 10)

# Create hollow boss
boss_out = Part.makeCylinder(15, 20)
boss_in = Part.makeCylinder(10, 20)
boss = boss_out.cut(boss_in)
boss.translate(App.Vector(50, 50, 0))

# Fuse boss to plate
plate = plate.fuse(boss)

# Create slot
slot = Part.makeBox(40, 10, 100)
slot.translate(App.Vector(100, 50, 0))

# Cut slot from plate
plate = plate.cut(slot)

obj = doc.addObject("Part::Feature", "Plate")
obj.Shape = plate

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
            Part.export(objs, r'../data/output/design_12_cf15eb5c.step')
        doc.saveAs(r'../data/output/design_12_cf15eb5c.FCStd')
except Exception as e:
    print("Export Failed:", e)
