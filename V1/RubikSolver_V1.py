"""
This is yet another Rubik's Cube solver
But this is more a project to help me learn Python
(And finally finish my own cube!)

Simple 3x3 cube only
"""

from magiccube import Cube # Module able to print a cube in 2D with its colors

# Define the Rubik's Cube as an object
class RubiksCube:

    def __init__(self) -> None:
        self.size = 3
        self.face_facets = self.size ** 2
        self.colors_map = {
            "B": "blue",
            "R": "red",
            "O": "orange",
            "G": "green",
            "W": "white",
            "Y": "yellow"
        }
        # What the cube should look like
        self.target_colors = {
            "front": "B" * 9,
            "right": "R" * 9,
            "left": "O" * 9,
            "back": "G" * 9,
            "upper": "W" * 9,
            "down": "Y" * 9
        }
        # Name of the faces
        self.faces = {
            "front": list(range(18,27)),
            "right": list(range(9,18)),
            "left": list(range(27,36)),
            "back": list(range(36,45)),
            "upper": list(range(0,9)),
            "down": list(range(45,54))
            }
        # Location of corners
        self.corners = {
            0: [0,9,38],
            1: [2,29,36],
            2: [6,11,18],
            3: [8,20,27],
            4: [15,44,51],
            5: [17,24,45],
            6: [26,33,47],
            7: [35,42,53]
        }
        # Location of edges
        self.edges = {
            0:  [1,37],
            1:  [3,10],
            2:  [5,28],
            3:  [7,19],
            4:  [12,41],
            5:  [14,21],
            6:  [16,48],
            7:  [23,30],
            8:  [25,46],
            9:  [32,39],
            10: [34,50],
            11: [43,52]
        }
        # Color characters
        self.color_char = self.colors_map.keys()
        # List of colors
        self.existing_colors = list(self.colors_map.values())
        # List of faces
        self.faces_names = list(self.faces.keys())
        # Inline string for target_colors
        self.inline_target_colors = self.inline_colors(self.target_colors)
        # Inline facet index
        self.inline_target_numbers = list(range(54))
        # What the corners should look like
        self.target_corners_colors = self.get_corners_colors(self.inline_target_colors)
        # What the edges should look like
        self.target_edges_colors = self.get_edges_colors(self.inline_target_colors)

        # Ask the user to enter the colors on each face
    def set_colors(self):
        self.now_colors = {}
        print("White face should be on top, and blue face towards the user")
        print("Colors should be entered from top-left to bottom-right")
        print("With blue face towards you, flip the cube up and down to read upper and down faces")
        for i in range(len(self.faces_names)):
            while True:
                user_input = input(f"Enter face color when {self.existing_colors[i]} facet is in center: ").upper()
                # Check if the number of inputs is correct, and if characters are in the list
                if len(user_input) == self.face_facets and all(char in self.color_char for char in user_input):
                    self.now_colors[self.faces_names[i]] = user_input
                    break
                else:
                    print(f"Only use characters from {self.color_char} on {self.face_facets} characters")
        # Keep in store the initial state
        self.now_colors = self.inline_colors(self.now_colors)
        self.initial_colors = self.now_colors
        self.now_numbers = self.find_cells()


    # Convert the faces colors into a unique string
    def inline_colors(self, color_dict):
        return "".join(color_dict[self.faces_names[i]] for i in [4, 1, 0, 2, 3, 5])

    def get_corners_colors(self, version):
        corner_color = {}
        for i in self.corners.keys():
            corner_color[i] = list(version[j] for j in self.corners[i])
        #print(corner_color)
        return corner_color

    def get_edges_colors(self, version):
        edge_color = {}
        for i in self.edges.keys():
            edge_color[i] = list(version[j] for j in self.edges[i])
        #print(edge_color)
        return edge_color

    # Find where the different cells are compared to the target configuration
    def find_cells(self):
        now_numbers = self.inline_target_numbers
        # Get the colors of corners and edges at their current location
        now_corners = self.get_corners_colors(self.now_colors)
        now_edges = self.get_edges_colors(self.now_colors)
        for i in self.corners.keys():
            for j in self.corners.keys():
            # Place the corner to its current position in the list
                if sorted(now_corners[i]) == sorted(self.target_corners_colors[j]):
                    for k in range(len(now_corners[i])):
                        now_numbers[self.corners[j][k]] = self.corners[i][k]
                    break

        for i in self.edges.keys():
            for j in self.edges.keys():
            # Place the edge to its current position in the list
                if sorted(now_edges[i]) == sorted(self.target_edges_colors[j]):
                    for k in range(len(now_edges[i])):
                        now_numbers[self.edges[j][k]] = self.edges[i][k]
                    break
        return now_numbers


    # Show the version of the cube we want (initial, target, now_colors)
    def show_cube(self, version):
        print(Cube(self.size, version))

    def rotate_clockwise(self, face):
        # Determine the changes depending on which face is moved
        if face == "front":
            permutation = list(range(6)) + [17, 14, 11, 9, 10, 45, \
                12, 13, 46, 15, 16, 47, 24, 21, 18, 25, 22, 19, 26, 23, 20,  \
                6, 28, 29, 7, 31, 32, 8] + list(range(34,45)) + \
                [33, 30, 27] + list(range(48,54))
        
        elif face == "upper":
            permutation = [6, 3, 0, 7, 4, 1, 8, 5, 2, 20, 19, 18] + list(range(12,18)) + \
                [27, 28, 29] + list(range(21,27)) + [36, 37, 38] + list(range(30,36)) + \
                [9, 10, 11] + list(range(39,54))
        
        elif face == "right":
            permutation = [38, 1, 2, 41, 4, 5, 44, 7, 8, 15, 12, 9, 16,\
                13, 10, 17, 14, 11, 0, 18, 20, 3, 22, 23, 6] + list(range(25,38)) +\
                [51, 39, 40, 48, 42, 43, 45, 18, 46, 47, 2, 49, 50, 24, 52, 53]
        
        elif face == "left":
            permutation = [0, 1, 20, 3, 4, 23, 6, 7, 26] + list(range(9,20)) + \
                [47, 21, 22, 50, 24, 25, 53, 33, 30, 27, 34, 31, 28, 35, 32, 29, 8,\
                37, 38, 5, 40, 41, 2] + list(range(43,47)) + [42, 48, 49, 39, 51, 52, 36]
        
        elif face == "back":
            permutation = [29, 32, 35] + list(range(3,9)) + [2, 10, 11, 1, 13, 14, 0] +\
                list(range(16,29)) + [53, 30, 31, 52, 33, 34, 51,42, 39, 36, 43, 40, 37,\
                44, 41, 38] + list(range(45,51)) + [9, 12, 15]
        
        elif face == "down":
            permutation = list(range(0,15)) + [42, 43, 44] + list(range(18,24)) +\
                [15, 16, 17] + list(range(27,33)) + [24, 25, 26] + list(range(36,42)) +\
                [33, 34, 35, 51, 48, 45, 52, 49, 46, 53, 50, 47]
        
        # Apply the modifications
        self.now_colors = "".join(self.now_colors[i] for i in permutation)
        self.now_numbers = list(self.now_numbers[i] for i in permutation)

    def rotate_counterclockwise(self, face):
        # A counterclockwise is simply 3 clockwise rotations
        for _ in range(3):
            self.rotate_clockwise(face)
            
    def white_cross(self):
        """
        First step of solving the Rubik's Cube
        Create a white cross on the upper face
        """
        pass
    
    def first_face(self):
        """
        Second step: complete the white (upper) face
        """
        pass

cube1 = RubiksCube()
cube1.set_colors()
print("\nTarget:")
cube1.show_cube(cube1.inline_target_colors)
print("Initial state of the cube:")
cube1.show_cube(cube1.initial_colors)
print(cube1.now_numbers)
cube1.rotate_clockwise("down")
cube1.rotate_counterclockwise("front")
print("Current state:")
cube1.show_cube(cube1.now_colors)
print(cube1.now_numbers)