import ctypes
from fmod_bindings import FMOD_RESULT, FMOD_INITFLAGS


# Import FMOD dynamic library
_fmod = ctypes.CDLL("libs/FMOD Programmers API/api/studio/lib/libfmodstudioL.dylib")

FMOD_VERSION = 0x00020313

# --- fmod studio primative types ---

FMOD_STUDIO_LOAD_BANK_FLAGS = ctypes.c_uint
FMOD_STUDIO_LOAD_BANK_NORMAL = 0x00000000
FMOD_STUDIO_LOAD_BANK_NONBLOCKING = 0x00000001
FMOD_STUDIO_LOAD_BANK_DECOMPRESS_SAMPLES = 0x00000002
FMOD_STUDIO_LOAD_BANK_UNENCRYPTED = 0x00000004

FMOD_STUDIO_INITFLAGS = ctypes.c_uint
FMOD_STUDIO_INIT_NORMAL = 0x00000000
FMOD_STUDIO_INIT_LIVEUPDATE = 0x00000001

FMOD_STUDIO_STOP_MODE = ctypes.c_int32
FMOD_STUDIO_STOP_ALLOWFADEOUT = 0
FMOD_STUDIO_STOP_IMMEDIATE = 1

# --- fmod studio struct types ---

# fmt: off

class FMOD_STUDIO_SYSTEM(ctypes.Structure): pass
FMOD_STUDIO_SYSTEM_PTR = ctypes.POINTER(FMOD_STUDIO_SYSTEM)

class FMOD_STUDIO_BANK(ctypes.Structure): pass
FMOD_STUDIO_BANK_PTR = ctypes.POINTER(FMOD_STUDIO_BANK)

class FMOD_STUDIO_EVENTDESCRIPTION(ctypes.Structure): pass
FMOD_STUDIO_EVENTDESCRIPTION_PTR = ctypes.POINTER(FMOD_STUDIO_EVENTDESCRIPTION)

class FMOD_STUDIO_EVENTINSTANCE(ctypes.Structure): pass
FMOD_STUDIO_EVENTINSTANCE_PTR = ctypes.POINTER(FMOD_STUDIO_EVENTINSTANCE)

class FMOD_STUDIO_BUS(ctypes.Structure): pass
FMOD_STUDIO_BUS_PTR = ctypes.POINTER(FMOD_STUDIO_BUS)

# fmt: on

# --- fmod studio functions ---

# - system -


# FMOD_RESULT F_API FMOD_Studio_System_Create(
#   FMOD_STUDIO_SYSTEM **system,
#   unsigned int headerversion
# );
FMOD_Studio_System_Create = _fmod.FMOD_Studio_System_Create
FMOD_Studio_System_Create.restype = FMOD_RESULT
FMOD_Studio_System_Create.argtypes = [
    ctypes.POINTER(FMOD_STUDIO_SYSTEM_PTR),
    ctypes.c_uint,
]


# FMOD_RESULT F_API FMOD_Studio_System_Initialize(
#   FMOD_STUDIO_SYSTEM *system,
#   int maxchannels,
#   FMOD_STUDIO_INITFLAGS studioflags,
#   FMOD_INITFLAGS flags,
#   void *extradriverdata
# );
FMOD_Studio_System_Initialize = _fmod.FMOD_Studio_System_Initialize
FMOD_Studio_System_Initialize.restype = FMOD_RESULT
FMOD_Studio_System_Initialize.argtypes = [
    FMOD_STUDIO_SYSTEM_PTR,
    ctypes.c_int,
    FMOD_STUDIO_INITFLAGS,
    FMOD_INITFLAGS,
    ctypes.c_void_p,
]


# FMOD_RESULT F_API FMOD_Studio_System_LoadBankFile(
#   FMOD_STUDIO_SYSTEM *system,
#   const char *filename,
#   FMOD_STUDIO_LOAD_BANK_FLAGS flags,
#   FMOD_STUDIO_BANK **bank
# );
FMOD_Studio_System_LoadBankFile = _fmod.FMOD_Studio_System_LoadBankFile
FMOD_Studio_System_LoadBankFile.restype = FMOD_RESULT
FMOD_Studio_System_LoadBankFile.argtypes = [
    FMOD_STUDIO_SYSTEM_PTR,
    ctypes.c_char_p,
    FMOD_STUDIO_LOAD_BANK_FLAGS,
    ctypes.POINTER(FMOD_STUDIO_BANK_PTR),
]


# FMOD_RESULT F_API FMOD_Studio_System_GetEvent(
#   FMOD_STUDIO_SYSTEM *system,
#   const char *pathOrID,
#   FMOD_STUDIO_EVENTDESCRIPTION **event
# );
FMOD_Studio_System_GetEvent = _fmod.FMOD_Studio_System_GetEvent
FMOD_Studio_System_GetEvent.restype = FMOD_RESULT
FMOD_Studio_System_GetEvent.argtypes = [
    FMOD_STUDIO_SYSTEM_PTR,
    ctypes.c_char_p,
    ctypes.POINTER(FMOD_STUDIO_EVENTDESCRIPTION_PTR),
]

