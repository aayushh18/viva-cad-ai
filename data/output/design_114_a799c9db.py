import FreeCAD as App
import FreeCADGui as Gui
import Part
import math

doc = App.newDocument("SimpleGear")

teeth = 20
radius = 20
tooth_depth = 4
thickness = 10

gear = Part.makeCylinder(radius, thickness)

angle_step = 360 / teeth

for i in range(teeth):
    angle = math.radians(i * angle_step)
    
    x = (radius) * math.cos(angle)
    y = (radius) * math.sin(angle)
    
    tooth = Part.makeBox(4, tooth_depth, thickness)
    tooth.translate(App.Vector(x, y, 0))
    
    tooth.rotate(App.Vector(0,0,0), App.Vector(0,0,1), i * angle_step)
    
    gear = gear.fuse(tooth)

Part.show(gear)
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
