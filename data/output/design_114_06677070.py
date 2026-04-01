import FreeCAD as App
import Part
import math

doc = App.newDocument("InvoluteGear")

# PARAMETERS
num_teeth = 20
module = 2
pressure_angle = 20  # degrees
thickness = 10

# BASIC CALCULATIONS
pitch_diameter = module * num_teeth
pitch_radius = pitch_diameter / 2

base_radius = pitch_radius * math.cos(math.radians(pressure_angle))
outer_radius = pitch_radius + module
root_radius = pitch_radius - 1.25 * module

# INVOLUTE FUNCTION
def involute_point(rb, t):
    x = rb * (math.cos(t) + t * math.sin(t))
    y = rb * (math.sin(t) - t * math.cos(t))
    return App.Vector(x, y, 0)

# GENERATE INVOLUTE CURVE
t_max = math.sqrt((outer_radius*2 - base_radius2) / base_radius*2)

points = []
steps = 15

for i in range(steps + 1):
    t = t_max * i / steps
    pt = involute_point(base_radius, t)
    points.append(pt)

# MIRROR CURVE
mirror_points = [App.Vector(p.x, -p.y, 0) for p in reversed(points)]

# COMBINE PROFILE
profile_pts = points + mirror_points

# CLOSE PROFILE (root circle)
root_left = App.Vector(root_radius, 0, 0)
root_right = App.Vector(root_radius, 0, 0)

profile_pts.insert(0, root_left)
profile_pts.append(root_right)

wire = Part.makePolygon(profile_pts)
face = Part.Face(wire)

# EXTRUDE TO TOOTH
tooth = face.extrude(App.Vector(0, 0, thickness))

# CREATE FULL GEAR
gear = None
angle_step = 360 / num_teeth

for i in range(num_teeth):
    copy = tooth.copy()
    copy.rotate(App.Vector(0, 0, 0), App.Vector(0, 0, 1), i * angle_step)
    
    if gear is None:
        gear = copy
    else:
        gear = gear.fuse(copy)

# ADD ROOT CYLINDER
core = Part.makeCylinder(root_radius, thickness)
final_gear = core.fuse(gear)

Part.show(final_gear)
doc.recompute()

# VIEW FIT
import FreeCADGui as Gui
Gui.ActiveDocument.ActiveView.fitAll()
import FreeCAD
if FreeCAD.GuiUp:
    import FreeCADGui
    try:
        FreeCADGui.activeDocument().activeView().viewIsometric()
        FreeCADGui.SendMsgToActiveView('ViewFit')
    except Exception:
        pass
