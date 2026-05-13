const canvas = document.getElementById("simulationCanvas");
const ctx = canvas.getContext("2d");

canvas.width = 900;
canvas.height = 600;

const robot = {
  x: 100,
  y: 100,
  radius: 20,
  speed: 2
};

const goal = {
  x: 800,
  y: 500,
  radius: 25
};

const obstacles = [];

for (let i = 0; i < 8; i++) {

  obstacles.push({
    x: Math.random() * 600 + 150,
    y: Math.random() * 400 + 100,
    width: 60,
    height: 60
  });

}

let collisionCount = 0;

function distance(x1, y1, x2, y2) {

  return Math.sqrt(
    (x2 - x1) ** 2 +
    (y2 - y1) ** 2
  );

}

function drawRobot() {

  ctx.beginPath();

  ctx.arc(
    robot.x,
    robot.y,
    robot.radius,
    0,
    Math.PI * 2
  );

  ctx.fillStyle = "dodgerblue";
  ctx.fill();

}

function drawGoal() {

  ctx.beginPath();

  ctx.arc(
    goal.x,
    goal.y,
    goal.radius,
    0,
    Math.PI * 2
  );

  ctx.fillStyle = "limegreen";
  ctx.fill();

}

function drawObstacles() {

  ctx.fillStyle = "red";

  obstacles.forEach(obstacle => {

    ctx.fillRect(
      obstacle.x,
      obstacle.y,
      obstacle.width,
      obstacle.height
    );

  });

}

function checkCollision(nextX, nextY) {

  for (const obstacle of obstacles) {

    if (
      nextX + robot.radius > obstacle.x &&
      nextX - robot.radius < obstacle.x + obstacle.width &&
      nextY + robot.radius > obstacle.y &&
      nextY - robot.radius < obstacle.y + obstacle.height
    ) {

      return true;

    }

  }

  return false;

}

function updateRobot() {

  let dx = goal.x - robot.x;
  let dy = goal.y - robot.y;

  let dist = distance(
    robot.x,
    robot.y,
    goal.x,
    goal.y
  );

  dx /= dist;
  dy /= dist;

  const nextX = robot.x + dx * robot.speed;
  const nextY = robot.y + dy * robot.speed;

  if (checkCollision(nextX, nextY)) {

    collisionCount++;

    robot.x += (Math.random() - 0.5) * 10;
    robot.y += (Math.random() - 0.5) * 10;

  } else {

    robot.x = nextX;
    robot.y = nextY;

  }

  document.getElementById("distance").innerText =
    `Distance to Goal: ${Math.floor(dist)}`;

  document.getElementById("collisions").innerText =
    `Collisions Avoided: ${collisionCount}`;

}

function animate() {

  ctx.clearRect(0, 0, canvas.width, canvas.height);

  drawGoal();
  drawObstacles();

  updateRobot();

  drawRobot();

  requestAnimationFrame(animate);

}

animate();