import math
import FreeCAD as App
import Part

doc = App.newDocument("Flange")

# Flange parameters
bolt_circle = 100
bolt_diameter = 10
bolt_thickness = 5
flange_thickness = 20

# Create flange
flange = Part.makeCylinder(bolt_circle, flange_thickness)

# Create bolt holes
num_bolts = 8
angle_step = 2 * math.pi / num_bolts
bolt_holes = []

for i in range(num_bolts):
    angle = i * angle_step
    x = bolt_circle * math.cos(angle)
    y = bolt_circle * math.sin(angle)
    hole = Part.makeCylinder(bolt_diameter / 2, flange_thickness + 2)
    hole.Placement.Base = App.Vector(x, y, -1)
    bolt_holes.append(hole)

# Cut holes from flange
result = flange.cut(bolt_holes[0])
for hole in bolt_holes[1:]:
    result = result.cut(hole)

obj = doc.addObject("Part::Feature", "Flange")
obj.Shape = result

doc.recompute()
doc.recompute()

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
            Part.export(objs, r'../data/output/design_18_7249e87b.step')
        doc.saveAs(r'../data/output/design_18_7249e87b.FCStd')
except Exception as e:
    print("Export Failed:", e)
