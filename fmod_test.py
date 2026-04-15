import ctypes

# Import FMOD dynamic library
fmod = ctypes.CDLL("libs/FMOD Programmers API/api/core/lib/libfmodL.dylib")

FMOD_VERSION = 0x00020313

# --- FMOD types ---
FMOD_RESULT = ctypes.c_int
FMOD_OK = 0


class FMOD_SYSTEM(ctypes.Structure):
    pass


FMOD_SYSTEM_PTR = ctypes.POINTER(FMOD_SYSTEM)

FMOD_MODE = ctypes.c_uint
FMOD_DEFAULT = 0x00000000

FMOD_INITFLAGS = ctypes.c_uint
FMOD_INIT_NORMAL = 0x00000000


class FMOD_CREATESOUNDEXINFO(ctypes.Structure):
    pass


class FMOD_SOUND(ctypes.Structure):
    pass


FMOD_SOUND_PTR = ctypes.POINTER(FMOD_SOUND)


class FMOD_CHANNELGROUP(ctypes.Structure):
    pass


FMOD_CHANNELGROUP_PTR = ctypes.POINTER(FMOD_CHANNELGROUP)

FMOD_BOOL = ctypes.c_int


class FMOD_CHANNEL(ctypes.Structure):
    pass


FMOD_CHANNEL_PTR = ctypes.POINTER(FMOD_CHANNEL)

# --- FMOD functions ---

fmod.FMOD_System_Create.restype = FMOD_RESULT
fmod.FMOD_System_Create.argtypes = [ctypes.POINTER(FMOD_SYSTEM_PTR), ctypes.c_uint]

fmod.FMOD_System_Init.restype = FMOD_RESULT
fmod.FMOD_System_Init.argtypes = [
    FMOD_SYSTEM_PTR,
    ctypes.c_int,
    FMOD_INITFLAGS,
    ctypes.c_void_p,
]

fmod.FMOD_System_Release.restype = FMOD_RESULT
fmod.FMOD_System_Release.argtypes = [FMOD_SYSTEM_PTR]

fmod.FMOD_System_CreateSound.restype = FMOD_RESULT
fmod.FMOD_System_CreateSound.argtypes = [
    FMOD_SYSTEM_PTR,
    ctypes.c_char_p,
    FMOD_MODE,
    ctypes.POINTER(FMOD_CREATESOUNDEXINFO),
    ctypes.POINTER(FMOD_SOUND_PTR),
]

fmod.FMOD_System_PlaySound.restype = FMOD_RESULT
fmod.FMOD_System_PlaySound.argtypes = [
    FMOD_SYSTEM_PTR,
    FMOD_SOUND_PTR,
    FMOD_CHANNELGROUP_PTR,
    FMOD_BOOL,
    ctypes.POINTER(FMOD_CHANNEL_PTR),
]

fmod.FMOD_System_Update.restype = FMOD_RESULT
fmod.FMOD_System_Update.argtypes = [FMOD_SYSTEM_PTR]

# main
system = FMOD_SYSTEM_PTR()

fmod.FMOD_System_Create(ctypes.byref(system), FMOD_VERSION)
fmod.FMOD_System_Init(system, 128, FMOD_INIT_NORMAL, None)

sound = FMOD_SOUND_PTR()

create_sound_result = fmod.FMOD_System_CreateSound(
    system,
    b"./sounds/Glitter.aif",
    FMOD_DEFAULT,
    None,
    ctypes.byref(sound),
)

print(create_sound_result)

channel = FMOD_CHANNEL_PTR()

fmod.FMOD_System_PlaySound(system, sound, None, False, ctypes.byref(channel))

input()

fmod.FMOD_System_Release(system)
