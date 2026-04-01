import FreeCAD as App
import Part
import math
import Import

doc = App.newDocument("Gear")

# Define gear parameters
num_teeth = 20
pitch_radius = 20
pressure_angle = 20
helix_angle = 0
axis_angle = 0
axis_direction = App.Vector(0, 0, 1)
axis_point = App.Vector(0, 0, 0)

# Create a circle for the gear
circle = Part.makeCircle(pitch_radius)

# Create a gear shape
gear = Part.Gear(num_teeth, pitch_radius, pressure_angle, helix_angle, axis_angle, axis_direction, axis_point)

# Add the gear to the document
obj = doc.addObject("Part::Feature", "Gear")
obj.Shape = gear

# Recompute the document
doc.recompute()

# Export the document to a STEP file
Import.export(doc.Objects, "../data/output/design_68_f65fe77b.step")
import FreeCAD
if FreeCAD.GuiUp:
    import FreeCADGui
    try:
        FreeCADGui.activeDocument().activeView().viewIsometric()
        FreeCADGui.SendMsgToActiveView('ViewFit')
    except Exception:
        pass
