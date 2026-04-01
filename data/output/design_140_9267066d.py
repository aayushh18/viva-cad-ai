import FreeCAD as App
import Part

doc = App.newDocument("LongHollowPipe")

# Parameters
length = 1000  # mm
outer_radius = 50  # mm
inner_radius = 40  # mm
flange_radius = 60  # mm
flange_thickness = 10  # mm

# Create hollow pipe
pipe_out = Part.makeCylinder(outer_radius, length)
pipe_in = Part.makeCylinder(inner_radius, length)
pipe = pipe_out.cut(pipe_in)

# Create flange
flange_out = Part.makeCylinder(flange_radius, flange_thickness)
flange_in = Part.makeCylinder(flange_radius - flange_thickness, flange_thickness)
flange = flange_out.cut(flange_in)

# Fuse flange to pipe
result = pipe.fuse(flange)

# Move flange to one end of the pipe
result.translate(App.Vector(0, 0, length - flange_thickness))

# Add to document
obj = doc.addObject("Part::Feature", "LongHollowPipe")
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
            Gui.ActiveDocument.ActiveView.fitAll()
except Exception:
    pass
