"""Draws docs/media/app-technical.svg: the technical view (request pipeline, token rotation, error mapping, state machine, API surface).
Run:  python3 docs/media/app_technical.py   (helpers in infokit.py)."""
from xml.sax.saxutils import escape
from infokit import out, COLORS, t, pill, card, chip, arrow, diamond, save

W, H = 1440, 1560
MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"


def mono(x, y, s, size=12.5, fill="#0f172a", anchor="start", weight=600):
    out.append(f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}" font-family="{MONO}">{escape(s)}</text>')


def box(x, y, w, h, color, fill, title, lines=(), mono_lines=True):
    out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{fill}" stroke="{color}" stroke-width="2"/>')
    out.append(f'<rect x="{x}" y="{y}" width="{w}" height="30" rx="12" fill="{color}"/><rect x="{x}" y="{y + 18}" width="{w}" height="12" fill="{color}"/>')
    t(x + w / 2, y + 21, title, 13.5, 800, "#fff")
    for i, s in enumerate(lines):
        (mono if mono_lines else (lambda a, b, c, **k: t(a, b, c, 12, 600, "#334155", "start")))(x + 12, y + 52 + i * 19, s, **({"size": 11.5, "fill": "#334155"} if mono_lines else {}))


out.append(f'<rect width="{W}" height="{H}" fill="#ffffff"/>')
t(60, 78, "AI Career Tracker", 46, 900, "#b91c1c", "start")
t(60, 128, "Mobile App · Under the Hood", 46, 900, "#1d4ed8", "start")
t(62, 158, "Dio interceptor chain  ·  single-flight token rotation  ·  typed error mapping  ·  FeatureState machine  ·  REST surface /api/v1", 15, 600, "#475569", "start")

# ------------------------------------------------------------------ A: the interceptor chain
card(60, 220, 1320, 300, "#0e7490", "#ecfeff", "A · One request through the Dio interceptor chain", "#0e7490")
xs = [84, 344, 604, 864, 1124]
box(xs[0], 270, 220, 150, "#b45309", "#fffbeb", "Repo → ApiClient", ["request(path, method,", "  data, query, withToken)", "extra['token'] = withToken", "BaseUrl  …/api/v1"])
box(xs[1], 270, 220, 150, "#1d4ed8", "#eff6ff", "RequestInterceptor", ["if extra.token != false:", "  Authorization:", "    Bearer <access>", "read from SecureStorage"])
box(xs[2], 270, 220, 150, "#0e7490", "#ecfeff", "HTTPS · JSON", ["connectTimeout  20 s", "receiveTimeout  60 s", "Accept: application/json", "file upload: octet-stream"])
box(xs[3], 270, 220, 150, "#be185d", "#fdf2f8", "RefreshInterceptor", ["onError, status == 401", "skip: /auth/*, retried,", "  token == false", "single-flight refresh"])
box(xs[4], 270, 220, 150, "#b91c1c", "#fef2f2", "ErrorInterceptor", ["DioException →", "  CustomDioException", "    (ErrorType, message)", "cubits see only this"])
for a, b, c in ((0, 1, "blue"), (1, 2, "teal"), (3, 4, "red")):
    arrow([(xs[a] + 224, 345), (xs[b] - 4, 345)], c, dash=False)
arrow([(xs[2] + 224, 345), (xs[3] - 4, 345)], "teal", dash=False)
chip(450, 465, "AppConfig.enableLogging → talker logs every failed call", "#cffafe", size=12)
chip(1000, 465, "Executer maps the result to a Status for the cubit", "#fee2e2", size=12)

# ------------------------------------------------------------------ B: token rotation sequence
card(60, 560, 700, 460, "#be185d", "#fdf2f8", "B · Token rotation, replayed once", "#be185d")
lanes = [(160, "App (Dio)", "#1d4ed8"), (410, "SecureStorage", "#7c3aed"), (660, "API  /api/v1", "#15803d")]
for x, name, c in lanes:
    pill(x, 612, name, c, size=13)
    out.append(f'<line x1="{x}" y1="630" x2="{x}" y2="985" stroke="{c}" stroke-opacity=".45" stroke-width="2" stroke-dasharray="6 6"/>')