# FMOD_RESULT F_API FMOD_Studio_System_Release(FMOD_STUDIO_SYSTEM *system);
FMOD_Studio_System_Release = _fmod.FMOD_Studio_System_Release
FMOD_Studio_System_Release.restype = FMOD_RESULT
FMOD_Studio_System_Release.argtypes = [FMOD_STUDIO_SYSTEM_PTR]


# FMOD_RESULT F_API FMOD_Studio_System_UnloadAll(FMOD_STUDIO_SYSTEM *system);
FMOD_Studio_System_UnloadAll = _fmod.FMOD_Studio_System_UnloadAll
FMOD_Studio_System_UnloadAll.restype = FMOD_RESULT
FMOD_Studio_System_UnloadAll.argtypes = [FMOD_STUDIO_SYSTEM_PTR]


# FMOD_RESULT F_API FMOD_Studio_System_Update(FMOD_STUDIO_SYSTEM *system);
FMOD_Studio_System_Update = _fmod.FMOD_Studio_System_Update
FMOD_Studio_System_Update.restype = FMOD_RESULT
FMOD_Studio_System_Update.argtypes = [FMOD_STUDIO_SYSTEM_PTR]


# - event description -

# FMOD_RESULT F_API FMOD_Studio_EventDescription_CreateInstance(
#   FMOD_STUDIO_EVENTDESCRIPTION *eventdescription,
#   FMOD_STUDIO_EVENTINSTANCE **instance
# );
FMOD_Studio_EventDescription_CreateInstance = (
    _fmod.FMOD_Studio_EventDescription_CreateInstance
)
FMOD_Studio_EventDescription_CreateInstance.restype = FMOD_RESULT
FMOD_Studio_EventDescription_CreateInstance.argtypes = [
    FMOD_STUDIO_EVENTDESCRIPTION_PTR,
    ctypes.POINTER(FMOD_STUDIO_EVENTINSTANCE_PTR),
]

# - event instance -

# FMOD_RESULT F_API FMOD_Studio_EventInstance_Start(FMOD_STUDIO_EVENTINSTANCE *eventinstance);
FMOD_Studio_EventInstance_Start = _fmod.FMOD_Studio_EventInstance_Start
FMOD_Studio_EventInstance_Start.restype = FMOD_RESULT
FMOD_Studio_EventInstance_Start.argtypes = [FMOD_STUDIO_EVENTINSTANCE_PTR]


# FMOD_RESULT F_API FMOD_Studio_EventInstance_Stop(
#   FMOD_STUDIO_EVENTINSTANCE *eventinstance,
#   FMOD_STUDIO_STOP_MODE mode
# );
FMOD_Studio_EventInstance_Stop = _fmod.FMOD_Studio_EventInstance_Stop
FMOD_Studio_EventInstance_Stop.restype = FMOD_RESULT
FMOD_Studio_EventInstance_Stop.argtypes = [
    FMOD_STUDIO_EVENTINSTANCE_PTR,
    FMOD_STUDIO_STOP_MODE,
]


# FMOD_RESULT F_API FMOD_Studio_EventInstance_Release(FMOD_STUDIO_EVENTINSTANCE *eventinstance);
FMOD_Studio_EventInstance_Release = _fmod.FMOD_Studio_EventInstance_Release
FMOD_Studio_EventInstance_Release.restype = FMOD_RESULT
FMOD_Studio_EventInstance_Release.argtypes = [FMOD_STUDIO_EVENTINSTANCE_PTR]


# - bus -


# FMOD_RESULT F_API FMOD_Studio_System_GetBus(
#   FMOD_STUDIO_SYSTEM *system,
#   const char *pathOrID,
#   FMOD_STUDIO_BUS **bus
# );
FMOD_Studio_System_GetBus = _fmod.FMOD_Studio_System_GetBus
FMOD_Studio_System_GetBus.restype = FMOD_RESULT
FMOD_Studio_System_GetBus.argtypes = [
    FMOD_STUDIO_SYSTEM_PTR,
    ctypes.c_char_p,
    ctypes.POINTER(FMOD_STUDIO_BUS_PTR),
]

# FMOD_RESULT F_API FMOD_Studio_Bus_SetVolume(
#   FMOD_STUDIO_BUS *bus,
#   float volume
# );
FMOD_Studio_Bus_SetVolume = _fmod.FMOD_Studio_Bus_SetVolume
FMOD_Studio_Bus_SetVolume.restype = FMOD_RESULT
FMOD_Studio_Bus_SetVolume.argtypes = [FMOD_STUDIO_BUS_PTR, ctypes.c_float]
