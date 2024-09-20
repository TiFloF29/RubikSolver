"""
This is yet another Rubik's Cube solver
But this is more a project to help me learn Python
(And finally finish my own cube!)

Simple 3x3 cube only
"""

from magiccube import Cube # Module able to print a cube in 2D with its colors

# Define the Rubik's Cube as an object
class RubiksCube:
    size = 3
    face_facets = size ** 2
    colors_map = {
        "B": "blue",
        "O": "orange",
        "R": "red",
        "G": "green",
        "W": "white",
        "Y": "yellow"
    }
    
    # What the cube should look like
    target_colors = {
        "front": "B" * 9,
        "right": "R" * 9,
        "left": "O" * 9,
        "back": "G" * 9,
        "upper": "W" * 9,
        "down": "Y" * 9
    }
    
    faces = ["front", "right", "left", "back", "upper", "down"]
    existing_colors = list(colors_map.values())
    
    def __init__(self) -> None:
        pass

    # Ask the user to enter the colors on each face
    def set_colors(self):
        self.now = {}
        print("White face should be on top, and blue face towards the user")
        print("Colors should be entered from top-left to bottom-right")
        print("With blue face towards you, flip the cube up and down to read upper and down faces")
        for i in range(len(self.faces)):
            while True:
                user_input = input(f"Enter face color when {self.existing_colors[i]} facet is in center: ").upper()
                # Check if the number of inputs is correct, and if characters are in the list
                if len(user_input) == self.face_facets and all(char in self.colors_map.keys() for char in user_input):
                    self.now[self.faces[i]] = user_input
                    break
                else:
                    print(f"Only use characters from {self.colors_map.keys()} on {self.face_facets} characters")
        # Keep in store the initial state
        self.initial_colors = self.now
    
    # Show the version of the cube we want (initial, target, now)
    def show_cube(self, version):
        what_version = getattr(self, version)
        cube_colors = "".join(what_version[self.faces[i]] for i in [4, 2, 0, 1, 3, 5])
        print(Cube(self.size, cube_colors))

    def rotate_clockwise(self, face):
        permutation = [6, 3, 0, 7, 4, 1, 8, 5, 2] # Permutation order of the face
        self.now[face] = "".join(self.now[face][i] for i in permutation)
        # Need to add adjacent cells behavior

    def rotate_counterclockwise(self, face):
        permutation = [2, 5, 8, 1, 4, 7, 0, 3, 6] # Permutation order of the face
        self.now[face] = "".join(self.now[face][i] for i in permutation)
        # Need to add adjacent cells behavior

cube1 = RubiksCube()
cube1.set_colors()
print("Target:")
cube1.show_cube("target_colors")
print("Initial state of the cube:")
cube1.show_cube("initial_colors")
cube1.rotate_clockwise("front")
cube1.rotate_counterclockwise("upper")
cube1.show_cube("now")