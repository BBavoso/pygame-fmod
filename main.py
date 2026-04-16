import pygame
import math
from fmod_studio_bindings import *
from fmod_bindings import FMOD_INIT_NORMAL, FMOD_3D_ATTRIBUTES, FMOD_VECTOR
from render_3d import Model

# pygame setup
pygame.init()
# screen = pygame.display.set_mode((1280, 720))
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
running = True
dt = 0

# fmod setup
fmod_studio_system = FMOD_STUDIO_SYSTEM_PTR()
FMOD_Studio_System_Create(ctypes.byref(fmod_studio_system), FMOD_VERSION)
FMOD_Studio_System_Initialize(
    fmod_studio_system, 128, FMOD_STUDIO_INIT_LIVEUPDATE, FMOD_INIT_NORMAL, None
)

master_bank = FMOD_STUDIO_BANK_PTR()
FMOD_Studio_System_LoadBankFile(
    fmod_studio_system,
    b"fmod-banks/Desktop/Master.bank",
    FMOD_STUDIO_LOAD_BANK_NORMAL,
    ctypes.byref(master_bank),
)

master_strings_bank = FMOD_STUDIO_BANK_PTR()
FMOD_Studio_System_LoadBankFile(
    fmod_studio_system,
    b"fmod-banks/Desktop/Master.strings.bank",
    FMOD_STUDIO_LOAD_BANK_NORMAL,
    ctypes.byref(master_strings_bank),
)

FMOD_Studio_System_SetNumListeners(fmod_studio_system, 1)

FMOD_Studio_System_SetListenerAttributes(
    fmod_studio_system, 0, None, FMOD_VECTOR(0, 0, 0)
)

# - Slider -

slider = pygame.Rect(200, 100, 200, 25)
slider.centerx = screen.get_width() / 2
slider_handle = pygame.Rect(0, 0, 25, 29)
slider_handle.center = (slider.right, slider.centery)

# coefficients to fit the formula a * e ^ (x * b)
# where x is the input percent from 0 - 1
slider_dynamic_range_db = 40
slider_power = pow(10, slider_dynamic_range_db / 20)
slider_a = 1 / slider_power
slider_b = math.log(slider_power)

# Model

model_3d = Model("models/Cube.obj", pygame.Vector3(0, 0, 3))

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
            glitter_event = FMOD_STUDIO_EVENTDESCRIPTION_PTR()
            get_event_result = FMOD_Studio_System_GetEvent(
                fmod_studio_system, b"event:/Glitter", ctypes.byref(glitter_event)
            )
            (get_event_result)
            glitter_event_instance = FMOD_STUDIO_EVENTINSTANCE_PTR()
            FMOD_Studio_EventDescription_CreateInstance(
                glitter_event, ctypes.byref(glitter_event_instance)
            )

            attibutes_3d = FMOD_3D_ATTRIBUTES(
                FMOD_VECTOR(
                    model_3d.position.x, model_3d.position.y, model_3d.position.z
                ),
                FMOD_VECTOR(0, 0, 0),
                FMOD_VECTOR(0, 0, -1),
                FMOD_VECTOR(0, 1, 0),
            )
            FMOD_Studio_EventInstance_Set3DAttributes(
                glitter_event_instance, ctypes.byref(attibutes_3d)
            )
            FMOD_Studio_EventInstance_Start(glitter_event_instance)
            FMOD_Studio_EventInstance_Release(glitter_event_instance)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        model_3d.position.z += 10 * dt
    if keys[pygame.K_s]:
        model_3d.position.z -= 10 * dt
    if keys[pygame.K_d]:
        model_3d.position.x += 10 * dt
    if keys[pygame.K_a]:
        model_3d.position.x -= 10 * dt
    if keys[pygame.K_e]:
        model_3d.position.y += 10 * dt
    if keys[pygame.K_q]:
        model_3d.position.y -= 10 * dt
    if keys[pygame.K_RIGHT]:
        model_3d.rotate_xz(math.pi * dt)
    if keys[pygame.K_LEFT]:
        model_3d.rotate_xz(-math.pi * dt)
    if keys[pygame.K_UP]:
        model_3d.rotate_yz(math.pi * dt)
    if keys[pygame.K_DOWN]:
        model_3d.rotate_yz(-math.pi * dt)

    model_3d.draw_wireframe(screen)

    if mouse_held[0] and slider_handle.collidepoint(mouse_pos):
        slider_handle.centerx = pygame.math.clamp(
            mouse_pos[0], slider.left, slider.right
        )

    slider_normalized = (slider_handle.centerx - slider.left) / slider.width

    if slider_normalized == 0:
        slider_adjusted_volume = 0
    else:
        slider_adjusted_volume = slider_a * math.exp(slider_normalized * slider_b)

    master_bus = FMOD_STUDIO_BUS_PTR()
    FMOD_Studio_System_GetBus(fmod_studio_system, b"bus:/", ctypes.byref(master_bus))
    FMOD_Studio_Bus_SetVolume(master_bus, slider_normalized)

    pygame.draw.rect(screen, "darkgrey", slider)
    pygame.draw.rect(screen, "mediumpurple", slider_handle)

    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

    FMOD_Studio_System_Update(fmod_studio_system)

FMOD_Studio_System_Release(fmod_studio_system)
pygame.quit()
