import FreeCAD as App
import Part

doc = App.newDocument("HollowCylinder")

# Parameters
length = 150  # mm
outer_radius = 20  # mm
wall_thickness = 3  # mm

# Inner radius
inner_radius = outer_radius - wall_thickness

# Create hollow cylinder
outer_cyl = Part.makeCylinder(outer_radius, length)
inner_cyl = Part.makeCylinder(inner_radius, length + 2)  # Slightly taller
hollow_cyl = outer_cyl.cut(inner_cyl)

# Add to document
obj = doc.addObject("Part::Feature", "HollowCylinder")
obj.Shape = hollow_cyl

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
