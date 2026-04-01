import FreeCAD as App
import Part

doc = App.newDocument("TJoint_Fixed")

# Main Pipe (Horizontal)
main = Part.makeCylinder(15, 80)
main.rotate(App.Vector(0,0,0), App.Vector(0,1,0), 90) # Lay it down

# Side Pipe (Vertical - starting from middle of main)
side = Part.makeCylinder(15, 40)
side.translate(App.Vector(40, 0, 0)) # Move to middle of 80mm main pipe

# Join them
t_joint = main.fuse(side)

obj = doc.addObject("Part::Feature", "TJoint")
obj.Shape = t_joint

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
