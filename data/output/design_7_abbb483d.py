import math
import FreeCAD as App
import Part

doc = App.newDocument("Pro_HX_Fixed")

# 1. SUPPORT STAND
base = Part.makeBox(120, 120, 10)
for x, y in [(10,10), (100,10), (10,100), (100,100)]:
    leg = Part.makeCylinder(6, 80)
    leg.translate(App.Vector(x, y, -80))
    base = base.fuse(leg)

# 2. MAIN SHELL (HOLLOW)
shell = Part.makeCylinder(50, 180).cut(Part.makeCylinder(46, 180))
shell.rotate(App.Vector(0,0,0), App.Vector(0,1,0), 90)

# 3. END CAPS (DISHED ENDS)
def make_cap(pos_x, rot_angle):
    cap = Part.makeSphere(50)
    # Cut half sphere to make a cap
    cap = cap.cut(Part.makeBox(100,100,100, App.Vector(-50,-50,-100)))
    cap.rotate(App.Vector(0,0,0), App.Vector(0,1,0), rot_angle)
    cap.translate(App.Vector(pos_x, 0, 0))
    return cap

cap_left = make_cap(0, -90)
cap_right = make_cap(180, 90)

# 4. IN/OUT NOZZLES
n1 = Part.makeCylinder(12, 25)
n1.translate(App.Vector(40, 0, 45))
n2 = n1.copy()
n2.translate(App.Vector(100, 0, -115)) # Opposite side

hx = shell.fuse(cap_left).fuse(cap_right).fuse(n1).fuse(n2)

# 5. SUPPORT STAND + TANK
assembly = base.fuse(hx)

# 6. 90-DEGREE HOLLOW ELBOW PIPE
elbow_out = Part.makeCylinder(15, 80)
elbow_in = Part.makeCylinder(12, 80)
elbow = elbow_out.cut(elbow_in)
elbow.rotate(App.Vector(0,0,0), App.Vector(0,1,0), 90)

# 7. CONNECT ELBOW TO TOP INLET NOZZLE
elbow.translate(App.Vector(0, 0, 180))
hx = hx.cut(elbow)

obj = doc.addObject("Part::Feature", "HeatExchanger")
obj.Shape = hx

doc.recompute()
doc.recompute()

# View Adjustment
import FreeCADGui as Gui
Gui.ActiveDocument.ActiveView.viewIsometric()
Gui.ActiveDocument.ActiveView.fitAll()

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
            Part.export(objs, r'../data/output/design_7_abbb483d.step')
        doc.saveAs(r'../data/output/design_7_abbb483d.FCStd')
except Exception as e:
    print("Export Failed:", e)
