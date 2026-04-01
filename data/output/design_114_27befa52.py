import FreeCAD as App
import FreeCADGui as Gui

doc = App.newDocument("Gear")

# 🔥 IMPORTANT: load gear workbench module
import sys
import os

# Try importing gear module
try:
    import Gear
except:
    raise Exception("Gear Workbench not installed. Install from Addon Manager.")

# CREATE INVOLUTE GEAR
gear = App.ActiveDocument.addObject("Part::FeaturePython", "InvoluteGear")

Gear.InvoluteGear(gear)

# PARAMETERS (EDITABLE)
gear.NumberOfTeeth = 20
gear.Module = 2
gear.PressureAngle = 20
gear.Thickness = 10

# RECOMPUTE
doc.recompute()

Gui.ActiveDocument.ActiveView.fitAll()
import FreeCAD
if FreeCAD.GuiUp:
    import FreeCADGui
    try:
        FreeCADGui.activeDocument().activeView().viewIsometric()
        FreeCADGui.SendMsgToActiveView('ViewFit')
    except Exception:
        pass