def msg(y, x1, x2, s, c, back=False, dash=False):
    col = COLORS[c]
    out.append(f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="{col}" stroke-width="2.4"{" stroke-dasharray=\"7 5\"" if dash else ""} marker-end="url(#m-{c})"/>')
    mono((x1 + x2) / 2, y - 7, s, 11.5, col, "middle", 700)


msg(660, 160, 660, "GET /jobs   Authorization: Bearer <old>", "blue")
msg(694, 660, 160, "401 Unauthorized", "red", dash=True)
msg(736, 160, 410, "read refresh token", "purple" if False else "violet")
msg(768, 160, 660, "POST /auth/refresh {refresh_token}", "pink")
msg(802, 660, 160, "200 {access_token, refresh_token}", "green", dash=True)
msg(838, 160, 410, "saveTokens(access, refresh)", "violet")
msg(880, 160, 660, "replay GET /jobs  (extra.retried = true)", "blue")
msg(914, 660, 160, "200 OK  → handler.resolve", "green", dash=True)
out.append('<rect x="92" y="942" width="600" height="38" rx="9" fill="#fee2e2" stroke="#b91c1c" stroke-width="1.5"/>')
mono(392, 966, "refresh fails → storage.clear() · onSessionExpired() → guest mode", 11.5, "#991b1b", "middle", 700)

# ------------------------------------------------------------------ C: error mapping
card(800, 560, 580, 460, "#b91c1c", "#fef2f2", "C · HTTP status → ErrorType → message", "#b91c1c")
rows = [("400", "badRequest", "Invalid request"), ("401", "unauthorized", "Please sign in again"), ("403", "forbidden", "You do not have access"), ("404", "notFound", "Not found"),
        ("409", "conflict", "Conflict"), ("422", "validation", "Please check the entered data"), ("429", "tooManyRequests", "Too many requests, slow down"), ("5xx", "server", "Server error, try again later"),
        ("timeout", "noInternet", "Cannot reach the server"), ("other", "unknown", "Something went wrong")]
mono(830, 622, "status", 11.5, "#64748b"); mono(920, 622, "ErrorType", 11.5, "#64748b"); mono(1090, 622, "fallback message", 11.5, "#64748b")
for i, (a, b, c) in enumerate(rows):
    y = 640 + i * 34
    out.append(f'<rect x="820" y="{y}" width="540" height="30" rx="7" fill="{"#fff" if i % 2 else "#fee2e2"}" opacity=".9"/>')
    mono(832, y + 20, a, 12.5, "#b91c1c", weight=800); mono(920, y + 20, b, 12.5, "#0f172a"); mono(1090, y + 20, c, 11.5, "#475569")
t(1090, 1000, "the server's  detail  text wins over the fallback", 12, 600, "#991b1b")

# ------------------------------------------------------------------ D: state machine
card(60, 1060, 700, 440, "#15803d", "#f0fdf4", "D · FeatureState machine", "#15803d")
def state(x, y, name, c):
    out.append(f'<rect x="{x - 58}" y="{y - 20}" width="116" height="40" rx="20" fill="#fff" stroke="{c}" stroke-width="2.4"/>'); mono(x, y + 5, name, 13, c, "middle", 800)
state(150, 1160, "initial", "#64748b"); state(330, 1160, "loading", "#1d4ed8"); state(560, 1110, "loaded", "#15803d"); state(560, 1210, "failed", "#b91c1c")
arrow([(210, 1160), (270, 1160)], "gray", dash=False)
arrow([(386, 1146), (500, 1114)], "green", "200", dash=False, ly=-14)
arrow([(386, 1174), (500, 1206)], "red", "error", dash=False, ly=20)
arrow([(560, 1232), (560, 1262), (330, 1262), (330, 1184)], "blue", "retry", at=0.5, ly=-14)
mono(80, 1290, "enum Status { initial, loading, loaded, failed }", 12, "#14532d")
mono(80, 1312, "abstract class FeatureState extends Equatable { status, error }", 12, "#14532d")
mono(80, 1334, "class PaginatedState<T> { items, hasReachedMax, total }", 12, "#14532d")
mono(80, 1368, "views never touch Dio · cubits never build requests · repos return models", 11.5, "#166534")
mono(80, 1392, "every screen renders loading, loaded and failed (Try again)", 11.5, "#166534")
mono(80, 1416, "Equatable props → BlocBuilder rebuilds only on real change", 11.5, "#166534")

# ------------------------------------------------------------------ E: API surface
card(800, 1060, 580, 440, "#1d4ed8", "#eff6ff", "E · REST surface used by the app  (/api/v1)", "#1d4ed8")
groups = [("auth", "#be185d", "register · login · refresh · logout · me · profile · password · google · forgot · reset · verify"),
          ("jobs", "#b45309", "GET /jobs · /jobs/{id} · /jobs/suggest · /companies"),
          ("me", "#15803d", "/me/pipeline · /me/jobs/{id} · /me/searches · /me/notifications"),
          ("market", "#0e7490", "GET /analytics/overview"),
          ("cv", "#7c3aed", "extract · tailor · ai-tailor · cover-letter · latex · pdf · compilers")]
y = 1104
for name, c, desc in groups:
    out.append(f'<rect x="822" y="{y}" width="72" height="26" rx="13" fill="{c}"/>'); mono(858, y + 18, name, 12.5, "#fff", "middle", 800)
    words, line, lines = desc.split(" "), "", []
    for w_ in words:
        if len(line) + len(w_) > 40: lines.append(line); line = ""
        line += w_ + " "
    lines.append(line)
    for i, l_ in enumerate(lines): mono(910, y + 18 + i * 17, l_.strip(), 11.5, "#334155")
    y += 26 + max(1, len(lines)) * 17 + 4
chip(1090, 1478, "JWT bearer · JSON · same API as the web app", "#dbeafe", size=12)

save("app-technical.svg", W, H)
