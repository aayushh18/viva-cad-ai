import FreeCAD as App
import Part

doc = App.newDocument("BoxWithFillet")

# Box dimensions
width, length, height = 100, 100, 20

# Create box
base = Part.makeBox(width, length, height)

# Fillet radius
fillet_radius = 10

# Create fillet edges
edges = base.edges()
for edge in edges:
    if edge.isClosed():
        fillet = Part.makeFillet(edge, fillet_radius)
        base = base.cut(fillet)

obj = doc.addObject("Part::Feature", "BoxWithFillet")
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
