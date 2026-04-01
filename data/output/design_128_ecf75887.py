import FreeCAD as App
import Part
import math
import Import

doc = App.newDocument("AnnularCylinder")
outer_cyl = Part.makeCylinder(30, 50)
inner_cyl = Part.makeCylinder(20, 50)
inner_cyl.Placement.Base = App.Vector(0, 0, 0)
inner_cyl.Placement.Rotation = App.Rotation(0, 0, 1, math.pi)

annular_cyl = outer_cyl.cut(inner_cyl)

obj = doc.addObject("Part::Feature", "AnnularCylinder")
obj.Shape = annular_cyl
doc.recompute()
Import.export(doc.Objects, "../data/output/design_128_ecf75887.step")

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
