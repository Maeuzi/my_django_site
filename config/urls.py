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
            body { 
                background-color: #ff9ff3; /* Your Pink Background */
                /* Subtle twinkling star background overlay */
                background-image: radial-gradient(white, rgba(255,255,255,.3) 1px, transparent 20px);
                background-size: 50px 50px;
                font-family: 'Press Start 2P', cursive; 
                text-align: center; 
                padding-top: 20px; 
                margin: 0;
                overflow: hidden;
            }
            .container {
                background: white; border: 4px solid black; display: inline-block; 
                padding: 20px; box-shadow: 8px 8px 0px #000;
                position: relative; z-index: 10;
            }
            .grid { display: grid; grid-template-columns: repeat(4, 75px); gap: 10px; justify-content: center; margin-top: 20px; }
            .card { 
                width: 75px; height: 75px; border: 3px solid black; 
                background: #ef5777; /* Darker pink for card backs */
                cursor: pointer; display: flex; 
                align-items: center; justify-content: center; 
                font-size: 30px; position: relative;
            }
            .card span { visibility: hidden; }
            .card.revealed { background: white !important; }
            .card.revealed span { visibility: visible !important; }
            .card.matched { visibility: hidden; pointer-events: none; }
            
            .particle {
                position: absolute;
                pointer-events: none;
                font-size: 24px;
                z-index: 100;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <p style="font-size:10px;">SWEET STARS PUZZLE</p>
            <div class="grid" id="gameGrid"></div>
            <p id="msg" style="font-size:8px; margin-top:20px;">Match clover, ice cream & more! ✨</p>
        </div>

        <script>
            // Updated Icons: Clover, Tomato, Rabbit, Ice Cream, Stars, and some extras to fill 16 slots
            const icons = ['🍀', '🍀', '🍅', '🍅', '🐰', '🐰', '🍦', '🍦', '⭐', '⭐', '✨', '✨', '🍭', '🍭', '🌸', '🌸'];
            let flipped = [];
            let matches = 0;
            
            icons.sort(() => Math.random() - 0.5);

            function createExplosion(x, y) {
                for (let i = 0; i < 12; i++) {
                    const p = document.createElement('div');
                    p.className = 'particle';
                    p.innerHTML = '⭐';
                    p.style.left = x + 'px';
                    p.style.top = y + 'px';
                    document.body.appendChild(p);

                    const angle = Math.random() * Math.PI * 2;
                    const velocity = 4 + Math.random() * 6;
                    let posX = x;
                    let posY = y;
                    let opacity = 1;

                    const move = setInterval(() => {
                        posX += Math.cos(angle) * velocity;
                        posY += Math.sin(angle) * velocity;
                        opacity -= 0.03;
                        p.style.left = posX + 'px';
                        p.style.top = posY + 'px';
                        p.style.opacity = opacity;
                        p.style.transform = `rotate(${opacity * 360}deg)`;

                        if (opacity <= 0) {
                            clearInterval(move);
                            p.remove();
                        }
                    }, 16);
                }
            }

            const grid = document.getElementById('gameGrid');
            for (let i = 0; i < icons.length; i++) {
                const card = document.createElement('div');
                card.className = 'card';
                card.innerHTML = "<span>" + icons[i] + "</span>";
                
                card.onclick = function(e) {
                    if (flipped.length < 2 && !card.classList.contains('revealed')) {
                        card.classList.add('revealed');
                        flipped.push(card);

                        if (flipped.length === 2) {
                            if (flipped[0].innerText === flipped[1].innerText) {
                                setTimeout(() => {
                                    const rect = card.getBoundingClientRect();
                                    createExplosion(rect.left + 35, rect.top + 35);
                                    
                                    flipped[0].classList.add('matched');
                                    flipped[1].classList.add('matched');
                                    flipped = [];