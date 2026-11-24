import subprocess
import os

BASE_DIR = "/Users/mc/.gemini/antigravity/scratch/plug-and-work-redesign/assets/facebook"
os.makedirs(BASE_DIR, exist_ok=True)

# -------------------------------------------------------------
# VERSION 2: DARK GLOW 2.0 (Electric Blue + Cantaloupe Orange)
# -------------------------------------------------------------
HTML_V2 = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Playfair+Display:ital,wght@0,600;0,700;1,500&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Cinzel:wght@700;800&display=swap" rel="stylesheet">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            width: 1640px;
            height: 624px;
            background-color: #05070A;
            color: #FFFFFF;
            overflow: hidden;
            position: relative;
            font-family: 'Plus Jakarta Sans', sans-serif;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        /* Ambient Glows */
        .blue-glow {
            position: absolute;
            right: 15%;
            top: 20%;
            width: 750px;
            height: 500px;
            background: radial-gradient(ellipse at center, rgba(0, 102, 255, 0.28) 0%, rgba(0, 102, 255, 0.08) 50%, rgba(5, 7, 10, 0) 75%);
            filter: blur(40px);
            pointer-events: none;
        }
        .cantaloupe-glow {
            position: absolute;
            left: 20%;
            top: 30%;
            width: 550px;
            height: 450px;
            background: radial-gradient(ellipse at center, rgba(255, 138, 91, 0.20) 0%, rgba(255, 138, 91, 0.05) 50%, rgba(5, 7, 10, 0) 75%);
            filter: blur(35px);
            pointer-events: none;
        }
        .dot-matrix {
            position: absolute;
            inset: 0;
            background-image: radial-gradient(rgba(0, 102, 255, 0.16) 1px, transparent 1px);
            background-size: 24px 24px;
            pointer-events: none;
        }

        /* Glassmorphic border */
        .border-container {
            position: absolute;
            inset: 20px;
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 20px;
            pointer-events: none;
        }

        .content {
            position: relative;
            z-index: 10;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 75px;
            max-width: 1440px;
            width: 100%;
            padding: 0 50px;
        }

        .emblem-wrapper {
            flex-shrink: 0;
            width: 220px;
            height: 250px;
            display: flex;
            align-items: center;
            justify-content: center;
            filter: drop-shadow(0 0 35px rgba(0, 102, 255, 0.45));
        }

        .brand-col {
            display: flex;
            flex-direction: column;
            justify-content: center;
            text-align: left;
        }

        .cantaloupe-badge {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: rgba(255, 138, 91, 0.12);
            border: 1px solid rgba(255, 138, 91, 0.35);
            color: #FF8A5B;
            font-size: 13px;
            font-weight: 700;
            letter-spacing: 2px;
            text-transform: uppercase;
            padding: 6px 16px;
            border-radius: 9999px;
            margin-bottom: 14px;
            box-shadow: 0 0 20px rgba(255, 138, 91, 0.2);
            width: fit-content;
        }

        .main-title {
            font-family: 'Instrument Serif', 'Playfair Display', Georgia, serif;
            font-size: 64px;
            font-weight: 500;
            letter-spacing: 3px;
            line-height: 1.05;
            color: #FFFFFF;
            margin-bottom: 8px;
            text-shadow: 0 4px 30px rgba(0, 0, 0, 0.9);
        }
        .main-title .highlight-blue {
            color: #0066FF;
            text-shadow: 0 0 30px rgba(0, 102, 255, 0.6);
        }

        .slogan-row {
            font-size: 19px;
            color: #94A3B8;
            margin-bottom: 22px;
            font-family: 'Instrument Serif', Georgia, serif;
            font-style: italic;
            letter-spacing: 1.5px;
        }
        .slogan-row strong {
            color: #FF8A5B;
            font-style: normal;
            font-family: 'Plus Jakarta Sans', sans-serif;
            font-size: 16px;
            letter-spacing: 1px;
            margin-left: 8px;
        }

        .services-grid {
            display: flex;
            align-items: center;
            flex-wrap: wrap;
            gap: 10px;
            margin-bottom: 22px;
        }
        .service-pill {
            display: inline-flex;
            align-items: center;
            gap: 7px;
            background: rgba(255, 255, 255, 0.04);
            border: 1px solid rgba(255, 255, 255, 0.12);
            padding: 6px 14px;
            border-radius: 10px;
            font-size: 13px;
            color: #E2E8F0;
            font-weight: 500;
        }

        .footer-contacts {
            display: flex;
            align-items: center;
            gap: 16px;
            flex-wrap: wrap;
        }
        .footer-item {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            font-size: 13.5px;
            font-weight: 600;
            color: #CBD5E1;
        }
        .footer-wa {
            background: #10B981;
            color: #FFFFFF;
            padding: 6px 16px;
            border-radius: 9999px;
            font-weight: 700;
            box-shadow: 0 0 20px rgba(16, 185, 129, 0.4);
        }
        .footer-url {
            color: #0066FF;
            font-weight: 700;
            text-shadow: 0 0 15px rgba(0, 102, 255, 0.5);
        }
    </style>
