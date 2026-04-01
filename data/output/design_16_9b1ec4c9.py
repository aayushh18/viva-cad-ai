import math
import FreeCAD as App
import Part

doc = App.newDocument("BasePlate")

# Base Plate
plate = Part.makeBox(100, 100, 10)

# Cylindrical Boss
boss = Part.makeCylinder(20, 20)

# Position boss at center of plate
boss.translate(App.Vector(50, 50, 10))

# Fuse plate and boss
final_shape = plate.fuse(boss)

obj = doc.addObject("Part::Feature", "BasePlate")
obj.Shape = final_shape

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
            Part.export(objs, r'../data/output/design_16_9b1ec4c9.step')
        doc.saveAs(r'../data/output/design_16_9b1ec4c9.FCStd')
except Exception as e:
    print("Export Failed:", e)
