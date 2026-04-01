import FreeCAD as App
import Part

doc = App.newDocument("Flange")

# Base Plate
base = Part.makeCylinder(50, 10)

# Center Hole
center = Part.makeCylinder(20, 10)
base = base.cut(center)

# Holes
for i in range(6):
    angle = i * math.radians(60)
    x = 35 * math.cos(angle)
    y = 35 * math.sin(angle)
    
    hole = Part.makeCylinder(5, 10)
    hole.Placement.Base = App.Vector(x, y, 0)
    base = base.cut(hole) 

obj = doc.addObject("Part::Feature", "Flange")
obj.Shape = base

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
