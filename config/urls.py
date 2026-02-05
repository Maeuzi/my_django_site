from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def home(request):
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <link href="https://fonts.googleapis.com/css?family=Press+Start+2P" rel="stylesheet">
        <style>
            body { background-color: #ff9ff3; font-family: 'Press Start 2P', cursive; text-align: center; padding-top: 20px; }
            .container {
                background:white; border:4px solid black; display:inline-block; 
                padding:20px; box-shadow:8px 8px 0px #000;
            }
            .grid { display: grid; grid-template-columns: repeat(4, 75px); gap: 10px; justify-content: center; margin-top: 20px; }
            
            /* The Card Style */
            .card { 
                width: 75px; height: 75px; border: 3px solid black; 
                background: #ef5777; /* Solid Dark Pink Back */
                cursor: pointer; display: flex; align-items: center; justify-content: center; 
                font-size: 30px; position: relative;
            }
            
            /* Hide the emoji text completely by default */
            .card span { visibility: hidden; }
            
            /* When Revealed: Turn background white and show emoji */
            .card.revealed { background: white !important; }
            .card.revealed span { visibility: visible !important; }
            
            /* When Matched: Hide the whole card */
            .card.matched { visibility: hidden; }
        </style>
    </head>
    <body>
        <div class="container">
            <p style="font-size:10px;">RABBIT & TOMATO PUZZLE</p>
            <div class="grid" id="gameGrid"></div>
            <p id="msg" style="font-size:8px; margin-top:20px;">Find the matches! 頑張れ!</p>
        </div>

        <script>
            const icons = ['🐰', '🐰', '🧺', '🧺', '🍅', '🍅', '🏴‍☠️', '🏴‍☠️', '🎀', '🎀', '⚓', '⚓', '🍎', '🍎', '⭐', '⭐'];
            let flipped = [];
            let matches = 0;
            
            icons.sort(() => Math.random() - 0.5);

            const grid = document.getElementById('gameGrid');
            
            for (let i = 0; i < icons.length; i++) {
                const card = document.createElement('div');
                card.className = 'card';
                card.innerHTML = "<span>" + icons[i] + "</span>";
                
                card.onclick = function() {
                    // Only allow flipping if less than 2 cards are flipped and card isn't already revealed
                    if (flipped.length < 2 && !card.classList.contains('revealed')) {
                        card.classList.add('revealed');
                        flipped.push(card);

                        if (flipped.length === 2) {
                            // Check for match using the icon text
                            if (flipped[0].innerText === flipped[1].innerText) {
                                setTimeout(() => {
                                    flipped[0].classList.add('matched');
                                    flipped[1].classList.add('matched');
                                    flipped = [];
                                    matches++;
                                    if(matches === 8) document.getElementById('msg').innerText = "MISSION COMPLETE! 👑";
                                }, 400);
                            } else {
                                setTimeout(() => {
                                    flipped[0].classList.remove('revealed');
                                    flipped[1].classList.remove('revealed');
                                    flipped = [];
                                }, 700);
                            }
                        }
                    }
                };
                grid.appendChild(card);
            }
        </script>
    </body>
    </html>
    """
    return HttpResponse(html)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
]