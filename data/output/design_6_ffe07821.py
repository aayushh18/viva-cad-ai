import math
import FreeCAD as App
import Part

doc = App.newDocument("MiniPlant")

# SUPPORT STAND
base = Part.makeBox(120, 120, 10)
for x, y in [(10,10), (100,10), (10,100), (100,100)]:
    leg = Part.makeCylinder(6, 80)
    leg.translate(App.Vector(x, y, -80))
    base = base.fuse(leg)

# TANK (HOLLOW)
tank = Part.makeCylinder(50, 120).cut(Part.makeCylinder(46, 125))
tank.translate(App.Vector(60, 60, 10))

# ASSEMBLY
assembly = base.fuse(tank)

# OUTLET PIPE (HOLLOW)
p_out = Part.makeCylinder(12, 100).cut(Part.makeCylinder(10, 110))
p_out.rotate(App.Vector(0,0,0), App.Vector(0,1,0), 90)
p_out.translate(App.Vector(110, 60, 40))

# GATE VALVE (CONNECTED TO PIPE)
v_body = Part.makeSphere(18).cut(Part.makeSphere(15))
v_body.translate(App.Vector(160, 60, 40))
v_stem = Part.makeCylinder(3, 20)
v_stem.translate(App.Vector(160, 60, 55))
v_wheel = Part.makeTorus(12, 2)
v_wheel.translate(App.Vector(160, 60, 75))
valve = v_body.fuse(v_stem).fuse(v_wheel)

# FINAL FUSE
final_plant = assembly.fuse(p_out).fuse(valve)

obj = doc.addObject("Part::Feature", "MiniPlant")
obj.Shape = final_plant

doc.recompute()
doc.recompute()

obj.purgeTouched()

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


try:
    import Part
    import FreeCAD as App
    doc = App.ActiveDocument
    if doc:
        objs = [obj for obj in doc.Objects if hasattr(obj, 'Shape') and obj.Shape is not None]
        if objs:
            Part.export(objs, r'../data/output/design_6_ffe07821.step')
        doc.saveAs(r'../data/output/design_6_ffe07821.FCStd')
except Exception as e:
    print("Export Failed:", e)
