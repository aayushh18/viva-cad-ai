import FreeCAD as App
import Part

doc = App.newDocument("Hollow_Elbow_Pipe")

# Parameters
bend_radius = 80  # mm
pipe_outer_radius = 25  # mm
wall_thickness = 4  # mm

# Create outer and inner torus
outer_torus = Part.makeTorus(bend_radius, pipe_outer_radius, App.Vector(0,0,0), App.Vector(0,0,1), 0, 360, 90)
inner_torus = Part.makeTorus(bend_radius, pipe_outer_radius - wall_thickness, App.Vector(0,0,0), App.Vector(0,0,1), 0, 360, 90)

# Cut inner torus from outer torus
elbow_pipe = outer_torus.cut(inner_torus)

Part.show(elbow_pipe)
doc.recompute()