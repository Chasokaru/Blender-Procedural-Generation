import bpy
import random

print ('hello world')

all_cubes = []
spacing = 2.2

# if materials exist; if not, create them
if 'Material.Red' not in bpy.data.materials:
    red_material = bpy.data.materials.new(name='Material.Red')
    red_material.diffuse_color = (1, 0, 0, 1)  # Red color
else:
    red_material = bpy.data.materials['Material.Red']
    
if 'Material.Black' not in bpy.data.materials:
    black_material = bpy.data.materials.new(name='Material.Black')
    black_material.diffuse_color = (0, 0, 0, 1)  # Black color
else:
    black_material = bpy.data.materials['Material.Black']
    
if 'Material.White' not in bpy.data.materials:
    black_material = bpy.data.materials.new(name='Material.White')
    black_material.diffuse_color = (0, 0, 0, 1)  # Black color
else:
    black_material = bpy.data.materials['Material.White']

# if materials are already created in the blender for use
RedMaterial = 'Material.Red'
BlackMaterial = 'Material.Black'
WhiteMaterial = 'Material.White'

# for generating the specific amount in specific area
for x in range(20):
    for y in range(20):
        location = (x * spacing, y * spacing, random.random() * 2)
        
        bpy.ops.mesh.primitive_cube_add(
            size=2,
            enter_editmode=False,
            align='WORLD',
            location=location,
            scale=(1,1,1))
            
        item = bpy.context.object
        if random.random() < 0.1:
            item.data.materials.append(bpy.data.materials['Material.White'])
        elif random.random() <0.4:
            item.data.materials.append(bpy.data.materials['Material.Red'])
        else:
            item.data.materials.append(bpy.data.materials['Material.Black'])