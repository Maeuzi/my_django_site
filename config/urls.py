from django.templatetags.static import static
from django.http import HttpResponse

def home(request):
    # Get image URLs safely
    luffy = static('luffy.png')
    kitty = static('kitty.png')
    tomato = static('tomato.png')

    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <link href="https://fonts.googleapis.com/css?family=Press+Start+2P" rel="stylesheet">
        <style>
            body { background-color: #f0f2f5; font-family: 'Press Start 2P', cursive; text-align: center; }
            .grid { display: grid; grid-template-columns: repeat(2, 100px); gap: 10px; justify-content: center; }
            .card { width: 100px; height: 100px; border: 3px solid black; background: white; }
            img { width: 80px; display: block; margin: auto; }
        </style>
    </head>
    <body>
        <h1>SWETA'S PUZZLE</h1>
        <div class="grid">
            <div class="card"><img src='""" + luffy + """'></div>
            <div class="card"><img src='""" + kitty + """'></div>
            <div class="card"><img src='""" + tomato + """'></div>
            <div class="card"><img src='""" + luffy + """'></div>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html_content)