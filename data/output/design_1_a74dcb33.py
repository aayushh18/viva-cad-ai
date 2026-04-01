import FreeCAD as App
import Part

doc = App.newDocument("AnnularCylinder")

outer_radius = 50
inner_radius = 20
height = 100

outer_cyl = Part.makeCylinder(outer_radius, height)
inner_cyl = Part.makeCylinder(inner_radius, height)

annular_cyl = outer_cyl.cut(inner_cyl)

obj = doc.addObject("Part::Feature", "AnnularCylinder")
obj.Shape = annular_cyl

doc.recompute()

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
