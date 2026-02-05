from django.templatetags.static import static

def home(request):
    # These variables get the correct URL for your local images
    luffy_url = static('luffy.png')
    kitty_url = static('kitty.png')
    tomato_url = static('tomato.png')

    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <link href="https://fonts.googleapis.com/css?family=Press+Start+2P" rel="stylesheet">
        <style>
            body {{ background-color: #ff9ff3; font-family: 'Press Start 2P', cursive; text-align: center; }}
            .choice-container {{ margin-top: 50px; display: flex; justify-content: center; gap: 20px; }}
            .icon-box {{ cursor: pointer; border: 4px solid black; background: white; padding: 10px; }}
            .icon-box img {{ width: 80px; height: 80px; image-rendering: pixelated; }}
            canvas {{ background: white; border: 4px solid black; display: none; margin: 20px auto; }}
        </style>
    </head>
    <body>
        <h1>CHOOSE YOUR PLAYER</h1>
        
        <div id="selection" class="choice-container">
            <div class="icon-box" onclick="startGame('{luffy_url}')">
                <img src="{luffy_url}" alt="Luffy">
                <p style="font-size:10px">LUFFY</p>
            </div>
            <div class="icon-box" onclick="startGame('{kitty_url}')">
                <img src="{kitty_url}" alt="Kitty">
                <p style="font-size:10px">KITTY</p>
            </div>
        </div>

        <canvas id="gameCanvas" width="400" height="400"></canvas>

        <script>
            let playerImg = new Image();
            let tomatoImg = new Image();
            tomatoImg.src = '{tomato_url}';

            function startGame(imgSrc) {{
                playerImg.src = imgSrc;
                document.getElementById('selection').style.display = 'none';
                document.getElementById('gameCanvas').style.display = 'block';
                // ... (rest of your game logic here)
            }}
        </script>
    </body>
    </html>
    """
    return HttpResponse(html_content)