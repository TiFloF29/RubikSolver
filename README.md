# Rubik's Cube Solver

## Why this project ?

I am pretty sure there are quite a lot of Rubik's Cube solver. My goal is not to bring a revolutionary new tool, but to learn Python doing it without using existing Python cube solvers like [RubikOptimal](https://pypi.org/project/RubikOptimal/) or [rubik-solver](https://pypi.org/project/rubik-solver/).

I hope this project will evolve towards a camera-based solution to avoid entering manually all the colors.

## Install requirements

```bash
python -m pip install -r requirements.txt
```

## Version 1

This first version is 100% command lines. You need to enter all the colors of your cube in the right order, after placing the cube with **blue face towards you, and white face on top**.

>[!NOTE]
>
>Here is the order you will be asked to follow :
>
>1. Blue / Front
>2. Red / Right
>3. Orange / Left
>4. Green / Back
>5. White / Upper
>6. Yellow / Down

>[!IMPORTANT]
>
>Looking at the cube, colors should be given from top-left to bottom-right:
>
>```txt
>    1   2   3
>    4   5   6
>    7   8   9
>```
