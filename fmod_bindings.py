import ctypes

# Import FMOD dynamic library
_fmod = ctypes.CDLL("libs/FMOD Programmers API/api/core/lib/libfmodL.dylib")

FMOD_VERSION = 0x00020313

# --- fmod primative types ---

FMOD_RESULT = ctypes.c_int
FMOD_OK = 0

FMOD_MODE = ctypes.c_uint
FMOD_DEFAULT = 0x00000000

FMOD_INITFLAGS = ctypes.c_uint
FMOD_INIT_NORMAL = 0x00000000

FMOD_BOOL = ctypes.c_int

# --- fmod struct types ---

# fmt: off

class FMOD_SYSTEM(ctypes.Structure): pass
FMOD_SYSTEM_PTR = ctypes.POINTER(FMOD_SYSTEM)

class FMOD_SOUND(ctypes.Structure): pass
FMOD_SOUND_PTR = ctypes.POINTER(FMOD_SOUND)

class FMOD_CHANNELGROUP(ctypes.Structure): pass
FMOD_CHANNELGROUP_PTR = ctypes.POINTER(FMOD_CHANNELGROUP)

class FMOD_CREATESOUNDEXINFO(ctypes.Structure): pass
FMOD_CREATESOUNDEXINFO_PTR = ctypes.POINTER(FMOD_CREATESOUNDEXINFO)

class FMOD_CHANNEL(ctypes.Structure): pass
FMOD_CHANNEL_PTR = ctypes.POINTER(FMOD_CHANNEL)

# fmt: on


class FMOD_VECTOR(ctypes.Structure):
    _fields_ = [
        ("x", ctypes.c_float),
        ("y", ctypes.c_float),
        ("z", ctypes.c_float),
    ]


FMOD_VECTOR_PTR = ctypes.POINTER(FMOD_VECTOR)


class FMOD_3D_ATTRIBUTES(ctypes.Structure):
    _fields_ = [
        ("position", FMOD_VECTOR),
        ("velocity", FMOD_VECTOR),
        ("forward", FMOD_VECTOR),
        ("up", FMOD_VECTOR),
    ]


FMOD_3D_ATTRIBUTES_PTR = ctypes.POINTER(FMOD_3D_ATTRIBUTES)


# --- fmod functions ---


# FMOD_RESULT F_API FMOD_System_Create (
#   FMOD_SYSTEM **system,
#   unsigned int headerversion
# );
FMOD_System_Create = _fmod.FMOD_System_Create
FMOD_System_Create.restype = FMOD_RESULT
FMOD_System_Create.argtypes = [ctypes.POINTER(FMOD_SYSTEM_PTR), ctypes.c_uint]


# FMOD_RESULT F_API FMOD_System_Init (
#   FMOD_SYSTEM *system,
#   int maxchannels,
#   FMOD_INITFLAGS flags,
#   void *extradriverdata
# );
FMOD_System_Init = _fmod.FMOD_System_Init
FMOD_System_Init.restype = FMOD_RESULT
FMOD_System_Init.argtypes = [
    FMOD_SYSTEM_PTR,
    ctypes.c_int,
    FMOD_INITFLAGS,
    ctypes.c_void_p,
]


# FMOD_RESULT F_API FMOD_System_Release (FMOD_SYSTEM *system);
FMOD_System_Release = _fmod.FMOD_System_Release
FMOD_System_Release.restype = FMOD_RESULT
FMOD_System_Release.argtypes = [FMOD_SYSTEM_PTR]


# FMOD_RESULT F_API FMOD_System_CreateSound (
#   FMOD_SYSTEM *system,
#   const char *name_or_data,
#   FMOD_MODE mode,
#   FMOD_CREATESOUNDEXINFO *exinfo,
#   FMOD_SOUND **sound
# );
FMOD_System_CreateSound = _fmod.FMOD_System_CreateSound
FMOD_System_CreateSound.restype = FMOD_RESULT
FMOD_System_CreateSound.argtypes = [
    FMOD_SYSTEM_PTR,
    ctypes.c_char_p,
    FMOD_MODE,
    FMOD_CREATESOUNDEXINFO_PTR,
    ctypes.POINTER(FMOD_SOUND_PTR),
]


# FMOD_RESULT F_API FMOD_System_PlaySound (
#   FMOD_SYSTEM *system,
#   FMOD_SOUND *sound,
#   FMOD_CHANNELGROUP *channelgroup,
#   FMOD_BOOL paused,
#   FMOD_CHANNEL **channel
# );
FMOD_System_PlaySound = _fmod.FMOD_System_PlaySound
FMOD_System_PlaySound.restype = FMOD_RESULT
FMOD_System_PlaySound.argtypes = [
    FMOD_SYSTEM_PTR,
    FMOD_SOUND_PTR,
    FMOD_CHANNELGROUP_PTR,
    FMOD_BOOL,
    ctypes.POINTER(FMOD_CHANNEL_PTR),
]


# FMOD_RESULT F_API FMOD_System_Update (FMOD_SYSTEM *system);
FMOD_System_Update = _fmod.FMOD_System_Update
FMOD_System_Update.restype = FMOD_RESULT
FMOD_System_Update.argtypes = [FMOD_SYSTEM_PTR]

# FMOD_RESULT F_API FMOD_ChannelGroup_SetVolume(
#   FMOD_CHANNELGROUP *channelgroup,
#   float volume
# );
FMOD_ChannelGroup_SetVolume = _fmod.FMOD_ChannelGroup_SetVolume
FMOD_ChannelGroup_SetVolume.restype = FMOD_RESULT
FMOD_ChannelGroup_SetVolume.argtypes = [FMOD_CHANNELGROUP_PTR, ctypes.c_float]


# FMOD_RESULT F_API FMOD_System_GetMasterChannelGroup (
#   FMOD_SYSTEM *system,
#   FMOD_CHANNELGROUP **channelgroup
# );
FMOD_SYSTEM_GetMasterChannelGroup = _fmod.FMOD_System_GetMasterChannelGroup
FMOD_SYSTEM_GetMasterChannelGroup.restype = FMOD_RESULT
FMOD_SYSTEM_GetMasterChannelGroup.argtypes = [
    FMOD_SYSTEM_PTR,
    ctypes.POINTER(FMOD_CHANNELGROUP_PTR),
]
