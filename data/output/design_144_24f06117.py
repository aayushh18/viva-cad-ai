import FreeCAD as App
import Part

doc = App.newDocument("Box_Fillet")

# Box dimensions
length = 100
width = 100
height = 50

# Create box
box = Part.makeBox(length, width, height)

# Fillet edges
fillet_radius = 10
edges = box.edges()
for edge in edges:
    if edge.isClosed():
        box = box.fuse(Part.makeFillet(edge, fillet_radius))

obj = doc.addObject("Part::Feature", "Box")
obj.Shape = box

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
            Gui.ActiveDocument.ActiveView.fitAll()
except Exception:
    pass
