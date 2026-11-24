import subprocess
import os

HTML_V1 = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800;900&family=Playfair+Display:ital,wght@0,600;0,700;1,500&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Instrument+Serif:ital@0;1&display=swap" rel="stylesheet">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
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
        }

        /* Luxury Fine Gold Border Certificate Framing */
        .frame-outer {
            position: absolute;
            inset: 22px;
            border: 1px solid rgba(212, 175, 55, 0.28);
            border-radius: 16px;
            pointer-events: none;
        }
        .frame-inner {
            position: absolute;
            inset: 30px;
            border: 0.5px solid rgba(212, 175, 55, 0.14);
            border-radius: 12px;
            pointer-events: none;
        }
        .corner-tick {
            position: absolute;
            width: 24px;
            height: 24px;
            border-color: rgba(212, 175, 55, 0.5);
            border-style: solid;
        }
        .corner-tl { top: 22px; left: 22px; border-width: 2px 0 0 2px; }
        .corner-tr { top: 22px; right: 22px; border-width: 2px 2px 0 0; }
        .corner-bl { bottom: 22px; left: 22px; border-width: 0 0 2px 2px; }
        .corner-br { bottom: 22px; right: 22px; border-width: 0 2px 2px 0; }

        /* Ambient Champagne Glow */
        .glow-aura {
            position: absolute;
            left: 50%;
            top: 50%;
            transform: translate(-50%, -50%);
            width: 900px;
            height: 500px;
            background: radial-gradient(ellipse at center, rgba(212, 175, 55, 0.16) 0%, rgba(212, 175, 55, 0.04) 45%, rgba(5, 7, 11, 0) 75%);
            pointer-events: none;
        }

        /* Subtle Luxury Radial Texture */
        .bg-grid {
            position: absolute;
            inset: 0;
            background-image: radial-gradient(rgba(212, 175, 55, 0.08) 1px, transparent 1px);
            background-size: 28px 28px;
            opacity: 0.7;
            pointer-events: none;
        }

        /* Main Content Container (Centered & Safe Zone optimized) */
        .banner-content {
            position: relative;
            z-index: 10;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 70px;
            max-width: 1400px;
            width: 100%;
            padding: 0 60px;
        }

        /* Left Emblem */
        .emblem-wrapper {
            flex-shrink: 0;
            width: 220px;
            height: 240px;
            display: flex;
            align-items: center;
            justify-content: center;
            filter: drop-shadow(0 0 25px rgba(212, 175, 55, 0.35));
        }

        /* Right Branding Typography */
        .brand-col {
            display: flex;
            flex-direction: column;
            justify-content: center;
            text-align: left;
        }

        .gold-text-gradient {
            background: linear-gradient(135deg, #FFFDF2 0%, #F7E6B5 20%, #D4AF37 50%, #B88A28 80%, #D9B44E 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .main-brand-title {
            font-family: 'Cinzel', 'Playfair Display', Georgia, serif;
            font-size: 58px;
            font-weight: 800;
            letter-spacing: 16px;
            line-height: 1.1;
            margin-bottom: 8px;
            text-shadow: 0 4px 20px rgba(0, 0, 0, 0.8);
        }

        .sub-brand-row {
            display: flex;
            align-items: center;
            gap: 16px;
            font-family: 'Cinzel', serif;
            font-size: 19px;
            font-weight: 600;
            letter-spacing: 12px;
            color: #F7E6B5;
            margin-bottom: 12px;
        }
        .sub-brand-row .sep {
            color: #D4AF37;
            font-weight: 300;
            letter-spacing: 2px;
        }
        .sub-brand-row .domain-tag {
            font-size: 13px;
            letter-spacing: 5px;
            color: #94A3B8;
            font-family: 'Plus Jakarta Sans', sans-serif;
            font-weight: 500;
        }

        /* Divider with Diamond */
        .divider-line {
            display: flex;
            align-items: center;
            gap: 14px;
            margin-bottom: 16px;
            max-width: 650px;
        }
        .divider-line .line {
            height: 1px;
            flex: 1;
            background: linear-gradient(90deg, rgba(212, 175, 55, 0.6), transparent);
        }
        .divider-line .line.left-line {
            background: linear-gradient(90deg, transparent, rgba(212, 175, 55, 0.6));
        }
        .divider-line .diamond {
            width: 7px;
            height: 7px;
            background: #D4AF37;
            transform: rotate(45deg);
            box-shadow: 0 0 10px #D4AF37;
        }

        .slogan-text {
            font-family: 'Playfair Display', 'Instrument Serif', Georgia, serif;
            font-style: italic;
            font-size: 20px;
            letter-spacing: 3px;
            color: #E2E8F0;
            margin-bottom: 22px;
        }
        .slogan-text strong {
            color: #D4AF37;
            font-weight: 600;
            font-style: normal;
        }

        /* Bottom Badges / Contact Info */
        .contact-badges {
            display: flex;
            align-items: center;
            flex-wrap: wrap;
            gap: 12px;
        }
        .badge-pill {
            display: inline-flex;
            align-items: center;
            gap: 7px;
            background: rgba(255, 255, 255, 0.04);
            border: 1px solid rgba(212, 175, 55, 0.25);
            padding: 7px 15px;
            border-radius: 9999px;
            font-size: 12.5px;
            font-weight: 600;
            letter-spacing: 0.5px;
            color: #F8FAFC;
            backdrop-filter: blur(8px);
        }
        .badge-pill.highlight-wa {
            background: rgba(16, 185, 129, 0.14);
            border-color: rgba(16, 185, 129, 0.4);
            color: #34D399;
        }
        .badge-pill.highlight-gold {
            background: rgba(212, 175, 55, 0.12);
            border-color: rgba(212, 175, 55, 0.45);
            color: #F7E6B5;
        }
    </style>
</head>
<body>
    <div class="glow-aura"></div>
    <div class="bg-grid"></div>

    <div class="frame-outer"></div>
    <div class="frame-inner"></div>
    <div class="corner-tick corner-tl"></div>
    <div class="corner-tick corner-tr"></div>
    <div class="corner-tick corner-bl"></div>
    <div class="corner-tick corner-br"></div>

    <div class="banner-content">
        <!-- SVG Emblem (Didot Masterpiece Monogram P & W) -->
        <div class="emblem-wrapper">
            <svg viewBox="0 0 280 340" width="100%" height="100%">
                <defs>
                    <linearGradient id="goldCrest" x1="0%" y1="0%" x2="100%" y2="100%">
                        <stop offset="0%" stop-color="#FFFDF2"/>
                        <stop offset="18%" stop-color="#F7E6B5"/>
                        <stop offset="40%" stop-color="#D4AF37"/>
                        <stop offset="65%" stop-color="#B88A28"/>
                        <stop offset="85%" stop-color="#F2DC99"/>
                        <stop offset="100%" stop-color="#D9B44E"/>
                    </linearGradient>
                </defs>
                <g transform="translate(140, 170)">
                    <!-- Outer Faceted Diamond -->
                    <polygon points="0,-145 110,-82 110,82 0,145 -110,82 -110,-82" 
                             fill="none" stroke="url(#goldCrest)" stroke-width="3" stroke-linejoin="round"/>
                    <!-- Inner Concentric Facet -->
                    <polygon points="0,-131 98,-75 98,75 0,131 -98,75 -98,-75" 
                             fill="none" stroke="url(#goldCrest)" stroke-width="1.2" stroke-opacity="0.5" stroke-linejoin="round"/>
                    
                    <!-- Corner Connectors -->
                    <line x1="0" y1="-145" x2="0" y2="-131" stroke="url(#goldCrest)" stroke-width="1.5"/>
                    <line x1="110" y1="-82" x2="98" y2="-75" stroke="url(#goldCrest)" stroke-width="1.5"/>
                    <line x1="110" y1="82" x2="98" y2="75" stroke="url(#goldCrest)" stroke-width="1.5"/>
                    <line x1="0" y1="145" x2="0" y2="131" stroke="url(#goldCrest)" stroke-width="1.5"/>
                    <line x1="-110" y1="82" x2="-98" y2="75" stroke="url(#goldCrest)" stroke-width="1.5"/>
                    <line x1="-110" y1="-82" x2="-98" y2="-75" stroke="url(#goldCrest)" stroke-width="1.5"/>

                    <!-- Apex 8-Point North Star -->
                    <g transform="translate(0, -158)">
                        <path d="M 0,-10 L 2.5,-2.5 L 10,0 L 2.5,2.5 L 0,10 L -2.5,2.5 L -10,0 L -2.5,-2.5 Z" fill="url(#goldCrest)"/>
                        <circle cx="0" cy="0" r="1.5" fill="#FFFFFF"/>
                    </g>

                    <!-- P Monogram -->
                    <rect x="-44" y="-72" width="8.5" height="138" fill="url(#goldCrest)"/>
                    <polygon points="-51,-72 -28,-72 -28,-69 -35,-69 -35,-67 -44,-67 -44,-69 -51,-69" fill="url(#goldCrest)"/>
                    <polygon points="-53,66 -27,66 -27,63 -35,63 -35,61 -44,61 -44,63 -53,63" fill="url(#goldCrest)"/>
                    <path d="M -35,-72 C 2,-72 28,-57 28,-26 C 28,4 2,19 -35,19 L -35,9 C -9,9 16,-4 16,-26 C 16,-49 -9,-62 -35,-62 Z" fill="url(#goldCrest)"/>

                    <!-- W Monogram -->
                    <polygon points="-75,-22 -61,-22 -25,66 -39,66" fill="url(#goldCrest)"/>
                    <polygon points="-39,66 -27,66 4,-10 -6,-10" fill="url(#goldCrest)"/>
                    <polygon points="-3,-10 7,-10 39,66 27,66" fill="url(#goldCrest)"/>
                    <polygon points="27,66 39,66 70,-22 58,-22" fill="url(#goldCrest)"/>
                    <circle cx="-1" cy="-8" r="2.2" fill="#FFFFFF"/>
                </g>
            </svg>
        </div>

        <!-- Right Branding -->
        <div class="brand-col">
            <h1 class="main-brand-title gold-text-gradient">PLUG &amp; WORK</h1>
            
            <div class="sub-brand-row">
                <span>A G E N C Y</span>
                <span class="sep">•</span>
                <span class="domain-tag">IMMOBILIER D'EXCEPTION &amp; PROGRAMMES NEUFS</span>
            </div>

            <div class="divider-line">
                <div class="line left-line"></div>
                <div class="diamond"></div>
                <div class="line"></div>
            </div>

            <div class="slogan-text">
                « Here to bring solutions » — <strong>Casablanca &amp; Maroc</strong>
            </div>

            <div class="contact-badges">
                <div class="badge-pill highlight-gold">
                    <span>🏢</span> Programmes Neufs &amp; Aide État
                </div>
                <div class="badge-pill">
                    <span>📍</span> 17 Place Charles Nicole, Casablanca
                </div>
                <div class="badge-pill highlight-wa">
                    <span>💬</span> WhatsApp Direct : 06 61 06 07 96
                </div>
                <div class="badge-pill">
                    <span>🌐</span> plugandworkagency.github.io
                </div>
            </div>
        </div>
    </div>
</body>
</html>"""

with open('/Users/mc/.gemini/antigravity/scratch/plug-and-work-redesign/assets/facebook/couverture_facebook_edition_or.html', 'w') as f:
    f.write(HTML_V1)

print('Written V1 HTML.')

# Render using headless Chrome
cmd = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "--headless",
    "--disable-gpu",
    "--window-size=1640,624",
    "--screenshot=/Users/mc/.gemini/antigravity/scratch/plug-and-work-redesign/assets/facebook/couverture_facebook_edition_or.png",
    "/Users/mc/.gemini/antigravity/scratch/plug-and-work-redesign/assets/facebook/couverture_facebook_edition_or.html"
]
subprocess.run(cmd, check=True)
print('Generated V1 PNG.')
