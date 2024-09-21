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
        
        self.faces = ["front", "right", "left", "back", "upper", "down"]
        self.existing_colors = list(self.colors_map.values())

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
        self.now = self.inline_colors(self.now)
        self.initial_colors = self.now
    
    # Convert the faces colors into a unique string
    def inline_colors(self, color_dict):
        return "".join(color_dict[self.faces[i]] for i in [4, 1, 0, 2, 3, 5])
    
    # Show the version of the cube we want (initial, target, now)
    def show_cube(self, version):
        print(Cube(self.size, version))

    def rotate_clockwise(self, face):
        pass

    def rotate_counterclockwise(self, face):
        pass

cube1 = RubiksCube()
cube1.set_colors()
print("\nTarget:")
cube1.show_cube(cube1.inline_colors(cube1.target_colors))
print("Initial state of the cube:")
cube1.show_cube(cube1.initial_colors)
cube1.rotate_clockwise("front")
cube1.rotate_counterclockwise("upper")
print("Current state:")
cube1.show_cube(cube1.now)