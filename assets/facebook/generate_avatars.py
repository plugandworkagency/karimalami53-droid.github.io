import subprocess

BASE_DIR = "/Users/mc/.gemini/antigravity/scratch/plug-and-work-redesign/assets/facebook"

HTML_AVATAR_OR = """<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
* { margin:0; padding:0; box-sizing:border-box; }
body {
    width: 1080px;
    height: 1080px;
    background: #05070B;
    display: flex;
    align-items: center;
    justify-content: center;
    position: relative;
    overflow: hidden;
}
.aura {
    position: absolute;
    width: 800px;
    height: 800px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(212, 175, 55, 0.22) 0%, rgba(212, 175, 55, 0.05) 50%, rgba(5,7,11,0) 75%);
}
.frame {
    position: absolute;
    inset: 40px;
    border-radius: 50%;
    border: 2px solid rgba(212, 175, 55, 0.35);
}
.emblem {
    width: 680px;
    height: 780px;
    position: relative;
    z-index: 10;
    filter: drop-shadow(0 0 45px rgba(212, 175, 55, 0.4));
}
</style>
</head>
<body>
    <div class="aura"></div>
    <div class="frame"></div>
    <div class="emblem">
        <svg viewBox="0 0 280 340" width="100%" height="100%">
            <defs>
                <linearGradient id="goldAvatar" x1="0%" y1="0%" x2="100%" y2="100%">
                    <stop offset="0%" stop-color="#FFFDF2"/>
                    <stop offset="18%" stop-color="#F7E6B5"/>
                    <stop offset="40%" stop-color="#D4AF37"/>
                    <stop offset="65%" stop-color="#B88A28"/>
                    <stop offset="85%" stop-color="#F2DC99"/>
                    <stop offset="100%" stop-color="#D9B44E"/>
                </linearGradient>
            </defs>
            <g transform="translate(140, 170)">
                <polygon points="0,-145 110,-82 110,82 0,145 -110,82 -110,-82" 
                         fill="none" stroke="url(#goldAvatar)" stroke-width="3" stroke-linejoin="round"/>
                <polygon points="0,-131 98,-75 98,75 0,131 -98,75 -98,-75" 
                         fill="none" stroke="url(#goldAvatar)" stroke-width="1.3" stroke-opacity="0.6" stroke-linejoin="round"/>
                
                <line x1="0" y1="-145" x2="0" y2="-131" stroke="url(#goldAvatar)" stroke-width="1.5"/>
                <line x1="110" y1="-82" x2="98" y2="-75" stroke="url(#goldAvatar)" stroke-width="1.5"/>
                <line x1="110" y1="82" x2="98" y2="75" stroke="url(#goldAvatar)" stroke-width="1.5"/>
                <line x1="0" y1="145" x2="0" y2="131" stroke="url(#goldAvatar)" stroke-width="1.5"/>
                <line x1="-110" y1="82" x2="-98" y2="75" stroke="url(#goldAvatar)" stroke-width="1.5"/>
                <line x1="-110" y1="-82" x2="-98" y2="-75" stroke="url(#goldAvatar)" stroke-width="1.5"/>

                <g transform="translate(0, -158)">
                    <path d="M 0,-10 L 2.5,-2.5 L 10,0 L 2.5,2.5 L 0,10 L -2.5,2.5 L -10,0 L -2.5,-2.5 Z" fill="url(#goldAvatar)"/>
                    <circle cx="0" cy="0" r="1.5" fill="#FFFFFF"/>
                </g>

                <rect x="-44" y="-72" width="8.5" height="138" fill="url(#goldAvatar)"/>
                <polygon points="-51,-72 -28,-72 -28,-69 -35,-69 -35,-67 -44,-67 -44,-69 -51,-69" fill="url(#goldAvatar)"/>
                <polygon points="-53,66 -27,66 -27,63 -35,63 -35,61 -44,61 -44,63 -53,63" fill="url(#goldAvatar)"/>
                <path d="M -35,-72 C 2,-72 28,-57 28,-26 C 28,4 2,19 -35,19 L -35,9 C -9,9 16,-4 16,-26 C 16,-49 -9,-62 -35,-62 Z" fill="url(#goldAvatar)"/>

                <polygon points="-75,-22 -61,-22 -25,66 -39,66" fill="url(#goldAvatar)"/>
                <polygon points="-39,66 -27,66 4,-10 -6,-10" fill="url(#goldAvatar)"/>
                <polygon points="-3,-10 7,-10 39,66 27,66" fill="url(#goldAvatar)"/>
                <polygon points="27,66 39,66 70,-22 58,-22" fill="url(#goldAvatar)"/>
                <circle cx="-1" cy="-8" r="2.2" fill="#FFFFFF"/>
            </g>
        </svg>
    </div>
</body>
</html>"""

with open(f"{BASE_DIR}/photo_profil_facebook_embleme_or.html", 'w') as f:
    f.write(HTML_AVATAR_OR)

cmd = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "--headless",
    "--disable-gpu",
    "--window-size=1080,1080",
    f"--screenshot={BASE_DIR}/photo_profil_facebook_embleme_or.png",
    f"{BASE_DIR}/photo_profil_facebook_embleme_or.html"
]
subprocess.run(cmd, check=True)
print("Rendered photo_profil_facebook_embleme_or.png")
