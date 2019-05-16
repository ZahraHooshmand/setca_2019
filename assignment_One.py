import numpy as np
import os
import sys
'''
# Now we can use sys to run this code for a specific input file. This is called accepting input.
file_location=sys.argv[1]
#argv[1] means after python name.py we should give the name of the input file.
#file_location = os.path.join('data','water.xyz')
#print (file_location)

xyz_file = open(file_location,'r')
data = xyz_file.readlines()
print(data)

num_atom = int(data[0])
print(num_atom)

coord_data = data[2:] #putting aside the first two lines that contain number of atoms and the name of compound
print(coord_data)

symbols = []
coordinates = []
for atom in coord_data:
    atom_data = atom.split()
    symbol = atom_data[0]
    symbols.append(symbol)
    x, y, z = float(atom_data[1]), float(atom_data[2]), float(atom_data[3])
    coordinates.append([x, y, z])

print (symbols)
print(coordinates)

#Calculate the distance between each two atoms:
for numA, atomA in enumerate(coordinates):
    for numB, atomB in enumerate(coordinates): # Avoid recalculating the distance from atomA to atomB
        if numA<numB:
            x_distance = atomA[0]-atomB[0]
            y_distance = atomA[1]-atomB[1]
            z_distance = atomA[2]-atomB[2]
            distance = np.sqrt(x_distance**2 + y_distance**2 + z_distance**2)
            if distance>0 and distance<1.5:  # Avoid printing meaningless bond lengths
                print(F'{symbols[numA]} to {symbols[numB]}: {distance:.3f}')

'''
# Now we want to learn a better way to calculate distances:
# Functions are much easier to test
def calculate_distance(atom1, atom2):

    #Using the following block not only it is easier for us to know what is happening inside the function, but also
    #if we type help (name_of_script.name_of_function), it will print this part as explanation.
    """
    Calculate the distance between two atoms.

    Parameters
    -----------------
    atom1: list
        A list of coordinates [x, y, z]
    atom2: list
        A list of coordinates [x, y, z]


    Return
    -----------------
    bond_length: float
        The distance between atoms.


    Examples
    ------------------
    >>> calculate_distance([0,0,0], [0,0,1])
    1.0
    """

    x_distance = atom1[0]-atom2[0]
    y_distance = atom1[1]-atom2[1]
    z_distance = atom1[2]-atom2[2]
    distance = np.sqrt(x_distance**2 + y_distance**2 + z_distance**2)
    return distance


# An important advice: One function, one job
# Now let's make our bond check function more general:
def bond_check(bond_distance, minimum_value=0, maximum_value=1.5): # If you give numbers to minimum_value and maximum_value it will be the default value
    """
    Check if the bond_distance is in the range of meaningful bond_length.

    Parameters
    ---------------
    bond_distance: float
        The distance between atoms.

    minimum_value: float
        A float value as the minimum bond_distance.

    maximum_value: float
        A float value as the minimum bond_distance.

    Return
    -----------------
    bond_check: True or False
        If the values are in range of bond_length or not.


    Examples
    ------------------
    >>> bond_check(0, 1.45)
    True

    >>> bond_check(0,1.7)
    False
    """

# Check that atom_distance is a float
    if not isinstance(bond_distance, float):
        raise TypeError(F'atom_distance must be type float. (bond_distance)')

    if bond_distance > minimum_value and bond_distance < maximum_value: # Here the variable should be bond_distance as it was defined in the previous line
        return True
    else:
        return False

def open_xys(filename):
    xyz_file = np.genfromtxt(fname=filename, skip_header=2, dtype='unicode')
    symbols=xyz_file[:,0]
    coord=(xyz_file[:,1:])
    coord=coord.astype(np,float)
    return symbols, coord


if __name__ == "__main__": # This tells that this is the main part of my script and let's me to import my script to do further analysis on any arbitrary two atoms
    if len(sys.argv)<2:
        raise IndexError('No file name given. Script requires an xyz file')

    xyzfilename = sys.argv[1]
    symbols, coord = open_xyz(xyzfilename)
    for numA, atomA in enumerate(coordinates):
     for numB, atomB in enumerate(coordinates): # Avoid recalculating the distance from atomA to atomB
        if numA<numB:
            distance_AB=calculate_distance(atomA, atomB) # We are using the function we defined above
            if bond_check(distance_AB, minimum_value=0, maximum_value=1.5) is True:
                print(F'{symbols[numA]} to {symbols[numB]}: {distance_AB:.3f}')
