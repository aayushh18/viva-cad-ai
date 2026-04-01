import FreeCAD as App
import Part

doc = App.newDocument("RoundWithHoles")

radius = 50
height = 20
thickness = 5
hole_radius = 5
hole_height = 10

# Create base shape
base = Part.makeCylinder(radius, height)

# Create holes
holes = []
for i in range(4):
    angle = i * 90
    x = radius * math.cos(math.radians(angle))
    y = radius * math.sin(math.radians(angle))
    hole = Part.makeCylinder(hole_radius, hole_height)
    hole.translate(App.Vector(x, y, 0))
    holes.append(hole)

# Cut holes from base
result = base
for hole in holes:
    result = result.cut(hole)

obj = doc.addObject("Part::Feature", "RoundWithHoles")
obj.Shape = result

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
            Gui.SendMsgToActiveView("ViewFit")
except Exception:
    pass
