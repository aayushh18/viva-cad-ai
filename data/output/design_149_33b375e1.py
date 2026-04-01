import FreeCAD as App
import Part

doc = App.newDocument("Flange")

# Flange dimensions
radius = 30
thickness = 10
height = 20

# Create flange
flange_out = Part.makeCylinder(radius, height)
flange_in = Part.makeCylinder(radius - thickness, height + 2)
flange = flange_out.cut(flange_in)

# Create bolts
bolt_radius = 5
bolt_height = 10
bolt_positions = [
    App.Vector(0, 0, -5),
    App.Vector(0, 0, 5),
    App.Vector(-radius, 0, 0),
    App.Vector(radius, 0, 0)
]

bolts = []
for pos in bolt_positions:
    bolt = Part.makeCylinder(bolt_radius, bolt_height)
    bolt.translate(pos)
    bolts.append(bolt)

# Fuse flange and bolts
final_flange = flange
for bolt in bolts:
    final_flange = final_flange.fuse(bolt)

# Add to document
obj = doc.addObject("Part::Feature", "Flange")
obj.Shape = final_flange

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
