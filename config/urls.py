from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def home(request):
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <link href="https://fonts.googleapis.com/css?family=Press+Start+2P" rel="stylesheet">
        <link href="https://unpkg.com/nes.css/css/nes.min.css" rel="stylesheet">
        <style>
            body { 
                background-color: #fffaf0; 
                color: #444; 
                font-family: 'Press Start 2P', cursive;
                margin: 0;
                overflow: hidden;
                display: flex;
                flex-direction: column;
                align-items: center;
            }
            .header { text-align: center; margin-top: 20px; z-index: 10; }
            
            /* The Floating Background Tomatoes */
            .bg-tomato {
                position: absolute;
                font-size: 2rem;
                opacity: 0.3;
                animation: float 6s infinite ease-in-out;
                z-index: 1;
            }
            @keyframes float {
                0%, 100% { transform: translateY(0) rotate(0deg); }
                50% { transform: translateY(-30px) rotate(20deg); }
            }

            #game-canvas {
                border: 4px solid #000;
                background: white;
                cursor: crosshair;
                margin-top: 10px;
                box-shadow: 10px 10px 0px #ffd1dc;
                z-index: 5;
            }

            .stats { margin-top: 15px; font-size: 0.8rem; color: #d81b60; z-index: 10; }
            
            /* Luffy Pop-up Style */
            #luffy-popup {
                display: none;
                position: fixed;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
                background: white;
                padding: 20px;
                border: 4px solid black;
                text-align: center;
                z-index: 100;
                box-shadow: 15px 15px 0px #ff0000;
            }
        </style>
    </head>
    <body>
        <div class="bg-tomato" style="top:10%; left:10%;">🍅</div>
        <div class="bg-tomato" style="top:20%; right:15%;">🍅</div>
        <div class="bg-tomato" style="bottom:15%; left:20%;">🍅</div>
        <div class="bg-tomato" style="bottom:10%; right:10%;">🍅</div>
        <div class="bg-tomato" style="top:50%; left:5%;">🍅</div>
        <div class="bg-tomato" style="top:40%; right:5%;">🍅</div>

        <div class="header">
            <h1 style="font-size: 0.9rem;">Hello, it's Sweta Nancy!</h1>
            <p style="font-size: 0.6rem;">It's my first Django website.</p>
        </div>

        <canvas id="game-canvas" width="350" height="350"></canvas>
        
        <div class="stats">
            Score: <span id="score">0</span> | 頑張れ！
        </div>

        <div id="luffy-popup" class="nes-container">
            <p style="font-size: 1.5rem;">👒</p>
            <p style="font-size: 0.7rem;">Luffy says:<br>"You found the One Piece of Code!"</p>
            <button class="nes-btn is-error" onclick="closePopup()">GANBARE!</button>
        </div>

        <script>
            const canvas = document.getElementById('game-canvas');
            const ctx = canvas.getContext('2d');
            const scoreElement = document.getElementById('score');
            const popup = document.getElementById('luffy-popup');

            let score = 0;
            let basketX = 145;
            let tomatoes = [];
            let gameActive = true;

            canvas.addEventListener('mousemove', (e) => {
                const rect = canvas.getBoundingClientRect();
                basketX = e.clientX - rect.left - 30;
            });

            // Using Emojis instead of broken links for reliability
            function drawPlayer() {
                ctx.font = "40px Arial";
                ctx.fillText("🎀", basketX, canvas.height - 10); // Hello Kitty ribbon
            }

            function createTomato() {
                tomatoes.push({
                    x: Math.random() * (canvas.width - 30),
                    y: -30,
                    speed: 2 + Math.random() * 2
                });
            }

            function closePopup() {
                popup.style.display = 'none';
                gameActive = true;
                score = 0;
                scoreElement.innerText = score;
                update();
            }

            function update() {
                if (!gameActive) return;

                ctx.clearRect(0, 0, canvas.width, canvas.height);
                drawPlayer();

                for (let i = 0; i < tomatoes.length; i++) {
                    let t = tomatoes[i];
                    t.y += t.speed;
                    ctx.font = "25px Arial";
                    ctx.fillText("🍅", t.x, t.y);

                    if (t.y > canvas.height - 40 && t.x > basketX - 10 && t.x < basketX + 60) {
                        score++;
                        scoreElement.innerText = score;
                        tomatoes.splice(i, 1);
                        i--;

                        if (score === 20) {
                            gameActive = false;
                            popup.style.display = 'block';
                        }
                    } else if (t.y > canvas.height) {
                        tomatoes.splice(i, 1);
                        i--;
                    }
                }

                if (Math.random() < 0.03) createTomato();
                requestAnimationFrame(update);
            }

            update();
        </script>
    </body>
    </html>
    """
    return HttpResponse(html_content)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
]