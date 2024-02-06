#!/usr/bin/env python

# Compute the center of gravity and inertia matrix of an stl (assumed homogenous)

import sys
import argparse
import numpy as np
import stl
from xml.dom.minidom import Document

def main():
    parser = argparse.ArgumentParser(description='Compute center of gravity and inertia matrix of an STL mesh.')
    parser.add_argument('mesh_path', type=str, help='Path to the STL mesh file')
    parser.add_argument('--mass' , type=float, default=1.0, help='Mass of the object in (default is 1.0 kg)')
    parser.add_argument('--scale', type=float, default=1.0, help='Scale factor for the mesh (default is  1.0)')
    args = parser.parse_args()

    # Load the STL mesh from the given file path
    mesh = stl.mesh.Mesh.from_file(args.mesh_path)

    # Scale the mesh if a scale factor was provided
    if args.scale !=  1.0:
        mesh.vectors *= args.scale

    # Get mass properties (volume, center of gravity, inertia)
    # volume = mesh.get_volume()
    volume, _, _ = mesh.get_mass_properties()
    _, _, cog, inertia = mesh.get_mass_properties_with_density(args.mass/volume)

    # Create XML elements for mass, origin, and inertia
    doc = Document()

    # Create the root element
    inertial = doc.createElement('inertial')
    doc.appendChild(inertial)

    # Create the mass element and add it to inertial
    mass = doc.createElement('mass')
    mass.setAttribute('value', str(args.mass))
    inertial.appendChild(mass)

    # Create the origin element and add it to inertial
    origin = doc.createElement('origin')
    origin.setAttribute('xyz', f"{cog[0]:.3f} {cog[1]:.3f} {cog[2]:.3f}")
    origin.setAttribute('rpy', "0  0  0")
    inertial.appendChild(origin)

    # Create the inertia element and add it to inertial
    inertia_elem = doc.createElement('inertia')
    inertia_elem.setAttribute('ixx', f"{inertia[0,0]:.2e}")
    inertia_elem.setAttribute('ixy', f"{inertia[0,1]:.2e}")
    inertia_elem.setAttribute('ixz', f"{inertia[0,2]:.2e}")
    inertia_elem.setAttribute('iyy', f"{inertia[1,1]:.2e}")
    inertia_elem.setAttribute('iyz', f"{inertia[1,2]:.2e}")
    inertia_elem.setAttribute('izz', f"{inertia[2,2]:.2e}")
    inertial.appendChild(inertia_elem)

    # Pretty-print the XML document
    pretty_xml = doc.toprettyxml(indent="    ")
    print(pretty_xml)
    return mesh

if __name__ == "__main__":
    m = main()