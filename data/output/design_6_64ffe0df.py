import math
import FreeCAD as App
import Part

doc = App.newDocument("Box_Fillet")

box = Part.makeBox(100, 80, 50)

fillet = box.makeFillet(5, box.Edges)

obj = doc.addObject("Part::Feature", "Box_Fillet")
obj.Shape = fillet

doc.recompute()
doc.recompute()

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
