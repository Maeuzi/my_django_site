from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def home(request):
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <link href="https://fonts.googleapis.com/css?family=Press+Start+2P" rel="stylesheet">
        <style>
            body { 
                background-color: #ff9ff3; 
                font-family: 'Press Start 2P', cursive; 
                text-align: center; 
                padding: 50px; 
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }
            .box { 
                border: 4px solid black; 
                background: white; 
                padding: 40px; 
                display: inline-block; 
                box-shadow: 10px 10px 0px #000; 
            }
            .icons {
                font-size: 60px;
                margin: 20px 0;
            }
            p { font-size: 12px; line-height: 1.5; }
        </style>
    </head>
    <body>
        <div class="box">
            <p>PUZZLE LOADING...</p>
            <div class="icons">👒 🧺 🍅</div>
            <p>頑張れ！</p>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html_content)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
]