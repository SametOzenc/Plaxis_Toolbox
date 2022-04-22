# Plaxis Toolbox

- A set of simple scripts to automate your daily work.
----
### max_core_to_use.py
![image](https://user-images.githubusercontent.com/66252675/164719180-c42a5d72-baf6-4d7e-899a-3d9ea67760c8.png)
- Changes the number of cores to be used by the solvers in the calculation process for all phases except the Initial phase

### max_number_of_steps_stored.py
![image](https://user-images.githubusercontent.com/66252675/164719737-6ec13432-a1ee-4cb5-bf75-48f627c791d5.png)
- Changes the number of steps of a calculation phase to be stored for all phases except the Initial phase

### tolerated_error.py
![image](https://user-images.githubusercontent.com/66252675/164719669-901b69cd-f4d5-486a-8ae8-6af31336d52a.png)
- Changes the tolerated error value for all phases except the Initial phase

### updated_mesh.py
- Activates the Updated Mesh option for all phases except the Initial phase

### updated_mesh_and_water_pressures.py (_Plaxis 2D Only_)
- Activates the Updated Mesh and Updated Water Pressures option for all phases except the Initial phase

### mesh_and_run.py
- Generates medium element mesh distribution and run the analysis

### delete_phases.py
- Deletes all phases except the Initial Phase

Usage instructions for Python script
------------------------------------
To use this Python script:
- Download the file
- In the Expert menu > Run Python script > Open... to the script

Version
-------
The script is tested with PLAXIS 2D V21.04, PLAXIS 2D V22.00, PLAXIS 3D V21.04, PLAXIS 3D V22.00 and with Python 3.7.4 and Python 3.8.10
