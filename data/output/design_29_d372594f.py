import math
import FreeCAD as App
import Part

doc = App.newDocument("CircularPlate")

# Create a circular plate
plate = Part.makeCircle(30)

# Create a list to store the hole positions
holes = []

# Calculate the angle between each hole
angle = 2 * math.pi / 6

# Loop through each hole position
for i in range(6):
    # Calculate the x and y coordinates of the hole
    x = 30 * math.cos(i * angle)
    y = 30 * math.sin(i * angle)

    # Create a hole cylinder
    hole = Part.makeCylinder(5, 10)
    hole.Placement.Base = App.Vector(x, y, 0)

    # Add the hole to the list
    holes.append(hole)

# Fuse all the holes together
for hole in holes:
    plate = plate.cut(hole)

# Create a Part object from the plate
obj = doc.addObject("Part::Feature", "CircularPlate")
obj.Shape = plate

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
            Part.export(objs, r'../data/output/design_29_d372594f.step')
        doc.saveAs(r'../data/output/design_29_d372594f.FCStd')
except Exception as e:
    print("Export Failed:", e)
