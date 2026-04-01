import FreeCAD as App
import Part

doc = App.newDocument("Demo Plant")

# 1. SUPPORT STAND & TANK
base = Part.makeBox(120, 120, 10)
for x, y in [(10,10), (100,10), (10,100), (100,100)]:
    leg = Part.makeCylinder(6, 80)
    leg.translate(App.Vector(x, y, -80))
    base = base.fuse(leg)

tank = Part.makeCylinder(50, 120).cut(Part.makeCylinder(46, 125))
tank.translate(App.Vector(60, 60, 10))
assembly = base.fuse(tank)

# 2. OUTLET PIPE (HOLLOW)
p_out = Part.makeCylinder(12, 100).cut(Part.makeCylinder(10, 110))
p_out.rotate(App.Vector(0,0,0), App.Vector(0,1,0), 90)
p_out.translate(App.Vector(110, 60, 40)) 

# 3. GATE VALVE (CONNECTED TO PIPE)
v_body = Part.makeSphere(18).cut(Part.makeSphere(15))
v_body.translate(App.Vector(160, 60, 40))
v_stem = Part.makeCylinder(3, 20)
v_stem.translate(App.Vector(160, 60, 55))
v_wheel = Part.makeTorus(12, 2)
v_wheel.translate(App.Vector(160, 60, 75))
valve = v_body.fuse(v_stem).fuse(v_wheel)

# 4. FLOW METER (FURTHER DOWN THE LINE)
fm_body = Part.makeCylinder(15, 40).cut(Part.makeCylinder(12, 40))
fm_body.rotate(App.Vector(0,0,0), App.Vector(0,1,0), 90)
fm_body.translate(App.Vector(210, 60, 40))
fm_box = Part.makeBox(20, 20, 15)
fm_box.translate(App.Vector(220, 50, 52))
flow_meter = fm_body.fuse(fm_box)

# FINAL FUSE
final_plant = assembly.fuse(p_out).fuse(valve).fuse(flow_meter)

obj = doc.addObject("Part::Feature", "Demo Plant")
obj.Shape = final_plant

doc.recompute()

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
            Gui.SendMsgToActiveView("ViewFit")
except Exception:
    pass
