import FreeCAD as App
import Part

doc = App.newDocument("Elbow_Fixed")

# Parameters
R = 50 # Bend radius
r = 15 # Pipe thickness

# Create torus segment (Quarter ring)
# 5th param = start angle, 6th param = end angle
elbow = Part.makeTorus(R, r, App.Vector(0,0,0), App.Vector(0,0,1), 0, 90)

obj = doc.addObject("Part::Feature", "Elbow")
obj.Shape = elbow

doc.recompute()
# Hint: Use 'V' then 'F' on keyboard in FreeCAD to fit view

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
