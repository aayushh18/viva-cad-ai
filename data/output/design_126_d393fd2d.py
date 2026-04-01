import FreeCAD as App
import Part
import Import

doc = App.newDocument("Sphere")
sphere = Part.makeSphere(10)
obj = doc.addObject("Part::Feature", "Sphere")
obj.Shape = sphere
doc.recompute()
Import.export(doc.Objects, "../data/output/design_126_d393fd2d.step")

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
