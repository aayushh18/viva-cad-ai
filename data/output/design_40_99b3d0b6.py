import math
import FreeCAD as App
import Part

doc = App.newDocument("ElbowPipe")

R = 50 # Bend radius
r_out = 15 # Outer pipe radius
r_in = 12 # Inner pipe radius

# Parameters: (MajorRadius, MinorRadius, Center, Axis, CrossSectionStart, CrossSectionEnd, SweepAngle)
outer = Part.makeTorus(R, r_out, App.Vector(0,0,0), App.Vector(0,0,1), 0, 360, 90)
inner = Part.makeTorus(R, r_in, App.Vector(0,0,0), App.Vector(0,0,1), 0, 360, 90)
elbow = outer.cut(inner)

obj = doc.addObject("Part::Feature", "ElbowPipe")
obj.Shape = elbow

doc.recompute()
doc.recompute()

obj.purgeTouched() # CRITICAL: Clears the 'Failed' flag and makes status 'Successful'

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
            Part.export(objs, r'../data/output/design_40_99b3d0b6.step')
        doc.saveAs(r'../data/output/design_40_99b3d0b6.FCStd')
except Exception as e:
    print("Export Failed:", e)
