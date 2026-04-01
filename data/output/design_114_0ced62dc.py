import FreeCAD as App
import FreeCADGui as Gui
import Part
import math

doc = App.newDocument("Gear")

# PARAMETERS
z = 20              # teeth
m = 2               # module
alpha = 20          # pressure angle
thickness = 10

# BASIC CALC
pitch_dia = m * z
r_pitch = pitch_dia / 2
r_base = r_pitch * math.cos(math.radians(alpha))
r_outer = r_pitch + m
r_root = r_pitch - 1.25 * m

# INVOLUTE FUNCTION
def involute(rb, t):
    return App.Vector(
        rb * (math.cos(t) + t * math.sin(t)),
        rb * (math.sin(t) - t * math.cos(t)),
        0
    )

# MAX PARAMETER
t_max = math.sqrt((r_outer*2 - r_base2) / r_base*2)

# POINTS
pts = []
steps = 10

for i in range(steps + 1):
    t = t_max * i / steps
    pts.append(involute(r_base, t))

# MIRROR
pts_mirror = [App.Vector(p.x, -p.y, 0) for p in reversed(pts)]

# ROTATE SIDES FOR TOOTH WIDTH
angle = 360 / z / 4

def rotate_points(points, angle_deg):
    res = []
    for p in points:
        ang = math.radians(angle_deg)
        x = p.x * math.cos(ang) - p.y * math.sin(ang)
        y = p.x * math.sin(ang) + p.y * math.cos(ang)
        res.append(App.Vector(x, y, 0))
    return res

left = rotate_points(pts, -angle)
right = rotate_points(pts_mirror, angle)

# ROOT CONNECTION
root_left = App.Vector(
    r_root * math.cos(math.radians(-angle)),
    r_root * math.sin(math.radians(-angle)),
    0
)

root_right = App.Vector(
    r_root * math.cos(math.radians(angle)),
    r_root * math.sin(math.radians(angle)),
    0
)

# BUILD CLOSED PROFILE
profile = [root_left] + left + right + [root_right, root_left]

wire = Part.makePolygon(profile)

# 🔥 IMPORTANT FIX: check validity
if not wire.isClosed():
    raise Exception("Wire not closed")

face = Part.Face(wire)

# EXTRUDE
tooth = face.extrude(App.Vector(0, 0, thickness))

# PATTERN
gear = None
angle_step = 360 / z

for i in range(z):
    t_copy = tooth.copy()
    t_copy.rotate(App.Vector(0, 0, 0), App.Vector(0, 0, 1), i * angle_step)
    
    if gear is None:
        gear = t_copy
    else:
        gear = gear.fuse(t_copy)

# CORE CYLINDER
core = Part.makeCylinder(r_root, thickness)

final = core.fuse(gear)

Part.show(final)
doc.recompute()

Gui.ActiveDocument.ActiveView.fitAll()
import FreeCAD
if FreeCAD.GuiUp:
    import FreeCADGui
    try:
        FreeCADGui.activeDocument().activeView().viewIsometric()
        FreeCADGui.SendMsgToActiveView('ViewFit')
    except Exception:
        pass
