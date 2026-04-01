import FreeCAD as App
import Part
import math
import Import

doc = App.newDocument("Gear")

# Define gear parameters
num_teeth = 10
pitch_radius = 20
thickness = 10
hole_radius = 5
hole_pitch = 10

# Create gear base
gear_base = Part.makeCylinder(pitch_radius, thickness)

# Create gear teeth
gear_teeth = Part.makeCylinder(pitch_radius, thickness)
gear_teeth.Placement.Base = App.Vector(0, 0, thickness)

# Create gear hole
gear_hole = Part.makeCylinder(hole_radius, thickness)
gear_hole.Placement.Base = App.Vector(0, 0, thickness)

# Create gear
gear = gear_base.cut(gear_teeth.cut(gear_hole))

# Create gear pattern
gear_pattern = gear.copy()
gear_pattern.Placement.Rotation = App.Rotation(math.radians(360 / num_teeth), 0, 0, 1)

# Create gear assembly
gear_assembly = gear_pattern.copy()
for i in range(num_teeth - 1):
    gear_assembly = gear_assembly.fuse(gear_pattern.copy())
    gear_assembly.Placement.Base = App.Vector(0, 0, (i + 1) * pitch_radius)

# Create gear object
obj = doc.addObject("Part::Feature", "Gear")
obj.Shape = gear_assembly

# Recompute document
doc.recompute()

# Export STEP file
Import.export(doc.Objects, "../data/output/design_131_5b184b38.step")

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
