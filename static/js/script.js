function processHtmlCode() {
  var htmlCode = document.getElementById("htmlCode").value;
  fetch("/process", {
    method: "POST",
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
    },
    body: "html_code=" + encodeURIComponent(htmlCode),
  })
    .then((response) => response.text())
    .then((result) => {
      var modifiedCodeTextarea = document.getElementById("modifiedCode");
      var modifiedCodeInput = document.getElementById("modifiedCodeInput");

      if (modifiedCodeTextarea && modifiedCodeInput) {
        modifiedCodeTextarea.value = result;
        modifiedCodeInput.value = result;
      } else {
        console.error(
          "Element with ID 'modifiedCode' or 'modifiedCodeInput' not found"
        );
      }
    });
}

function uploadFile() {
  var fileInput = document.querySelector('input[type="file"]');
  var file = fileInput.files[0];
  var formData = new FormData();
  formData.append("file", file);
  fetch("/upload", {
    method: "POST",
    body: formData,
  })
    .then((response) => response.text())
    .then((result) => {
      var modifiedCodeTextarea = document.getElementById("modifiedCode");
      var modifiedCodeInput = document.getElementById("modifiedCodeInput");

      if (modifiedCodeTextarea && modifiedCodeInput) {
        modifiedCodeTextarea.value = result;
        modifiedCodeInput.value = result;
      } else {
        console.error(
          "Element with ID 'modifiedCode' or 'modifiedCodeInput' not found"
        );
      }
    });
}

function copyToClipboard() {
  var copyText = document.getElementById("modifiedCode");
  copyText.select();
  copyText.setSelectionRange(0, 99999); /* For mobile devices */
  document.execCommand("copy");
  alert("Code copied to clipboard!");
}

var canvas = document.getElementById("bgCanvas");
var ctx = canvas.getContext("2d");

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

var particles = [];
var particleCount = 50;

function createParticles() {
  for (let i = 0; i < particleCount; i++) {
    particles.push({
      x: Math.random() * canvas.width,
      y: Math.random() * canvas.height,
      size: Math.random() * 5 + 1,
      speedX: Math.random() * 3 - 1.5,
      speedY: Math.random() * 3 - 1.5,
    });
  }
}

function drawParticles() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  ctx.fillStyle = "rgba(255, 255, 255, 0.7)";
  ctx.beginPath();

  for (let i = 0; i < particleCount; i++) {
    let particle = particles[i];
    ctx.moveTo(particle.x, particle.y);
    ctx.arc(particle.x, particle.y, particle.size, 0, Math.PI * 2, true);
  }

  ctx.fill();
  moveParticles();
}

function moveParticles() {
  for (let i = 0; i < particleCount; i++) {
    let particle = particles[i];

    if (
      particle.x + particle.size + particle.speedX > canvas.width ||
      particle.x - particle.size + particle.speedX < 0
    ) {
      particle.speedX = -particle.speedX;
    }

    if (
      particle.y + particle.size + particle.speedY > canvas.height ||
      particle.y - particle.size + particle.speedY < 0
    ) {
      particle.speedY = -particle.speedY;
    }

    particle.x += particle.speedX;
    particle.y += particle.speedY;
  }
}

function updateCanvasSize() {
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;
}

createParticles();
setInterval(drawParticles, 30);
window.addEventListener("resize", updateCanvasSize);

// GitHub Link Image
var githubLink = document.getElementById("githubLink");
var githubImage = document.createElement("img");
githubImage.src = "https://image-url/github-icon.png";
githubLink.prepend(githubImage);