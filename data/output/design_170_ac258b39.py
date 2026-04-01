import FreeCAD as App
import Part

doc = App.newDocument("ElbowPipe")

# Parameters
R = 50  # Bend radius
r_out = 15  # Outer pipe radius
r_in = 12  # Inner pipe radius

# Create outer and inner torus
outer = Part.makeTorus(R, r_out, App.Vector(0,0,0), App.Vector(0,0,1), 0, 360, 90)
inner = Part.makeTorus(R, r_in, App.Vector(0,0,0), App.Vector(0,0,1), 0, 360, 90)

# Cut inner torus from outer torus
elbow = outer.cut(inner)

# Add elbow to document
obj = doc.addObject("Part::Feature", "ElbowPipe")
obj.Shape = elbow

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
