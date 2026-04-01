import FreeCAD as App
import Part

doc = App.newDocument("BoxWithFillet")

# Box dimensions
length = 20
width = 30
height = 10

# Fillet radius
fillet_radius = 2

box = Part.makeBox(length, width, height)

# Apply fillet to edges
edges = box.Edges
fillet = box.makeFillet(fillet_radius, edges)

obj = doc.addObject("Part::Feature", "BoxWithFillet")
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