</head>
<body>
    <div class="blue-glow"></div>
    <div class="cantaloupe-glow"></div>
    <div class="dot-matrix"></div>
    <div class="border-container"></div>

    <div class="content">
        <!-- SVG Emblem in Electric Blue & Polished Gold -->
        <div class="emblem-wrapper">
            <svg viewBox="0 0 280 340" width="100%" height="100%">
                <defs>
                    <linearGradient id="crestGoldV2" x1="0%" y1="0%" x2="100%" y2="100%">
                        <stop offset="0%" stop-color="#FFFDF2"/>
                        <stop offset="25%" stop-color="#FFD494"/>
                        <stop offset="50%" stop-color="#FF8A5B"/>
                        <stop offset="75%" stop-color="#D97706"/>
                        <stop offset="100%" stop-color="#FFA680"/>
                    </linearGradient>
                    <linearGradient id="facetBlue" x1="0%" y1="0%" x2="100%" y2="100%">
                        <stop offset="0%" stop-color="#60A5FA"/>
                        <stop offset="50%" stop-color="#0066FF"/>
                        <stop offset="100%" stop-color="#1D4ED8"/>
                    </linearGradient>
                </defs>
                <g transform="translate(140, 170)">
                    <polygon points="0,-145 110,-82 110,82 0,145 -110,82 -110,-82" 
                             fill="none" stroke="url(#facetBlue)" stroke-width="3" stroke-linejoin="round"/>
                    <polygon points="0,-131 98,-75 98,75 0,131 -98,75 -98,-75" 
                             fill="none" stroke="url(#crestGoldV2)" stroke-width="1.4" stroke-opacity="0.7" stroke-linejoin="round"/>
                    
                    <line x1="0" y1="-145" x2="0" y2="-131" stroke="url(#facetBlue)" stroke-width="1.5"/>
                    <line x1="110" y1="-82" x2="98" y2="-75" stroke="url(#facetBlue)" stroke-width="1.5"/>
                    <line x1="110" y1="82" x2="98" y2="75" stroke="url(#facetBlue)" stroke-width="1.5"/>
                    <line x1="0" y1="145" x2="0" y2="131" stroke="url(#facetBlue)" stroke-width="1.5"/>
                    <line x1="-110" y1="82" x2="-98" y2="75" stroke="url(#facetBlue)" stroke-width="1.5"/>
                    <line x1="-110" y1="-82" x2="-98" y2="-75" stroke="url(#facetBlue)" stroke-width="1.5"/>

                    <g transform="translate(0, -158)">
                        <path d="M 0,-10 L 2.5,-2.5 L 10,0 L 2.5,2.5 L 0,10 L -2.5,2.5 L -10,0 L -2.5,-2.5 Z" fill="#FF8A5B"/>
                        <circle cx="0" cy="0" r="1.5" fill="#FFFFFF"/>
                    </g>

                    <rect x="-44" y="-72" width="8.5" height="138" fill="url(#crestGoldV2)"/>
                    <polygon points="-51,-72 -28,-72 -28,-69 -35,-69 -35,-67 -44,-67 -44,-69 -51,-69" fill="url(#crestGoldV2)"/>
                    <polygon points="-53,66 -27,66 -27,63 -35,63 -35,61 -44,61 -44,63 -53,63" fill="url(#crestGoldV2)"/>
                    <path d="M -35,-72 C 2,-72 28,-57 28,-26 C 28,4 2,19 -35,19 L -35,9 C -9,9 16,-4 16,-26 C 16,-49 -9,-62 -35,-62 Z" fill="url(#crestGoldV2)"/>

                    <polygon points="-75,-22 -61,-22 -25,66 -39,66" fill="url(#crestGoldV2)"/>
                    <polygon points="-39,66 -27,66 4,-10 -6,-10" fill="url(#crestGoldV2)"/>
                    <polygon points="-3,-10 7,-10 39,66 27,66" fill="url(#crestGoldV2)"/>
                    <polygon points="27,66 39,66 70,-22 58,-22" fill="url(#crestGoldV2)"/>
                    <circle cx="-1" cy="-8" r="2.2" fill="#FFFFFF"/>
                </g>
            </svg>
        </div>

        <div class="brand-col">
            <div class="cantaloupe-badge">
                <span>✨</span> Immobilier d'Exception &amp; Programmes Neufs
            </div>

            <h1 class="main-title">
                plugandwork<span class="highlight-blue">agency</span>
            </h1>

            <div class="slogan-row">
                « Here to bring solutions » <strong>Casablanca • Maroc</strong>
            </div>

            <div class="services-grid">
                <div class="service-pill">💎 Villas de Prestige</div>
                <div class="service-pill">🏢 Programmes Neufs (Gloria 2 &amp; Victoria)</div>
                <div class="service-pill">🏛️ Aide Directe de l'État (&lt; 700k DH)</div>
                <div class="service-pill">🤝 Commercialisation Promoteurs</div>
            </div>

            <div class="footer-contacts">
                <div class="footer-item footer-wa">
                    💬 WhatsApp : 06 61 06 07 96
                </div>
                <div class="footer-item">
                    📍 17 Place Charles Nicole
                </div>
                <div class="footer-item footer-url">
                    🌐 plugandworkagency.github.io
                </div>
            </div>
        </div>
    </div>
