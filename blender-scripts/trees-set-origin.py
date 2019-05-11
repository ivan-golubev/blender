import fnmatch

scene = bpy.context.scene
trees = [obj for obj in scene.objects if fnmatch.fnmatchcase(obj.name, "TreeLocator*")]

# to delete selection:
# bpy.ops.object.delete()
	
# apply modifiers and split by loose parts	
for t in trees:
    t.select = True	
bpy.ops.object.modifier_apply(modifier='Array')
bpy.ops.object.modifier_apply(modifier='Curve')
bpy.ops.mesh.separate(type='LOOSE')	

# for each locator: set origin to geometry
trees = [obj for obj in scene.objects if fnmatch.fnmatchcase(obj.name, "TreeLocator*")]
for t in trees:
    t.select = True
bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')