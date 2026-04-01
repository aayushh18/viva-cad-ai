import FreeCAD as App
import Part

doc = App.newDocument("Pipe")

# Parameters
radius = 15
length = 200

# Create outer and inner pipes
outer = Part.makeCylinder(radius, length)
inner = Part.makeCylinder(radius - 3, length + 10)

# Cut inner pipe from outer pipe
pipe = outer.cut(inner)

# Rotate pipe to vertical position
pipe.rotate(App.Vector(0,0,0), App.Vector(0,1,0), 90)

# Add pipe to document
obj = doc.addObject("Part::Feature", "Pipe")
obj.Shape = pipe

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
