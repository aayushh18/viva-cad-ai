import FreeCAD as App
import Part

doc = App.newDocument("MountingPlate")

# Plate dimensions
plate_width = 100
plate_height = 100
plate_thickness = 10

# Corner hole dimensions
hole_diameter = 10
hole_depth = 20

# Create plate
plate = Part.makeBox(plate_width, plate_height, plate_thickness)

# Create corner holes
hole_positions = [
    App.Vector(0, 0, -hole_depth),
    App.Vector(plate_width, 0, -hole_depth),
    App.Vector(0, plate_height, -hole_depth),
    App.Vector(plate_width, plate_height, -hole_depth)
]

for pos in hole_positions:
    hole = Part.makeCylinder(hole_diameter, hole_depth)
    hole.translate(pos)
    plate = plate.cut(hole)

obj = doc.addObject("Part::Feature", "MountingPlate")
obj.Shape = plate

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
