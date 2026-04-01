import FreeCAD as App
import Part
import Import

doc = App.newDocument("Cone")
cone = Part.makeCone(10, 20, 30)
obj = doc.addObject("Part::Feature", "Cone")
obj.Shape = cone
doc.recompute()
Import.export(doc.Objects, "../data/output/design_121_48cf96d1.step")

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
