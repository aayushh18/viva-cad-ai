import math
import FreeCAD as App
import Part

doc = App.newDocument("BoxWithHole")

# Box dimensions
length = 50
width = 50
height = 20

# Hole dimensions
hole_radius = 10

# Create box
box = Part.makeBox(length, width, height)

# Create hole
hole = Part.makeCylinder(hole_radius, height)
hole.Placement.Base = App.Vector(length/2, width/2, 0)

# Cut hole from box
result = box.cut(hole)

obj = doc.addObject("Part::Feature", "BoxWithHole")
obj.Shape = result

doc.recompute()
doc.recompute()

# View
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
