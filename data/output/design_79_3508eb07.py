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
num_bolts = 6

base = Part.makeCylinder(outer_diameter / 2, thickness)
center = Part.makeCylinder(inner_diameter / 2, thickness)
base = base.cut(center)

bolt_circle = Part.makeCircle(bolt_circle_diameter / 2, App.Vector(0, 0, thickness / 2))
bolt_holes = []
for i in range(num_bolts):
    angle = math.radians(i * 360 / num_bolts)
    x = bolt_circle_diameter / 2 * math.cos(angle)
    y = bolt_circle_diameter / 2 * math.sin(angle)
    hole = Part.makeCylinder(bolt_diameter / 2, thickness)
    hole.Placement.Base = App.Vector(x, y, 0)
    bolt_holes.append(hole)

for hole in bolt_holes:
    base = base.cut(hole)

obj = doc.addObject("Part::Feature", "Flange")
obj.Shape = base
doc.recompute()
Import.export(doc.Objects, "../data/output/design_79_3508eb07.step")
import FreeCAD
if FreeCAD.GuiUp:
    import FreeCADGui
    try:
        FreeCADGui.activeDocument().activeView().viewIsometric()
        FreeCADGui.SendMsgToActiveView('ViewFit')
    except Exception:
        pass
