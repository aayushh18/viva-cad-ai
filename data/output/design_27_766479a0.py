import math
import FreeCAD as App
import Part

doc = App.newDocument("DN50_Flange")

# Flange dimensions
outer_diameter = 50
wall_thickness = 5
bolt_diameter = 10
bolt_length = 20
bolt_hole_radius = 5

# Create flange
flange = Part.makeCylinder(outer_diameter, wall_thickness)

# Create bolt holes
bolt_holes = []
for i in range(8):
    angle = math.radians(i * 45)
    x = outer_diameter / 2 + bolt_hole_radius * math.cos(angle)
    y = outer_diameter / 2 + bolt_hole_radius * math.sin(angle)
    bolt_hole = Part.makeCylinder(bolt_hole_radius, bolt_length)
    bolt_hole.translate(App.Vector(x, y, 0))
    bolt_holes.append(bolt_hole)

# Fuse bolt holes into flange
for hole in bolt_holes:
    flange = flange.cut(hole)

# Create bolts
bolts = []
for i in range(8):
    angle = math.radians(i * 45)
    x = outer_diameter / 2 + bolt_diameter / 2 * math.cos(angle)
    y = outer_diameter / 2 + bolt_diameter / 2 * math.sin(angle)
    bolt = Part.makeCylinder(bolt_diameter, bolt_length)
    bolt.translate(App.Vector(x, y, 0))
    bolts.append(bolt)

# Fuse bolts into flange
for bolt in bolts:
    flange = flange.cut(bolt)

obj = doc.addObject("Part::Feature", "DN50_Flange")
obj.Shape = flange

doc.recompute()
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
