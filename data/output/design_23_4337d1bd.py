import math
import FreeCAD as App
import Part

doc = App.newDocument("Flange")

# Base
base = Part.makeCylinder(50, 10)

# Inner hole
hole = Part.makeCylinder(20, 10)
hole.Placement.Base = App.Vector(0, 0, 5)

base = base.cut(hole)

# Bolt holes
for i in range(6):
    angle = math.radians(i * 60)
    x = 35 * math.cos(angle)
    y = 35 * math.sin(angle)

    hole = Part.makeCylinder(5, 10)
    hole.Placement.Base = App.Vector(x, y, 0)

    base = base.cut(hole)

obj = doc.addObject("Part::Feature", "Flange")
obj.Shape = base

doc.recompute()
doc.recompute()

import FreeCADGui as Gui
Gui.ActiveDocument.ActiveView.viewIsometric()
Gui.ActiveDocument.ActiveView.fitAll()

obj.purgeTouched()

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
            Part.export(objs, r'../data/output/design_23_4337d1bd.step')
        doc.saveAs(r'../data/output/design_23_4337d1bd.FCStd')
except Exception as e:
    print("Export Failed:", e)
