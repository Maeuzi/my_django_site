from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def home(request):
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <link href="https://fonts.googleapis.com/css?family=Press+Start+2P" rel="stylesheet">
        <style>
            body { background-color: #ff9ff3; font-family: 'Press Start 2P', cursive; text-align: center; padding-top: 20px; }
            .grid { display: grid; grid-template-columns: repeat(4, 70px); gap: 10px; justify-content: center; margin-top: 20px; }
            .card { 
                width: 70px; height: 70px; border: 3px solid black; background: #fff; 
                cursor: pointer; display: flex; align-items: center; justify-content: center; 
                font-size: 30px; transition: 0.2s;
            }
            .hidden { background: #333; color: #333; }
            .matched { visibility: hidden; }
            .container {
                background:white; border:4px solid black; display:inline-block; 
                padding:20px; box-shadow:8px 8px 0px #000;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <p style="font-size:10px;">RABBIT & TOMATO PUZZLE</p>
            <div class="grid" id="gameGrid"></div>
            <p id="msg" style="font-size:8px; margin-top:20px;">Find the matches! 頑張れ!</p>
        </div>

        <script>
            // Replaced the hat with a rabbit!
            const icons = ['🐰', '🐰', '🧺', '🧺', '🍅', '🍅', '🏴‍☠️', '🏴‍☠️', '🎀', '🎀', '⚓', '⚓', '🍎', '🍎', '⭐', '⭐'];
            let flipped = [];
            let matches = 0;
            
            icons.sort(() => Math.random() - 0.5);

            const grid = document.getElementById('gameGrid');
            icons.forEach((icon, i) => {
                const card = document.createElement('div');
                card.className = 'card hidden';
                card.dataset.icon = icon;
                card.innerHTML = icon;
                card.onclick = () => {
                    if (flipped.length < 2 && card.classList.contains('hidden')) {
                        card.classList.remove('hidden');
                        flipped.push(card);
                        if (flipped.length === 2) {
                            if (flipped[0].dataset.icon === flipped[1].dataset.icon) {
                                setTimeout(() => {
                                    flipped.forEach(c => c.classList.add('matched'));
                                    flipped = [];
                                    matches++;
                                    if(matches === 8) document.getElementById('msg').innerText = "MISSION COMPLETE! 👑";
                                }, 500);
                            } else {
                                setTimeout(() => {
                                    flipped.forEach(c => c.classList.add('hidden'));
                                    flipped = [];
                                }, 700);
                            }
                        }
                    }
                };
                grid.appendChild(card);
            });
        </script>
    </body>
    </html>
    """
    return HttpResponse(html)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
]