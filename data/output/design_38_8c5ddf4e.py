import math
import FreeCAD as App
import Part

doc = App.newDocument("DemoPlant")

# 1. SUPPORT STAND & TANK
base = Part.makeBox(120, 120, 10)
for x, y in [(10,10), (100,10), (10,100), (100,100)]:
    leg = Part.makeCylinder(6, 80)
    leg.translate(App.Vector(x, y, -80))
    base = base.fuse(leg)

tank = Part.makeCylinder(50, 120).cut(Part.makeCylinder(46, 125))
tank.translate(App.Vector(60, 60, 10))
assembly = base.fuse(tank)

# 2. OUTLET PIPE (Hollow)
p_out = Part.makeCylinder(12, 100).cut(Part.makeCylinder(10, 110))
p_out.rotate(App.Vector(0,0,0), App.Vector(0,1,0), 90)
p_out.translate(App.Vector(110, 60, 40)) # Tank ke side se nikla

# 3. GATE VALVE (Connected to Pipe)
v_body = Part.makeSphere(18).cut(Part.makeSphere(15))
v_body.translate(App.Vector(160, 60, 40))
v_stem = Part.makeCylinder(3, 20)
v_stem.translate(App.Vector(160, 60, 55))
v_wheel = Part.makeTorus(12, 2)
v_wheel.translate(App.Vector(160, 60, 75))
valve = v_body.fuse(v_stem).fuse(v_wheel)

# 4. FLOW METER (Further down the line)
fm_body = Part.makeCylinder(15, 40).cut(Part.makeCylinder(12, 40))
fm_body.rotate(App.Vector(0,0,0), App.Vector(0,1,0), 90)
fm_body.translate(App.Vector(210, 60, 40))
fm_box = Part.makeBox(20, 20, 15)
fm_box.translate(App.Vector(220, 50, 52))
flow_meter = fm_body.fuse(fm_box)

# FINAL FUSE
final_plant = assembly.fuse(p_out).fuse(valve).fuse(flow_meter)

obj = doc.addObject("Part::Feature", "DemoPlant")
obj.Shape = final_plant

doc.recompute()
doc.recompute()

obj.purgeTouched()

# View Adjustment
import FreeCAD
if FreeCAD.GuiUp:
    import FreeCADGui as Gui
    if Gui.ActiveDocument and Gui.ActiveDocument.ActiveView:
        Gui.ActiveDocument.ActiveView.viewIsometric()
        Gui.ActiveDocument.ActiveView.fitAll()

try:
    import Part
    import FreeCAD as App
    doc = App.ActiveDocument
    if doc:
        objs = [obj for obj in doc.Objects if hasattr(obj, 'Shape') and obj.Shape is not None]
        if objs:
            Part.export(objs, r'../data/output/design_38_8c5ddf4e.step')
        doc.saveAs(r'../data/output/design_38_8c5ddf4e.FCStd')
except Exception as e:
    print("Export Failed:", e)
