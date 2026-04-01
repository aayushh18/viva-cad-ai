import math
import FreeCAD as App
import Part

doc = App.newDocument("PipeWithFlangesAndFlowMeter")

# Pipe parameters
length = 300
radius_outer = 50
radius_inner = 45

# Create hollow pipe
pipe = Part.makeCylinder(radius_outer, length).cut(Part.makeCylinder(radius_inner, length))

# Flanges at both ends
flange_outer = Part.makeCylinder(60, 10)
flange_outer.translate(App.Vector(0, 0, length / 2))
flange_inner = Part.makeCylinder(45, 10)
flange_inner.translate(App.Vector(0, 0, length / 2 + radius_outer - radius_inner))

# Fuse pipe and flanges
pipe_with_flanges = pipe.fuse(flange_outer).fuse(flange_inner)

# Digital flow meter
flow_meter_body = Part.makeCylinder(15, 40).cut(Part.makeCylinder(12, 40))
flow_meter_body.rotate(App.Vector(0,0,0), App.Vector(0,1,0), 90)
flow_meter_body.translate(App.Vector(0, 0, length / 2))

flow_meter_box = Part.makeBox(20, 20, 15)
flow_meter_box.translate(App.Vector(0, 0, length / 2 + radius_outer - radius_inner))

# Fuse pipe with flanges and flow meter
final_model = pipe_with_flanges.fuse(flow_meter_body).fuse(flow_meter_box)

obj = doc.addObject("Part::Feature", "PipeWithFlangesAndFlowMeter")
obj.Shape = final_model

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
            Part.export(objs, r'../data/output/design_8_67ee4180.step')
        doc.saveAs(r'../data/output/design_8_67ee4180.FCStd')
except Exception as e:
    print("Export Failed:", e)
