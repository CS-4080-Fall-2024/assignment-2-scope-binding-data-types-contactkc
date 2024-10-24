'''
Design a data structure to represent a Rubik’s Cube and store its state in memory. The
cube can have an arbitrary number of tiles per side (e.g., 3x3, 4x4, 5x5).
Things to Consider:
- Cube Size: The cube can be of any size (e.g., 3x3, 4x4, 5x5). Your solution should be
flexible enough to handle cubes with different numbers of tiles per side.
- Layer Rotation: Since it's a Rubik's Cube, layers (rows, columns, or faces) need to be
rotatable. Think about how rotating a layer affects adjacent sides and how to efficiently
update the cube's state in memory.
'''

class RubiksCube:
    def __init__(self, size):
        '''
        Initialize a cube with the given size

        :param size: size of the cube e.g. 3x3, 4x4, 5x5 (number of tiles per side)
        '''
        self.size = size
        self.cube = self.initialize()

    def initialize(self):
        '''
        Initialize cube with a default solved state

        :return: a 3D list representing the cube
        '''
        # Array of the colors
        colors = ['W', 'R', 'G', 'B', 'O', 'Y']
        # Returns a cube with 6 faces, each filled with a single color
        return [[[colors[i]] * self.size for _ in range(self.size)] for i in range(6)]
    
    def rotate_face(self, face_idx):
        '''
        Rotates the face of the cube clockwise

        :param face_idx: Index of face to rotate (0-5)
        '''
        # Rotates the 2D face of matrix clockwise
        face = self.cube[face_idx]
        self.cube[face_idx] = [list(reversed(col)) for col in zip(*face)]

        # Rotates the adjacent side
        self.adj_faces(face_idx)

    def rotate_layer(self, layer_idx, dir):
        '''
        Rotates a layer of the cube

        :param layer_idx: index of the layer to rotate
        :param dir: clockwise (c) or counter clockwise (cc) direction to rotate
        '''
        if dir == 'c':
            self.rotate_face(layer_idx)
        elif dir == 'cc': 
            self.rotate_face(layer_idx)
            self.rotate_face(layer_idx)  # To rotate it back counter clockwise
    
    def adj_faces(self, face_idx):
        '''
        Updates adjacent face when a face is rotated

        :param face_idx: Index of face to rotate (0-5)
        '''
        if face_idx == 0:  # Front face
            top_row = self.cube[5][0]  # Top face
            right_col = [self.cube[3][i][0] for i in range(self.size)]  # Right face
            bottom_row = self.cube[4][2]  # Bottom face
            left_col = [self.cube[1][i][2] for i in range(self.size)]  # Left face

            self.cube[5][0] = left_col[::-1]  # Top row -> reversed left column
            for i in range(self.size):
                self.cube[3][i][0] = top_row[i]  # Right column -> top row
            self.cube[4][2] = right_col[::-1]  # Bottom row -> reversed right column
            for i in range(self.size):
                self.cube[1][i][2] = bottom_row[i]  # Left column -> bottom row

        elif face_idx == 1:  # Left face
            top_col = [self.cube[5][i][0] for i in range(self.size)]  # Top face
            front_col = [self.cube[0][i][0] for i in range(self.size)]  # Front face
            bottom_col = [self.cube[4][i][0] for i in range(self.size)]  # Bottom face
            back_col = [self.cube[2][i][2] for i in range(self.size)]  # Back face reversed

            for i in range(self.size):
                self.cube[5][i][0] = back_col[::-1][i]  # Top face -> reversed back column
                self.cube[0][i][0] = top_col[i]         # Front face -> top column
                self.cube[4][i][0] = front_col[i]       # Bottom face -> front column
                self.cube[2][i][2] = bottom_col[::-1][i]

    def display(self):
        '''
        Prints state of cube
        '''
        for i in range(6):
            print(f"Face {i}:")
            for row in self.cube[i]:
                print(" ".join(row))
            print()

# Testing to show the faces changing
def main():
    size = 3
    cube = RubiksCube(size)
    cube.display()

    print('rotate face')
    cube.rotate_face(0)
    cube.display()

    print('rotate layer')
    cube.rotate_layer(1, 'cc')
    cube.display()

main()