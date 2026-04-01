import math
import FreeCAD as App
import Part

doc = App.newDocument("Nuclear_Power_Plant")

# 1. SUPPORT STAND & TANK
base = Part.makeBox(120, 120, 10)
for x, y in [(10,10), (100,10), (10,100), (100,100)]:
    leg = Part.makeCylinder(6, 80)
    leg.translate(App.Vector(x, y, -80))
    base = base.fuse(leg)

# Tank (Hollow)
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

# 5. PRESSURE GAUGE
pg_case = Part.makeCylinder(25, 12).cut(Part.makeCylinder(23, 12))
pg_case.translate(App.Vector(0,0,2))
pg_face = Part.makeCylinder(23, 2)
pg_face.translate(App.Vector(0,0,2))
pg_needle = Part.makeBox(15, 1.5, 1)
pg_needle.translate(App.Vector(0, -0.75, 4))
pg_socket = Part.makeCylinder(5, 15)
pg_socket.rotate(App.Vector(0,0,0), App.Vector(1,0,0), 90)
pg_socket.translate(App.Vector(0, -23, 8))
gauge = pg_case.fuse(pg_face).fuse(pg_needle).fuse(pg_socket)

# 6. REACTOR VESSEL
rv_body = Part.makeCylinder(80, 200).cut(Part.makeCylinder(76, 205))
rv_body.translate(App.Vector(100, 100, 20))
rv_cap = Part.makeSphere(80)
rv_cap.translate(App.Vector(100, 100, 220))
rv_cap = rv_cap.cut(Part.makeBox(160,160,160, App.Vector(-80,-80,-100)))
rv_cap.rotate(App.Vector(0,0,0), App.Vector(0,1,0), 90)
rv_cap.translate(App.Vector(100, 100, 220))
rv = rv_body.fuse(rv_cap)

# FINAL FUSE
final_plant = assembly.fuse(p_out).fuse(valve).fuse(flow_meter).fuse(gauge).fuse(rv)

Part.show(final_plant)
doc.recompute()
doc.recompute()

try:
    import Part
    import FreeCAD as App
    doc = App.ActiveDocument
    if doc:
        objs = [obj for obj in doc.Objects if hasattr(obj, 'Shape') and obj.Shape is not None]
        if objs:
            Part.export(objs, r'../data/output/design_3_73d8421d.step')
        doc.saveAs(r'../data/output/design_3_73d8421d.FCStd')
except Exception as e:
    print("Export Failed:", e)
