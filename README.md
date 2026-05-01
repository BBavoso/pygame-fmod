# pygame-fmod

This project is a demonstration on implementing fmod into pygame. The project includes some basic FMOD bindings for both fmod studio an the low level fmod api. It also includes a basic 3d wireframe renderer along with a very basic .obj file reader to load the 3d models.

## Video Demos

### Fmod Live Update and Volume Slider

<video src="https://github.com/user-attachments/assets/f15ecf26-6437-44bc-a654-6b106e7e7e43
" controls></video>

### 3D Wireframe model and spatialized audio

<video controls src="https://github.com/user-attachments/assets/34558570-b3e8-43ba-8c19-6dfe128d95b6"></video>

## Running the project

### External Libraries

In order to run the project you must have the fmod programmer's api downloaded.
The download can be found [HERE](https://www.fmod.com/download#fmodengine) under the `FMOD Engine` tab.
The project is setup to place the entire `FMOD Programmers API Mac` inside a folder called `libs`.

If you do this right the library files should be located at (mac example):

- `libs/FMOD Programmers API/api/core/lib/libfmodL.dylib`
- `libs/FMOD Programmers API/api/studio/lib/libfmodstudioL.dylib`

If you want to change the location of the loaded files or you're on a different opertating system, you will need to change the top of `fmod_bindings.py` and `fmod_studio_bindings.py`.

### Setup and running the project

On Mac/Linux the following command makes a new python virtual environment called .venv

`python -m venv .venv`

to activate the environment, use:

`source .venv/bin/activate`

to install the required python packages use:

`pip install -r requirements.txt`

finally run the project with

`python main.py`

### Controls

WASD - move the model further closer / left right
QE - move the model up and down
Arrow Keys - spin the model
Space Bar - Play sound from model

Drag the purple handle of the slider to change the volume level.

## Resources Used

- Game Audio Programming Principles and Practices - Guy Somberg
- [pygame docs](https://www.pygame.org/docs/)
- [pygame named colors reference](https://www.pygame.org/docs/ref/color_list.html)
- [python ctypes docs](https://docs.python.org/3/library/ctypes.html)
- [fmod core api documentation](https://www.fmod.com/docs/2.03/api/core-api-sound.html)
- [fmod studio api documentation](https://www.fmod.com/docs/2.03/studio/scripting-api-reference.html)
- [One Formula That Demystifies 3D Graphics - Tsoding](https://youtu.be/qjWkNZ0SXfo)
