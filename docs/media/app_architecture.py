"""Draws docs/media/app-architecture.svg: how the Flutter app is built and what it talks to.
Run:  python3 docs/media/app_architecture.py   (helpers in infokit.py)."""
from infokit import out, COLORS, t, pill, card, icon, chip, cyl_v, arrow, node, save

W, H = 1440, 900
BR, GR, PK, BL, GY, TL = "#b45309", "#15803d", "#be185d", "#1d4ed8", "#64748b", "#0e7490"

out.append(f'<rect width="{W}" height="{H}" fill="#ffffff"/>')
t(60, 78, "AI Career Tracker", 46, 900, "#b91c1c", "start")
t(60, 128, "Mobile App · System Design", 46, 900, "#1d4ed8", "start")
t(62, 158, "feature-first Cubit architecture  ·  one API shared with the web app  ·  tokens in the system keychain", 15, 600, "#475569", "start")

# ------------------------------------------------------------------ the app
card(60, 220, 660, 620, "#02569B", "#eff6ff", "📱  Flutter app · iOS and Android", "#02569B")
node(160, 320, "👁️", "View", BL, ("screens and widgets", "loading · loaded · failed"))
node(390, 320, "🧠", "Cubit", GR, ("flutter_bloc + equatable", "one FeatureState each"))
node(620, 320, "🗄️", "Repo", BR, ("returns models,", "never touches Dio"))
node(620, 520, "🛡️", "Executer", "#b91c1c", ("maps server errors to", "friendly messages"))
node(390, 520, "🌐", "ApiClient", TL, ("Dio + interceptors", "bearer · refresh · errors"))
node(160, 520, "🔐", "Secure storage", PK, ("Keychain / Keystore", "never plain prefs"), ring=PK)
arrow([(198, 308), (352, 308)], "blue", "events", dash=False, ly=-16)
arrow([(352, 332), (198, 332)], "green", dash=False, ly=22)
arrow([(428, 308), (582, 308)], "green", dash=False)
arrow([(620, 412), (620, 466)], "brown", dash=False)
arrow([(582, 508), (428, 508)], "red", dash=False)
arrow([(354, 508), (198, 508)], "pink", "tokens", dash=False, ly=-16, both=True)
chip(160, 690, "get_it · DI", "#dbeafe"); chip(300, 690, "fl_chart", "#dcfce7"); chip(430, 690, "talker logs", "#fef3c7")
chip(570, 690, "url_launcher", "#fce7f3"); chip(200, 735, "file_picker · share_plus", "#e0f2fe"); chip(420, 735, "google_sign_in", "#ffedd5")
t(390, 790, "views never touch Dio · cubits never build requests · repos return models", 12.5, 600, "#1e3a8a")

# ------------------------------------------------------------------ the backend
card(780, 220, 600, 620, "#16a34a", "#f0fdf4", "☁️  AI Career Tracker API (the web repo)", "#16a34a")
node(930, 320, "⚡", "FastAPI", GR, ("REST · JWT sessions", "same API as the web app"))
cyl_v(1250, 300, 90, 90, "#336791", "PostgreSQL", "pgvector · full-text")
node(930, 520, "🔥", "Firebase Auth", "#f59e0b", ("e-mail · Google sign-in", "sessions for the app"))
node(1250, 520, "🤖", "AI layer", PK, ("fit score · tailoring", "inbox · your own model"))
node(930, 710, "✉️", "Gmail", "#dc2626", ("read-only OAuth", "connected once on the web"))
node(1250, 710, "🕷️", "Crawler + worker", BR, ("11 job systems · boards", "alerts · embeddings"))
arrow([(966, 308), (1190, 308)], "green", dash=False, both=True)
arrow([(930, 428), (930, 466)], "orange", "verifies", dash=False, both=True, lx=36)
arrow([(1000, 698), (1100, 698), (1100, 508), (1210, 508)], "red", "mail facts", at=0.4, lx=-30, ly=-14)
arrow([(1250, 660), (1250, 612)], "brown", dash=False)
arrow([(1322, 698), (1352, 698), (1352, 345), (1300, 345)], "brown", "jobs in", at=0.4, lx=-28)

# ------------------------------------------------------------------ the bridge
arrow([(390, 612), (390, 640), (750, 640), (750, 308), (894, 308)], "teal", "HTTPS · JWT", at=0.5, lx=0, ly=-18)
t(750, 880, "tokens refresh transparently · sign-out revokes the session · the Google button appears only when the server has Google set up", 12.5, 600, "#475569")

save("app-architecture.svg", W, H)
