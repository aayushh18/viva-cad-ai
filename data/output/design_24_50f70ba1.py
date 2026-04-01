import math
import FreeCAD as App
import Part

doc = App.newDocument("Tube")

r_out = 20
r_in = 15
length = 100

# Create outer tube
outer = Part.makeCylinder(r_out, length)

# Create inner tube
inner = Part.makeCylinder(r_in, length)

# Cut inner tube from outer tube
tube = outer.cut(inner)

obj = doc.addObject("Part::Feature", "Tube")
obj.Shape = tube

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
