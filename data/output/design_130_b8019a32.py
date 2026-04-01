import FreeCAD as App
import Part
import math
import Import

doc = App.newDocument("Tank")

outer_radius = 100
inner_radius = 100 - 20
height = 300

outer_cylinder = Part.makeCylinder(height, outer_radius)
inner_cylinder = Part.makeCylinder(height, inner_radius)
inner_cylinder.Placement.Base = App.Vector(0, 0, height / 2)

tank = outer_cylinder.cut(inner_cylinder)

obj = doc.addObject("Part::Feature", "Tank")
obj.Shape = tank
doc.recompute()
Import.export(doc.Objects, "../data/output/design_130_b8019a32.step")

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
