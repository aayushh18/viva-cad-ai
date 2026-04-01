import FreeCAD as App
import Part
import math
import Import

doc = App.newDocument("Flange")

outer_diameter = 100
inner_diameter = 40
thickness = 10
bolt_circle_diameter = 70
bolt_diameter = 8
num_holes = 6

base = Part.makeCylinder(outer_diameter / 2, thickness)
center = Part.makeCylinder(inner_diameter / 2, thickness)
base = base.cut(center)

bolt_circle = Part.makeCircle(bolt_circle_diameter / 2, App.Vector(0, 0, thickness / 2))
bolt_holes = []
for i in range(num_holes):
    angle = math.radians(i * 360 / num_holes)
    x = bolt_circle_diameter / 2 * math.cos(angle)
    y = bolt_circle_diameter / 2 * math.sin(angle)
    hole = Part.makeCylinder(bolt_diameter / 2, thickness)
    hole.Placement.Base = App.Vector(x, y, 0)
    base = base.cut(hole)
    bolt_holes.append(hole)

obj = doc.addObject("Part::Feature", "Flange")
obj.Shape = base
doc.recompute()
Import.export(doc.Objects, "../data/output/design_78_e4007941.step")
import FreeCAD
if FreeCAD.GuiUp:
    import FreeCADGui
    try:
        FreeCADGui.activeDocument().activeView().viewIsometric()
        FreeCADGui.SendMsgToActiveView('ViewFit')
    except Exception:
        pass
