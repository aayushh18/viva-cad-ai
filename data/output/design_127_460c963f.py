import FreeCAD as App
import Part
import Import

doc = App.newDocument("AnnularCylinder")
inner_cyl = Part.makeCylinder(10, 20)
outer_cyl = Part.makeCylinder(20, 20)
outer_cyl.Placement.Base = App.Vector(0, 0, 20)
result = outer_cyl.cut(inner_cyl)

obj = doc.addObject("Part::Feature", "AnnularCylinder")
obj.Shape = result
doc.recompute()
Import.export(doc.Objects, "../data/output/design_127_460c963f.step")

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
