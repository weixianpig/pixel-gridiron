# Pixel Gridiron — Mod Lab

A **small original American football browser game**, with a retro game-portal interface and built-in optional mods. This is **not Retro Bowl** and does not include any New Star Games game code, trademarks as branding, art, or assets.

## Play locally

Open `index.html` in Chrome, Edge, Firefox or Safari. No installation, network or build step required. On some browsers, use `python3 -m http.server 8000` and visit `http://localhost:8000/` if `file://` permissions get in the way.

Controls: arrows / WASD move, J / Enter pass to a receiver, Space dash. There are also on-screen controls and tap-to-move.

In MOD MENU you can enable **infinite coins, turbo speed, ghost mode (no tackles) and unlimited time**. Upgrades use localStorage. There is no account, analytics, ads or server.

## Publish a normal website (recommended)

1. Create a **public** GitHub repository, such as `pixel-gridiron`.
2. Upload `index.html`, `.nojekyll`, and optionally other files from this folder to the repo root.
3. Open **Settings → Pages → Build and deployment → Deploy from a branch → main / (root) → Save**.
4. Visit `https://YOUR-USERNAME.github.io/pixel-gridiron/` once deployed.

## Experimental single SVG version

`game.svg` is a full standalone SVG+`foreignObject`+XHTML+JS document generated using `python3 make_svg.py`. It is designed for **direct document navigation** to the SVG. When an SVG is used as an `<img>` or is embedded through certain browsers/sandbox policies, script execution is disabled. Behavior differs by browser, and CDN security headers/MIME types can prevent this version from working.

An experimental CDN URL after pushing to a public GitHub repository is:

`https://cdn.jsdelivr.net/gh/YOUR-USERNAME/pixel-gridiron@main/game.svg`

This is *not* the recommended primary web deployment: jsDelivr is for asset distribution, has caching, and may not allow browser execution of active SVG content. Its GitHub CDN does not serve HTML files as active HTML. Use GitHub Pages for the normal site. Do not use this method to misrepresent the contents of a link or evade organizational network policies.

## Files

- `index.html`: complete standalone game (HTML/CSS/JS)
- `game.svg`: standalone experimental SVG generated from the same game
- `make_svg.py`: reproduces SVG artifact from the HTML
- `.nojekyll`: tells GitHub Pages to serve files without Jekyll transforms
- `LICENSE`: MIT license for this original demo code

## Notes

The arcade game is intentionally a compact proof of concept: AI is simplified; player football rules are not a full Retro Bowl simulation. No original commercial game assets or code were used.