import FreeCAD as App
import Part

doc = App.newDocument("Viva_CAD_Final_Plant")

# 1. SUPPORT STAND & TANK
base_plate = Part.makeBox(120, 120, 10)

# Leg dimensions
r_leg = 6
h_leg = 80

# Create and place 4 legs at corners
positions = [
    App.Vector(10, 10, -h_leg),
    App.Vector(90, 10, -h_leg),
    App.Vector(10, 90, -h_leg),
    App.Vector(90, 90, -h_leg)
]

stand = base_plate
for pos in positions:
    leg = Part.makeCylinder(r_leg, h_leg)
    leg.translate(pos)
    stand = stand.fuse(leg)

# Tank (Hollow)
tank_radius = 50
tank_height = 120
tank_thickness = 10
tank = Part.makeCylinder(tank_radius, tank_height).cut(Part.makeCylinder(tank_radius - tank_thickness, tank_height + 2))
tank.translate(App.Vector(60, 60, 10))
assembly = stand.fuse(tank)

# 2. OUTLET PIPE (Hollow)
p_out_radius = 12
p_out_height = 100
p_out_thickness = 10
p_out = Part.makeCylinder(p_out_radius, p_out_height).cut(Part.makeCylinder(p_out_radius - p_out_thickness, p_out_height + 2))
p_out.rotate(App.Vector(0,0,0), App.Vector(0,1,0), 90)
p_out.translate(App.Vector(110, 60, 40)) # Tank ke side se nikla

# 3. GATE VALVE (Connected to Pipe)
v_body_radius = 18
v_body_height = 20
v_body_thickness = 10
v_body = Part.makeSphere(v_body_radius).cut(Part.makeSphere(v_body_radius - v_body_thickness))
v_body.translate(App.Vector(160, 60, 40))
v_stem_radius = 3
v_stem_height = 20
v_stem = Part.makeCylinder(v_stem_radius, v_stem_height)
v_stem.translate(App.Vector(160, 60, 55))
v_wheel_radius = 12
v_wheel_height = 10
v_wheel = Part.makeTorus(v_wheel_radius, v_wheel_height)
v_wheel.translate(App.Vector(160, 60, 75))
valve = v_body.fuse(v_stem).fuse(v_wheel)

# 4. FLOW METER (Further down the line)
fm_body_radius = 15
fm_body_height = 40
fm_body_thickness = 10
fm_body = Part.makeCylinder(fm_body_radius, fm_body_height).cut(Part.makeCylinder(fm_body_radius - fm_body_thickness, fm_body_height + 2))
fm_body.rotate(App.Vector(0,0,0), App.Vector(0,1,0), 90)
fm_body.translate(App.Vector(210, 60, 40))
fm_box_length = 20
fm_box_width = 20
fm_box_height = 15
fm_box = Part.makeBox(fm_box_length, fm_box_width, fm_box_height)
fm_box.translate(App.Vector(220, 50, 52))
flow_meter = fm_body.fuse(fm_box)

# FINAL FUSE
final_plant = assembly.fuse(p_out).fuse(valve).fuse(flow_meter)

obj = doc.addObject("Part::Feature", "DemoPlant")
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
            Gui.ActiveDocument.ActiveView.fitAll()
except Exception:
    pass
