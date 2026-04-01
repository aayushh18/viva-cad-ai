import math
import FreeCAD as App
import Part

doc = App.newDocument("Flange")

# Flange parameters
r_flange = 50
h_flange = 10
r_hole = 5
h_hole = 10

# Create flange
flange = Part.makeCylinder(r_flange, h_flange)

# Create hole
hole = Part.makeCylinder(r_hole, h_hole)
hole.Placement.Base = App.Vector(0, 0, h_flange / 2)

# Cut hole from flange
flange = flange.cut(hole)

# Create second hole
hole2 = hole.copy()
hole2.Placement.Base = App.Vector(0, 0, -h_flange / 2)

# Cut second hole from flange
flange = flange.cut(hole2)

obj = doc.addObject("Part::Feature", "Flange")
obj.Shape = flange

doc.recompute()
doc.recompute()

import FreeCADGui as Gui
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
