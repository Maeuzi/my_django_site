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
                background-color: #f8bbd0; 
                color: #212529; 
                font-family: 'Press Start 2P', cursive;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 100vh;
                margin: 0;
                overflow: hidden;
            }
            .container { 
                background: white; 
                padding: 2rem; 
                border: 4px solid #000; 
                text-align: center; 
                z-index: 10;
                box-shadow: 10px 10px 0px #ff80ab;
            }
            .character {
                position: absolute;
                image-rendering: pixelated;
                animation: float 4s infinite ease-in-out;
            }
            @keyframes float {
                0%, 100% { transform: translateY(0px) rotate(0deg); }
                50% { transform: translateY(-20px) rotate(10deg); }
            }
            .tomato { font-size: 3.5rem; position: absolute; animation: float 3s infinite; }
            h1 { font-size: 1.1rem; line-height: 1.6; color: #d81b60; }
        </style>
    </head>
    <body>
        <img src="https://i.pinimg.com/originals/9e/3c/6e/9e3c6e9366e6093d987820a28308466b.png" 
             class="character" style="top: 10%; left: 8%; width: 90px;">
        
        <img src="https://raw.githubusercontent.com/gist/adrianmcli/6027374/raw/3e390637f9ed3c31828f9f65c95790c50d4f1837/hello-kitty.png" 
             class="character" style="bottom: 12%; right: 8%; width: 110px;">

        <div class="tomato" style="top: 15%; right: 15%;">🍅</div>
        <div class="tomato" style="bottom: 15%; left: 15%; animation-delay: 1s;">🍅</div>

        <div class="container">
            <h1>Hello, it's Sweta Nancy!</h1>
            <h1>It's my first Django website.</h1>
            <br>
            <div class="nes-balloon from-left is-primary">
                <p style="color: #212529; font-size: 1.2rem; margin: 0;">頑張れ！</p>
            </div>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html_content)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
]