</body>
</html>"""

with open(f"{BASE_DIR}/couverture_facebook_dark_glow.html", 'w') as f:
    f.write(HTML_V2)

print('Written V2 HTML.')

# -------------------------------------------------------------
# VERSION 3: ARCHITECTURAL PRESTIGE (Villa Background + Gold Crest)
# -------------------------------------------------------------
VILLA_IMG_PATH = "/Users/mc/.gemini/antigravity/scratch/plug-and-work-redesign/assets/properties/dar_bouazza/dar_bouazza_1.jpg"

HTML_V3 = f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800;900&family=Playfair+Display:ital,wght@0,600;0,700;1,500&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Instrument+Serif:ital@0;1&display=swap" rel="stylesheet">
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            width: 1640px;
            height: 624px;
            background-color: #05070B;
            color: #FFFFFF;
            overflow: hidden;
            position: relative;
            font-family: 'Plus Jakarta Sans', sans-serif;
            display: flex;
            align-items: center;
            justify-content: center;
        }}

        /* Villa Real Estate Background with Dark Luxury Vignette */
        .bg-photo {{
            position: absolute;
            inset: 0;
            background-image: url('file://{VILLA_IMG_PATH}');
            background-size: cover;
            background-position: center 40%;
            filter: brightness(0.28) contrast(1.15) saturate(0.85);
            transform: scale(1.04);
        }}
        .bg-overlay {{
            position: absolute;
            inset: 0;
            background: linear-gradient(90deg, rgba(5, 7, 11, 0.96) 0%, rgba(5, 7, 11, 0.88) 45%, rgba(5, 7, 11, 0.70) 100%);
        }}

        .frame-outer {{
            position: absolute;
            inset: 20px;
            border: 1px solid rgba(212, 175, 55, 0.35);
            border-radius: 16px;
            pointer-events: none;
        }}

        .content {{
            position: relative;
            z-index: 10;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 70px;
            max-width: 1440px;
            width: 100%;
            padding: 0 50px;
        }}

        .emblem-wrapper {{
            flex-shrink: 0;
            width: 230px;
            height: 260px;
            display: flex;
            align-items: center;
            justify-content: center;
            filter: drop-shadow(0 0 35px rgba(212, 175, 55, 0.45));
        }}

        .brand-col {{
            display: flex;
            flex-direction: column;
            justify-content: center;
            text-align: left;
        }}

        .gold-gradient-text {{
            background: linear-gradient(135deg, #FFFDF2 0%, #F7E6B5 20%, #D4AF37 50%, #B88A28 80%, #D9B44E 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}

        .main-title {{
            font-family: 'Cinzel', 'Playfair Display', serif;
            font-size: 56px;
            font-weight: 800;
            letter-spacing: 15px;
            line-height: 1.1;
            margin-bottom: 8px;
            text-shadow: 0 4px 20px rgba(0, 0, 0, 0.9);
        }}

        .sub-row {{
            display: flex;
            align-items: center;
            gap: 14px;
            font-family: 'Cinzel', serif;
            font-size: 18px;
            font-weight: 600;
            letter-spacing: 10px;
            color: #F7E6B5;
            margin-bottom: 14px;
        }}
        .sub-row .sep {{ color: #D4AF37; }}
        .sub-row .desc {{
            font-family: 'Plus Jakarta Sans', sans-serif;
            font-size: 13px;
            letter-spacing: 4px;
            color: #CBD5E1;
            font-weight: 600;
        }}

        .slogan {{
            font-family: 'Playfair Display', Georgia, serif;
            font-style: italic;
            font-size: 21px;
            letter-spacing: 2.5px;
            color: #E2E8F0;
            margin-bottom: 22px;
        }}
        .slogan strong {{
            color: #D4AF37;
            font-style: normal;
        }}

        .pills-row {{
            display: flex;
            align-items: center;
            gap: 12px;
            flex-wrap: wrap;
        }}
        .pill {{
            display: inline-flex;
            align-items: center;
            gap: 7px;
            background: rgba(0, 0, 0, 0.55);
            border: 1px solid rgba(212, 175, 55, 0.35);
            backdrop-filter: blur(10px);
            padding: 7px 16px;
            border-radius: 9999px;
            font-size: 13px;
            font-weight: 600;
            color: #F8FAFC;
        }}
        .pill-wa {{
            background: rgba(16, 185, 129, 0.2);
            border-color: rgba(16, 185, 129, 0.5);
            color: #34D399;
        }}
    </style>
</head>
<body>
    <div class="bg-photo"></div>
    <div class="bg-overlay"></div>
    <div class="frame-outer"></div>

    <div class="content">
        <div class="emblem-wrapper">
            <svg viewBox="0 0 280 340" width="100%" height="100%">
                <defs>
                    <linearGradient id="crestGoldV3" x1="0%" y1="0%" x2="100%" y2="100%">
                        <stop offset="0%" stop-color="#FFFDF2"/>
                        <stop offset="20%" stop-color="#F7E6B5"/>
                        <stop offset="45%" stop-color="#D4AF37"/>
                        <stop offset="70%" stop-color="#B88A28"/>
                        <stop offset="100%" stop-color="#D9B44E"/>
                    </linearGradient>
                </defs>
                <g transform="translate(140, 170)">
                    <polygon points="0,-145 110,-82 110,82 0,145 -110,82 -110,-82" 
                             fill="none" stroke="url(#crestGoldV3)" stroke-width="3" stroke-linejoin="round"/>
                    <polygon points="0,-131 98,-75 98,75 0,131 -98,75 -98,-75" 
                             fill="none" stroke="url(#crestGoldV3)" stroke-width="1.3" stroke-opacity="0.6" stroke-linejoin="round"/>
                    
                    <g transform="translate(0, -158)">
                        <path d="M 0,-10 L 2.5,-2.5 L 10,0 L 2.5,2.5 L 0,10 L -2.5,2.5 L -10,0 L -2.5,-2.5 Z" fill="url(#crestGoldV3)"/>
                        <circle cx="0" cy="0" r="1.5" fill="#FFFFFF"/>
                    </g>

                    <rect x="-44" y="-72" width="8.5" height="138" fill="url(#crestGoldV3)"/>
                    <path d="M -35,-72 C 2,-72 28,-57 28,-26 C 28,4 2,19 -35,19 L -35,9 C -9,9 16,-4 16,-26 C 16,-49 -9,-62 -35,-62 Z" fill="url(#crestGoldV3)"/>

                    <polygon points="-75,-22 -61,-22 -25,66 -39,66" fill="url(#crestGoldV3)"/>
                    <polygon points="-39,66 -27,66 4,-10 -6,-10" fill="url(#crestGoldV3)"/>
                    <polygon points="-3,-10 7,-10 39,66 27,66" fill="url(#crestGoldV3)"/>
                    <polygon points="27,66 39,66 70,-22 58,-22" fill="url(#crestGoldV3)"/>
                    <circle cx="-1" cy="-8" r="2.2" fill="#FFFFFF"/>
                </g>
            </svg>
        </div>

        <div class="brand-col">
            <h1 class="main-title gold-gradient-text">PLUG &amp; WORK</h1>
            
            <div class="sub-row">
                <span>A G E N C Y</span>
                <span class="sep">•</span>
                <span class="desc">IMMOBILIER DE PRESTIGE &amp; PROGRAMMES NEUFS</span>
            </div>

            <div class="slogan">
                « Here to bring solutions » — <strong>Casablanca &amp; Maroc</strong>
            </div>

            <div class="pills-row">
                <div class="pill">📍 17 Place Charles Nicole, Casablanca</div>
                <div class="pill pill-wa">💬 WhatsApp : 06 61 06 07 96</div>
                <div class="pill">🌐 plugandworkagency.github.io</div>
            </div>
        </div>
    </div>
</body>
</html>"""

with open(f"{BASE_DIR}/couverture_facebook_architectural.html", 'w') as f:
    f.write(HTML_V3)

print('Written V3 HTML.')

# Render PNGs using Google Chrome
configs = [
    ("couverture_facebook_dark_glow.html", "couverture_facebook_dark_glow.png"),
    ("couverture_facebook_architectural.html", "couverture_facebook_architectural.png"),
]

for src, dst in configs:
    cmd = [
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "--headless",
        "--disable-gpu",
        "--window-size=1640,624",
        f"--screenshot={BASE_DIR}/{dst}",
        f"{BASE_DIR}/{src}"
    ]
    subprocess.run(cmd, check=True)
    print(f"Rendered {dst}")

