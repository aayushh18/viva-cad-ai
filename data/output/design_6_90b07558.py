import math
import FreeCAD as App
import Part

doc = App.newDocument("Plate")

# Plate dimensions
length, width, thickness = 100, 80, 10

# Plate creation
plate = Part.makeBox(length, width, thickness)

# Central axis creation
axis = Part.makeCylinder(1, length + 2).cut(Part.makeCylinder(0.5, length + 2))
axis.translate(App.Vector(length/2, width/2, -1))

# Mirror features across X and Y directions
plate = plate.cut(axis)
plate = plate.fuse(Part.makeMirroredObject(plate, App.Vector(0, 0, 0), App.Vector(1, 0, 0)))
plate = plate.fuse(Part.makeMirroredObject(plate, App.Vector(0, 0, 0), App.Vector(0, 1, 0)))

obj = doc.addObject("Part::Feature", "Plate")
obj.Shape = plate

doc.recompute()
doc.recompute()

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
            Part.export(objs, r'../data/output/design_6_90b07558.step')
        doc.saveAs(r'../data/output/design_6_90b07558.FCStd')
except Exception as e:
    print("Export Failed:", e)
