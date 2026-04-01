import FreeCAD as App
import Part
import math
import Import

doc = App.newDocument("DN50 Flange")

# Create base circle
base_radius = 25
base = Part.makeCircle(base_radius)

# Create bolt holes
bolt_radius = 5
bolt_distance = 50
bolt_count = 8
bolt_angle = 360 / bolt_count
bolt_positions = []
for i in range(bolt_count):
    angle = math.radians(i * bolt_angle)
    x = (bolt_distance / 2) * math.cos(angle)
    y = (bolt_distance / 2) * math.sin(angle)
    bolt_positions.append(App.Vector(x, y, 0))

# Create bolt holes
bolts = Part.makeCylinder(bolt_radius, 10)
bolts = bolts.copy()
for position in bolt_positions:
    bolts.translate(position)
bolts = Part.Compound([bolts])

# Create flange
flange = base.copy()
flange = flange.cut(bolts)

obj = doc.addObject("Part::Feature", "DN50 Flange")
obj.Shape = flange
doc.recompute()
Import.export(doc.Objects, "../data/output/design_67_9801c688.step")
import FreeCAD
if FreeCAD.GuiUp:
    import FreeCADGui
    try:
        FreeCADGui.activeDocument().activeView().viewIsometric()
        FreeCADGui.SendMsgToActiveView('ViewFit')
    except Exception:
        pass
