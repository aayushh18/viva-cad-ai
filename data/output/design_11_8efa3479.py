import math
import FreeCAD as App
import Part

doc = App.newDocument("Plate")

# Plate
plate = Part.makeBox(100, 100, 10)

# Slot
slot = Part.makeBox(50, 10, 10)
slot.translate(App.Vector(25, 50, 0))
plate = plate.cut(slot)

# Boss
boss = Part.makeCylinder(20, 10)
boss.translate(App.Vector(75, 50, 0))
plate = plate.cut(boss)

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
            Part.export(objs, r'../data/output/design_11_8efa3479.step')
        doc.saveAs(r'../data/output/design_11_8efa3479.FCStd')
except Exception as e:
    print("Export Failed:", e)
