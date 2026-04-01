import FreeCAD as App
import Part
import math
import Import

doc = App.newDocument("Tank")
base = Part.makeBox(20, 20, 0.1)
wall = Part.makeCylinder(10, 20)
wall.Placement.Base = App.Vector(0, 0, 0.1)

result = base.cut(wall)

obj = doc.addObject("Part::Feature", "Tank")
obj.Shape = result
doc.recompute()
Import.export(doc.Objects, "../data/output/design_133_2348ea4d.step")

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
