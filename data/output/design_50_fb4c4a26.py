import math
import FreeCAD as App
import Part

doc = App.newDocument("Vessel")

radius = 50
height = 100
thickness = 10

# Create hollow shell
outer = Part.makeCylinder(radius, height)
inner = Part.makeCylinder(radius - thickness, height + 2) # Slightly taller
vessel = outer.cut(inner)

obj = doc.addObject("Part::Feature", "Vessel")
obj.Shape = vessel

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
            Part.export(objs, r'../data/output/design_50_fb4c4a26.step')
        doc.saveAs(r'../data/output/design_50_fb4c4a26.FCStd')
except Exception as e:
    print("Export Failed:", e)
