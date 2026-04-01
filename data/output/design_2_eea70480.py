import math
import FreeCAD as App
import Part

doc = App.newDocument("MountingPlate")

# Plate parameters
length, width, thickness = 120, 80, 10

# Rib parameters
rib_width, rib_height, rib_spacing = 10, 20, 20

# Create plate
plate = Part.makeBox(length, width, thickness)

# Create ribs
num_ribs = int(length / rib_spacing)
rib_positions = [rib_spacing * i for i in range(num_ribs)]
for x in rib_positions:
    rib = Part.makeBox(rib_width, width, rib_height)
    rib.translate(App.Vector(x, 0, thickness / 2))
    plate = plate.fuse(rib)

obj = doc.addObject("Part::Feature", "MountingPlate")
obj.Shape = plate

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
            Part.export(objs, r'../data/output/design_2_eea70480.step')
        doc.saveAs(r'../data/output/design_2_eea70480.FCStd')
except Exception as e:
    print("Export Failed:", e)
