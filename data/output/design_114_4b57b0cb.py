import FreeCAD as App
import Part
import math
import Import

doc = App.newDocument("Gear")

# Define gear parameters
module = 2
teeth = 20
outer_radius = module * teeth
inner_radius = module * (teeth - 2)
height = 10

# Create gear shape
gear = Part.makeHelix(outer_radius, height, 2 * math.pi * outer_radius, 10)
gear = gear.extrude(App.Vector(0, 0, height))

# Create inner hole
hole = Part.makeCylinder(inner_radius, height)
hole.Placement.Base = App.Vector(0, 0, 0)
gear = gear.cut(hole)

obj = doc.addObject("Part::Feature", "Gear")
obj.Shape = gear
doc.recompute()
Import.export(doc.Objects, "../data/output/design_114_4b57b0cb.step")
import FreeCAD
if FreeCAD.GuiUp:
    import FreeCADGui
    try:
        FreeCADGui.activeDocument().activeView().viewIsometric()
        FreeCADGui.SendMsgToActiveView('ViewFit')
    except Exception:
        pass
