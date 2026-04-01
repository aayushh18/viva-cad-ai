import FreeCAD as App
import Part

doc = App.newDocument("Flange")

# Base shape
base = Part.makeCylinder(50, 10)

# Center hole
center_hole = Part.makeCylinder(20, 10)
center_hole.Placement.Base = App.Vector(0, 0, 0)
base = base.cut(center_hole)

# Hole positions
hole_positions = [
    App.Vector(-25, 0, 0),
    App.Vector(25, 0, 0),
    App.Vector(0, -25, 0),
    App.Vector(0, 25, 0),
    App.Vector(-15, -15, 0),
    App.Vector(15, 15, 0)
]

# Create holes
for pos in hole_positions:
    hole = Part.makeCylinder(5, 10)
    hole.Placement.Base = pos
    base = base.cut(hole)

# Fillet edges
fillet = base.makeFillet(2, base.Edges)

obj = doc.addObject("Part::Feature", "Flange")
obj.Shape = fillet

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
