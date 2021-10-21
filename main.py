from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

grass_texture = load_texture('assets/grass_block.png')
stone_texture = load_texture('assets/stone_block.png')
dirt_texture = load_texture('assets/dirt_block.png')
brick_texture = load_texture('assets/brick_block.png')
sky_texture = load_texture('assets/skybox.png')
arm_texture = load_texture('assets/arm_texture.png')
punch_sound = Audio('assets/assets_punch_sound', loop=False, autoplay=False)
block_list = [grass_texture, stone_texture, dirt_texture, brick_texture]
block_pick = 0

window.exit_button.visible = False

def update():
    global block_pick
    
    if held_keys['1']: block_pick = 0
    if held_keys['2']: block_pick = 1
    if held_keys['3']: block_pick = 2
    if held_keys['4']: block_pick = 3
    
    if  held_keys['left mouse'] or held_keys['right mouse']:
        hand.active()
    else:
        hand.passive()
        
    
    
    
        
class Voxel(Button):
    def __init__(self, position=(0, 0, 0), texture=grass_texture):
        super().__init__(
            parent=scene,
            position=position,
            model="assets/block",
            origin_y=0.5,
            texture=texture,
            color=color.color(0, 0, random.uniform(.9, 1)),
            scale=.5
        )
        

    def input(self, key):
        if self.hovered:
            
            if key == "left mouse down":
                voxel = Voxel(position=self.position + mouse.normal, texture=block_list[block_pick])
                punch_sound.play()
                
                
            if key == "right mouse down":
                punch_sound.play()
                destroy(self)
                
class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent=scene,
            model='sphere',
            texture=sky_texture,
            scale=150,
            double_sided=True
            
        )

class Hand(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            model='assets/arm',
            texture=arm_texture,
            scale=.2,
            rotation = Vec3(150, -10, 0),
            position = Vec2(.4, -.6)
        )    
    
    def active(self):
        self.rotation = Vec3(150, -10, 0),
        self.position = Vec2(.3, -.5)                   
                
    def passive(self):
        self.position = Vec2(.4, -.6)
        

for z in range(20):
    for x in range(20):
        voxel = Voxel((x, 0, z))

sky = Sky()

player = FirstPersonController()
hand = Hand()
app.run()