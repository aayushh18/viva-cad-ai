import FreeCAD as App
import Part

doc = App.newDocument("BoxWithHole")

# Create base box
box = Part.makeBox(20, 20, 10)

# Create cylindrical hole
hole = Part.makeCylinder(5, 10)

# Move hole to center of box
hole.translate(App.Vector(10, 10, 5))

# Cut hole from box
result = box.cut(hole)

# Add result to document
obj = doc.addObject("Part::Feature", "BoxWithHole")
obj.Shape = result

# Recompute document
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
