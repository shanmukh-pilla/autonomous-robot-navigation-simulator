import tkinter as tk
import random
import math

# Window setup
WIDTH = 900
HEIGHT = 600

root = tk.Tk()
root.title("Autonomous Robot Navigation Simulator")

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="#111111")
canvas.pack()

# Robot settings
robot_x = 100
robot_y = 100
robot_radius = 20
robot_speed = 3

# Goal position
goal_x = 800
goal_y = 500

# Obstacles
obstacles = []

for _ in range(8):

    x = random.randint(200, 750)
    y = random.randint(100, 500)

    obstacles.append((x, y, x + 60, y + 60))

# Metrics
collision_count = 0


def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def move_robot():

    global robot_x
    global robot_y
    global collision_count

    canvas.delete("all")

    # Draw goal
    canvas.create_oval(
        goal_x - 25,
        goal_y - 25,
        goal_x + 25,
        goal_y + 25,
        fill="green"
    )

    # Direction vector
    dx = goal_x - robot_x
    dy = goal_y - robot_y

    dist = distance(robot_x, robot_y, goal_x, goal_y)

    if dist != 0:
        dx /= dist
        dy /= dist

    next_x = robot_x + dx * robot_speed
    next_y = robot_y + dy * robot_speed

    collision = False

    # Draw obstacles
    for obstacle in obstacles:

        x1, y1, x2, y2 = obstacle

        canvas.create_rectangle(
            x1,
            y1,
            x2,
            y2,
            fill="red"
        )

        # Collision detection
        if (
            next_x + robot_radius > x1 and
            next_x - robot_radius < x2 and
            next_y + robot_radius > y1 and
            next_y - robot_radius < y2
        ):

            collision = True

    # Obstacle avoidance
    if collision:

        collision_count += 1

        robot_x += random.choice([-1, 1]) * robot_speed
        robot_y += random.choice([-1, 1]) * robot_speed

    else:

        robot_x = next_x
        robot_y = next_y

    # Draw robot
    canvas.create_oval(
        robot_x - robot_radius,
        robot_y - robot_radius,
        robot_x + robot_radius,
        robot_y + robot_radius,
        fill="dodgerblue"
    )

    # Labels
    canvas.create_text(
        180,
        20,
        text="Autonomous Robot Navigation Simulator",
        fill="white",
        font=("Arial", 18, "bold")
    )

    canvas.create_text(
        120,
        50,
        text=f"Distance to Goal: {int(dist)}",
        fill="white",
        font=("Arial", 12)
    )

    canvas.create_text(
        110,
        75,
        text=f"Collisions Avoided: {collision_count}",
        fill="white",
        font=("Arial", 12)
    )

    # Continue simulation
    root.after(30, move_robot)


move_robot()

root.mainloop()