"""Draws docs/media/app-how-it-works.svg: the four things you do in the app, as one infographic.
Run:  python3 docs/media/app_how_it_works.py   (helpers in infokit.py)."""
from infokit import out, COLORS, t, pill, card, icon, chip, arrow, diamond, node, save

W, H = 1440, 1260
BR, GR, PK, BL, GY, TL = "#b45309", "#15803d", "#be185d", "#1d4ed8", "#64748b", "#0e7490"

out.append(f'<rect width="{W}" height="{H}" fill="#ffffff"/>')
t(60, 78, "AI Career Tracker", 46, 900, "#b91c1c", "start")
t(60, 128, "Mobile App · How It Works", 46, 900, "#1d4ed8", "start")
t(62, 158, "① sign in once and stay signed in  ·  ② find and save a job  ·  ③ tailor your CV  ·  ④ let your inbox move the pipeline", 15, 600, "#475569", "start")

# ------------------------------------------------------------------ ① sessions
card(60, 220, 640, 470, TL, "#ecfeff", "①  Sign in once, stay signed in", TL)
y = 320
node(160, y, "👤", "Sign in", BL, ("e-mail · Google", "forgot password · verify"))
node(380, y, "🔥", "Firebase", "#f59e0b", ("checks the account",))
node(600, y, "🎟️", "Session", GR, ("access + refresh token",))
node(600, 520, "🔐", "Keychain", PK, ("iOS Keychain ·", "Android Keystore"), ring=PK)
diamond(380, 508, ["token", "expired?"], "#ca8a04")
node(160, 520, "🔄", "Rotate", TL, ("new refresh token,", "request retried"))
arrow([(196, y - 12), (344, y - 12)], "blue", dash=False)
arrow([(416, y - 12), (564, y - 12)], "orange", dash=False)
arrow([(600, 412), (600, 466)], "green", "store", dash=False, lx=28)
arrow([(564, 496), (448, 496)], "pink", "read", dash=False, ly=-16)
arrow([(324, 508), (200, 508)], "teal", "yes", dash=False, ly=-16)
chip(380, 640, "all of it inside the Dio interceptor, no screen code", "#cffafe", size=12)

# ------------------------------------------------------------------ ② find a job
card(740, 220, 640, 470, BR, "#fffbeb", "②  Find a job and save it", BR)
y = 320
node(840, y, "🔎", "Search", BR, ("keyword · meaning", "or both together"))
node(1060, y, "🎛️", "Filters", BR, ("sort · posted date", "remote · NL IND sponsor"))
node(1280, y, "📋", "Results", BR, ("paged list, Jobs or", "Internships switch"))
node(1280, 520, "📄", "Job detail", GR, ("sponsor + salary badges", "English ok / Dutch required"))
node(1060, 520, "🗂️", "Pipeline", BL, ("saved → applied →", "interview → offer"))
node(840, 520, "🔔", "Alert", "#f59e0b", ("save the search,", "get told about new jobs"), ring="#f59e0b")
arrow([(876, y - 12), (1024, y - 12)], "brown", dash=False)
arrow([(1096, y - 12), (1244, y - 12)], "brown", dash=False)
arrow([(1280, 412), (1280, 466)], "green", dash=False)
arrow([(1244, 508), (1096, 508)], "blue", "save", dash=False, ly=-16)
arrow([(1024, 508), (876, 508)], "orange", dash=False)
chip(1060, 640, "same search engine as the web app", "#fef3c7", size=12)

# ------------------------------------------------------------------ ③ CV tools
card(60, 750, 640, 470, PK, "#fdf2f8", "③  CV tools", PK)
y = 850
node(160, y, "📂", "Import CV", PK, ("pick a PDF or Word", "file from the phone"))
node(380, y, "🤖", "Tailor to a job", PK, ("summary · bullets", "your AI model"))
node(600, y, "🛡️", "Fact guard", "#b91c1c", ("no new numbers,", "employers or skills"))
node(600, 1050, "📤", "Export", GR, ("LaTeX or PDF", "share sheet"))
node(380, 1050, "✉️", "Cover letter", PK, ("drafted for the", "same posting"))
node(160, 1050, "👁️", "Review", "#ca8a04", ("read it before", "you send it"), ring="#f59e0b")
arrow([(196, y - 12), (344, y - 12)], "pink", dash=False)
arrow([(416, y - 12), (564, y - 12)], "pink", dash=False)
arrow([(600, 940), (600, 996)], "red", dash=False)
arrow([(564, 1038), (416, 1038)], "pink", dash=False)
arrow([(344, 1038), (196, 1038)], "green", dash=False)
chip(380, 1170, "the work runs on the server, the phone stays light", "#fce7f3", size=12)

# ------------------------------------------------------------------ ④ inbox
card(740, 750, 640, 470, BL, "#eff6ff", "④  Inbox moves your pipeline", BL)
y = 850
node(840, y, "✉️", "Gmail", "#dc2626", ("connected once", "on the web"))
node(1060, y, "🔄", "Sync", BL, ("one tap in the Inbox", "tab of My search"))
node(1280, y, "🤖", "Events found", PK, ("invite · test · offer", "rejection · message"))
node(1280, 1050, "🔗", "Linked", GR, ("to the right job", "in your pipeline"))
node(1060, 1050, "👤", "You decide", "#ca8a04", ("accept or dismiss", "each suggestion"), ring="#f59e0b")
node(840, 1050, "🧭", "Stage moves", BL, ("applied → interview →", "offer / rejected"))
arrow([(876, y - 12), (1024, y - 12)], "red", dash=False)
arrow([(1096, y - 12), (1244, y - 12)], "blue", dash=False)
arrow([(1280, 940), (1280, 996)], "green", dash=False)
arrow([(1244, 1038), (1096, 1038)], "green", dash=False)
arrow([(1024, 1038), (876, 1038)], "blue", "accept", dash=False, ly=-16)
chip(1060, 1170, "only extracted facts are stored, never the e-mail text", "#dbeafe", size=12)

save("app-how-it-works.svg", W, H)
