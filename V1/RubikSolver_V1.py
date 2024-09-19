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
        "b": "blue",
        "r": "red",
        "o": "orange",
        "g": "green",
        "w": "white",
        "y": "yellow"
    }
    
    faces = ["front", "right", "left", "back", "upper", "down"]
    existing_colors = list(colors_map.values())
    
    def __init__(self) -> None:
        pass

    # Ask the user to enter the colors on each face
    def set_colors(self):
        self.face_colors = {}
        print("White face should be on top, and blue face towards the user")
        print("Colors should be entered from top-left to bottom-right")
        print("With blue face towards you, flip the cube up and down to read upper and down faces")
        for i in range(len(self.faces)):
            while True:
                user_input = input(f"Enter face color when {self.existing_colors[i]} facet is in center: ").lower()
                # Check if the number of inputs is correct, and if characters are in the list
                if len(user_input) == self.face_facets and all(char in self.colors_map.keys() for char in user_input):
                    self.face_colors[self.faces[i]] = user_input
                    break
                else:
                    print(f"Only use characters from {self.colors_map.keys()} on {self.face_facets} characters")
    
    # Show
    def show_cube(self):
        cube_colors = "".join(self.face_colors[self.faces[i]] for i in [4, 1, 0, 2, 3, 5])
        print(Cube(self.size, cube_colors.upper()))

cube1 = RubiksCube()
cube1.set_colors()
cube1.show_cube()