import pygame
import math
from fmod_bindings import *

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

# fmod setup
fmod_system = FMOD_SYSTEM_PTR()
FMOD_System_Create(ctypes.byref(fmod_system), FMOD_VERSION)
FMOD_System_Init(fmod_system, 128, FMOD_INIT_NORMAL, None)

glitter_sound = FMOD_SOUND_PTR()
FMOD_System_CreateSound(
    fmod_system,
    b"./sounds/Glitter.aif",
    FMOD_DEFAULT,
    None,
    ctypes.byref(glitter_sound),
)

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

# - Slider -

slider = pygame.Rect(200, 200, 200, 25)
slider_handle = pygame.Rect(200, 198, 25, 29)

# coefficients to fit the formula a * e ^ (x * b)
# where x is the input percent from 0 - 1
slider_dynamic_range_db = 40
slider_power = pow(10, slider_dynamic_range_db / 20)
slider_a = 1 / slider_power
slider_b = math.log(slider_power)

while running:
    screen.fill("purple")

    mouse_held = pygame.mouse.get_pressed()
    mouse_pos = pygame.mouse.get_pos()

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            channel = FMOD_CHANNEL_PTR()
            FMOD_System_PlaySound(
                fmod_system, glitter_sound, None, False, ctypes.byref(channel)
            )

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    pygame.draw.circle(screen, "red", player_pos, 40)

    if mouse_held[0] and slider_handle.collidepoint(mouse_pos):
        slider_handle.centerx = pygame.math.clamp(
            mouse_pos[0], slider.left, slider.right
        )

    slider_normalized = (slider_handle.centerx - slider.left) / slider.width

    fmod_master_channel_group = FMOD_CHANNELGROUP_PTR()
    getmaster_result = FMOD_SYSTEM_GetMasterChannelGroup(
        fmod_system, ctypes.byref(fmod_master_channel_group)
    )
    if slider_normalized == 0:
        slider_adjusted_volume = 0
    else:
        slider_adjusted_volume = slider_a * math.exp(slider_normalized * slider_b)

    FMOD_ChannelGroup_SetVolume(fmod_master_channel_group, slider_adjusted_volume)

    pygame.draw.rect(screen, "darkgrey", slider)
    pygame.draw.rect(screen, "mediumpurple", slider_handle)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

    FMOD_System_Update(fmod_system)

FMOD_System_Release(fmod_system)
pygame.quit()
