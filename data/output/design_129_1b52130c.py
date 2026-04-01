import FreeCAD as App
import Part
import math
import Import

doc = App.newDocument("Pipe")

outer_radius = 30 / 2
inner_radius = 25 / 2
length = 200

cylinder = Part.makeCylinder(length, outer_radius)
hole = Part.makeCylinder(length, inner_radius)
hole.Placement.Base = App.Vector(0, 0, length / 2)

pipe = cylinder.cut(hole)

obj = doc.addObject("Part::Feature", "Pipe")
obj.Shape = pipe
doc.recompute()
Import.export(doc.Objects, "../data/output/design_129_1b52130c.step")

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
