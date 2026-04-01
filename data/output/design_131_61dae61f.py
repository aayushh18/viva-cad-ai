import FreeCAD as App
import Part
import math
import Import

doc = App.newDocument("Tanks")

# Tank 1
tank1 = Part.makeBox(10, 10, 20)
obj1 = doc.addObject("Part::Feature", "Tank1")
obj1.Shape = tank1
doc.recompute()

# Tank 2
tank2 = Part.makeBox(10, 10, 20)
obj2 = doc.addObject("Part::Feature", "Tank2")
obj2.Shape = tank2
doc.recompute()

# Pipe Bend
bend_radius = 5
bend_length = 10
bend = Part.makeHelix(bend_radius, bend_length, 10)
bend.Placement.Base = App.Vector(15, 0, 0)
obj3 = doc.addObject("Part::Feature", "Bend")
obj3.Shape = bend
doc.recompute()

# Outlet Pipe
outlet_length = 10
outlet = Part.makeCylinder(2, outlet_length)
outlet.Placement.Base = App.Vector(25, 0, 0)
obj4 = doc.addObject("Part::Feature", "Outlet")
obj4.Shape = outlet
doc.recompute()

# Connect Tanks with Pipe Bend and Outlet Pipe
tank1_cut = tank1.cut(bend)
tank2_cut = tank2.cut(outlet)
tank1_cut = tank1_cut.cut(outlet)
tank2_cut = tank2_cut.cut(bend)

obj5 = doc.addObject("Part::Feature", "Result")
obj5.Shape = tank1_cut
doc.recompute()

Import.export(doc.Objects, "../data/output/design_131_61dae61f.step")

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
            Gui.ActiveDocument.ActiveView.fitAll()
except Exception:
    pass
