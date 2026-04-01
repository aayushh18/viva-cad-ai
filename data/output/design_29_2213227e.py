import math
import FreeCAD as App
import Part

doc = App.newDocument("Shaft")

c1 = Part.makeCylinder(10, 20)

c2 = Part.makeCylinder(5, 30)
c2.Placement.Base = App.Vector(0, 0, 20)

shaft = c1.fuse(c2)

obj = doc.addObject("Part::Feature", "Shaft")
obj.Shape = shaft

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
