import FreeCAD as App
import Part
import math

doc = App.newDocument("Flange")

# Flange parameters
outer_radius = 50
inner_radius = 20
thickness = 10
height = 20

# Create outer and inner cylinders
outer_cyl = Part.makeCylinder(outer_radius, height)
inner_cyl = Part.makeCylinder(inner_radius, height + 2)

# Cut inner cylinder from outer
flange = outer_cyl.cut(inner_cyl)

# Translate flange to correct position
flange.translate(App.Vector(0, 0, height))

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
