import FreeCAD as App
import Part
import math
import Import

if App.ActiveDocument:
    App.closeDocument(App.ActiveDocument.Name)

doc = App.newDocument("Gear")

# Parameters
module = 2
teeth = 20
outer_radius = 20
inner_radius = 10
width = 10
height = 10
hole_radius = 2
hole_pitch = 10

# Create outer cylinder
base = Part.makeCylinder(outer_radius, height)

# Create inner cylinder
tool1 = Part.makeCylinder(inner_radius, height)

# Position inner cylinder
tool1.translate(App.Vector(0, 0, -height/2))

# Cut inner cylinder from outer cylinder
result = base.cut(tool1)

# Create circular hole pattern
n = int(2 * math.pi * outer_radius / hole_pitch)
for i in range(n):
    angle = 2 * math.pi * i / n
    x = outer_radius * math.cos(angle)
    y = outer_radius * math.sin(angle)
    z = -height/2
    hole = Part.makeCylinder(hole_radius, height)
    hole.translate(App.Vector(x, y, z))
    result = result.cut(hole)

# Create gear teeth
teeth_radius = outer_radius / module
for i in range(teeth):
    angle = 2 * math.pi * i / teeth
    x = outer_radius * math.cos(angle)
    y = outer_radius * math.sin(angle)
    z = -height/2
    tooth = Part.makeBox(width, height, outer_radius - inner_radius)
    tooth.translate(App.Vector(x, y, z))
    result = result.cut(tooth)

# Create shaft
shaft_radius = outer_radius / 2
shaft = Part.makeCylinder(shaft_radius, height)
shaft.translate(App.Vector(0, 0, -height/2))
result = result.fuse(shaft)

# Final shape
final_shape = result

# Add to document
obj = doc.addObject("Part::Feature", "MainPart")
obj.Shape = final_shape

# Display
Part.show(final_shape)

# Recompute
doc.recompute()

# Export
Import.export(doc.Objects, "../data/output/design_51_a655f68b.step")