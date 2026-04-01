import FreeCAD as App
import Part

doc = App.newDocument("Flange")

# Flange parameters
outer_radius = 50
inner_radius = 20
thickness = 10
height = 20

# Create outer cylinder
outer_cyl = Part.makeCylinder(outer_radius, height)

# Create inner cylinder
inner_cyl = Part.makeCylinder(inner_radius, height + 2)

# Cut inner cylinder from outer cylinder
flange = outer_cyl.cut(inner_cyl)

# Create base plate
base_plate = Part.makeCylinder(outer_radius, thickness)

# Fuse base plate with flange
flange = flange.fuse(base_plate)

# Create holes for bolts
bolt_radius = 5
bolt_height = 10
bolt_positions = [
    App.Vector(outer_radius - 20, 0, 0),
    App.Vector(outer_radius + 20, 0, 0),
    App.Vector(0, outer_radius - 20, 0),
    App.Vector(0, outer_radius + 20, 0)
]

for pos in bolt_positions:
    bolt = Part.makeCylinder(bolt_radius, bolt_height)
    bolt.translate(pos)
    flange = flange.cut(bolt)

obj = doc.addObject("Part::Feature", "Flange")
obj.Shape = flange

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
