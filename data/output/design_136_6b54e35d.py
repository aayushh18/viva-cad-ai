import FreeCAD as App
import Part

doc = App.newDocument("Hollow_Elbow_Pipe")

# Parameters
bend_radius = 80  # mm
outer_radius = 25  # mm
wall_thickness = 4  # mm
inner_radius = outer_radius - wall_thickness

# Create outer and inner torus
outer_torus = Part.makeTorus(bend_radius, outer_radius, App.Vector(0,0,0), App.Vector(0,0,1), 0, 360, 90)
inner_torus = Part.makeTorus(bend_radius, inner_radius, App.Vector(0,0,0), App.Vector(0,0,1), 0, 360, 90)

# Create hollow elbow pipe by cutting inner torus from outer torus
elbow_pipe = outer_torus.cut(inner_torus)

# Show the result
Part.show(elbow_pipe)

# Add the shape to the document
obj = doc.addObject("Part::Feature", "Hollow_Elbow_Pipe")
obj.Shape = elbow_pipe

# Recompute the document
doc.recompute()