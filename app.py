#!/usr/bin/env python3
import json
import os
import sqlite3
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import unquote, urlparse

ROOT = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(ROOT, "site_data.db")
PORT = 8000


def connect_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def seed_database():
    conn = connect_db()
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS page_data (
            page TEXT NOT NULL,
            key TEXT NOT NULL,
            payload TEXT NOT NULL,
            PRIMARY KEY (page, key)
        )
        """
    )

    data = {
        "about": {
            "brand": "MICHAEL / .NET",
            "hero": {
                "kicker": "C# • .NET • Blazor • IT Automation",
                "title": "Buduję systemy, które rozwiązują realne problemy biznesowe.",
                "lead": "Ekspert rozwoju i wsparcia aplikacji biznesowych z doświadczeniem w automatyzacji IT, integracjach, systemach enterprise i tworzeniu aplikacji w C#/.NET.",
                "stat_value": "15+",
                "stat_text": "lat doświadczenia w IT — od administracji i automatyzacji po rozwój aplikacji biznesowych.",
                "tags": ["C#", ".NET", "Blazor", "SQL", "PowerShell", "Kafka"]
            },
            "story": [
                "Moje doświadczenie łączy dwa światy: <strong>technologię i biznes</strong>. Z jednej strony lubię projektowanie i pisanie kodu, z drugiej — dobrze czuję się w problemach, w których trzeba zrozumieć proces biznesowy, dane, integracje i ograniczenia istniejącego środowiska.",
                "Przez lata pracowałem z dużymi systemami enterprise, automatyzacją oraz aplikacjami biznesowymi. Obecnie koncentruję się przede wszystkim na <strong>C#, .NET i Blazor</strong>, rozwijając kalkulatory i inne aplikacje wykorzystywane w środowisku ubezpieczeniowym."
            ],
            "strengths": [
                {"title": "Programowanie", "text": "C#, .NET, ASP.NET Core, Blazor WebAssembly, WPF, aplikacje konsolowe i REST API."},
                {"title": "Integracje", "text": "REST, OAuth2, Apigee, Kafka/Avro, WCF, SMTP, RabbitMQ i komunikacja między systemami."},
                {"title": "Automatyzacja", "text": "PowerShell, narzędzia pomocnicze, importy danych, raportowanie i usprawnianie procesów IT."},
                {"title": "Systemy enterprise", "text": "Doświadczenie z dużymi środowiskami, w tym OpenText Captiva i farmą obejmującą dziesiątki serwerów."},
                {"title": "Architektura", "text": "Modular monolith, podejście usługowe, skalowanie API, Load Balancer, SignalR i przetwarzanie asynchroniczne."},
                {"title": "Biznes", "text": "Praca na styku IT, biznesu, sprzedaży i underwriterów oraz przekładanie wymagań na działające rozwiązania."}
            ],
            "experience": [
                {
                    "title": "Ekspert ds. Rozwoju i Wsparcia Aplikacji Biznesowych",
                    "period": "08.2023 — obecnie",
                    "description": "Rozwój aplikacji biznesowych w C#/.NET i Blazor. Kalkulatory składek ubezpieczeniowych, analiza ryzyka, dane, raporty, wsparcie produkcyjne i współpraca z biznesem."
                },
                {
                    "title": "OpenText Captiva / Enterprise IT",
                    "period": "",
                    "description": "Rozwój, administracja i automatyzacja dużych środowisk. Narzędzia PowerShell, SQL, raportowanie oraz obsługa infrastruktury obejmującej około 50 serwerów."
                },
                {
                    "title": "Integracje i aplikacje .NET",
                    "period": "",
                    "description": "Projekty obejmujące REST, WCF, WPF, Apigee, komunikację asynchroniczną oraz własne narzędzia automatyzujące procesy."
                }
            ],
            "direction": {
                "title": "Dokąd zmierzam",
                "body": "Naturalnym kolejnym krokiem jest połączenie doświadczenia technicznego z odpowiedzialnością za ludzi i produkt: <strong>Team Lead, Manager, Product Owner lub rola architektoniczno-liderska</strong>.<br><span class=\"muted\">Lubię rozwiązywać trudne problemy techniczne, ale równie ważne jest dla mnie uporządkowanie sposobu pracy zespołu i doprowadzenie projektu od pomysłu do działającego rozwiązania.</span>"
            }
        },
        "projects": {
            "brand": "MICHAEL / PROJECTS",
            "hero": {
                "kicker": "Portfolio",
                "title": "Projekty, systemy i rozwiązania.",
                "lead": "Zestawienie projektów i obszarów technicznych, które przewijają się przez moje doświadczenie zawodowe.",
                "stat_value": "20+",
                "stat_text": "projektów, systemów, narzędzi i inicjatyw technicznych zidentyfikowanych na podstawie mojego doświadczenia."
            },
            "sections": [
                {
                    "heading": "Aplikacje biznesowe",
                    "layout": "two",
                    "items": [
                        {"title": "Kalkulatory składki ubezpieczeniowej", "description": "Rozwój kalkulatorów w C#/.NET i Blazor WebAssembly. Logika wyliczeń, dane, obsługa scenariuszy biznesowych i współpraca z biznesem.", "tags": ["C#", ".NET", "Blazor WASM"]},
                        {"title": "Kalkulator flotowy", "description": "Aplikacja do obsługi kalkulacji związanych z ubezpieczeniami flotowymi. Jeden z kluczowych przykładów łączenia logiki biznesowej z aplikacją webową.", "tags": ["Blazor", "C#", "Business Logic"]},
                        {"title": "Modułowa obsługa danych DamageId", "description": "Przetwarzanie danych z wielu tabel i prezentowanie ich w kilku/kilkunastu obszarach aplikacji. Wykorzystanie DTO, list, reflection oraz mapowania.", "tags": ["EF Core", "DTO", "Mapperly"]},
                        {"title": "Importy danych z Excela", "description": "Narzędzia do automatyzacji importu danych z wielu plików Excel. Projekt skalowany wraz ze zmianami liczby plików i zmiennych biznesowych.", "tags": ["C#", "Excel", "Automation"]},
                        {"title": "Raportowanie Word / Excel / PDF", "description": "Generowanie raportów na podstawie danych biznesowych i wyników przetwarzania.", "tags": ["C#", "Reporting"]},
                        {"title": "Console Import Tools", "description": "Małe, wyspecjalizowane aplikacje konsolowe automatyzujące import i przetwarzanie danych.", "tags": [".NET", "Console"]}
                    ]
                },
                {
                    "heading": "Integracje i infrastruktura aplikacyjna",
                    "layout": "grid",
                    "items": [
                        {"title": "REST API + OAuth2", "description": "Integracje aplikacji biznesowych poprzez REST i client credentials.", "tags": ["REST", "OAuth2", "ASP.NET Core"]},
                        {"title": "Kafka + Avro", "description": "Integracje oparte o komunikację zdarzeniową i schematy Avro.", "tags": ["Kafka", "Avro"]},
                        {"title": "SignalR — centralne powiadomienia", "description": "Koncepcja zewnętrznego huba SignalR dla alertów administracyjnych w aplikacjach Blazor, z myślą o wielu klientach.", "tags": ["SignalR", "Blazor"]},
                        {"title": "API za Load Balancerem", "description": "Projektowanie rozwiązania z dwiema instancjami API za Load Balancerem i analiza problemów stanu oraz skalowania.", "tags": ["IIS", "Load Balancer"]},
                        {"title": "Email Dispatcher .NET 8", "description": "System pobierający dane z DB, składający wiadomości z szablonów i załączników oraz wysyłający je przez SMTP.", "tags": [".NET 8", "SMTP", "DB"]},
                        {"title": "RabbitMQ + wysyłka maili", "description": "Asynchroniczny wariant architektury dispatchera mailowego z wykorzystaniem kolejki.", "tags": ["RabbitMQ", "Async"]}
                    ]
                },
                {
                    "heading": "Enterprise IT & automatyzacja",
                    "layout": "two",
                    "items": [
                        {"title": "OpenText Captiva", "description": "Wieloletnie doświadczenie w środowisku Captiva — administracja, utrzymanie, automatyzacja i rozwój narzędzi.", "tags": ["Captiva", "Enterprise"]},
                        {"title": "Captiva Farm", "description": "Zarządzanie środowiskiem obejmującym około 50 serwerów, wraz z automatyzacją powtarzalnych operacji.", "tags": ["Infrastructure", "PowerShell"]},
                        {"title": "PowerShell Automation", "description": "Własne skrypty i narzędzia do automatyzacji zadań administracyjnych i operacyjnych.", "tags": ["PowerShell", "Automation"]},
                        {"title": "SQL Reporting", "description": "Ekstrakcja i analiza danych oraz tworzenie raportów wspierających procesy operacyjne i biznesowe.", "tags": ["SQL", "Data"]},
                        {"title": "Apigee Proxies", "description": "Praca przy integracjach API i warstwie proxy w Apigee.", "tags": ["Apigee", "API"]},
                        {"title": "WCF / WPF / aplikacje konsolowe", "description": "Starsze aplikacje i narzędzia biznesowe rozwijane oraz utrzymywane przed przejściem mocniej w stronę web/.NET.", "tags": ["WCF", "WPF", ".NET"]}
                    ]
                },
                {
                    "heading": "Architektura i inicjatywy techniczne",
                    "layout": "grid",
                    "items": [
                        {"title": "Modular Monolith / Microservices", "description": "Analiza kierunku rozwoju aplikacji: modularizacja domen, separacja odpowiedzialności i potencjalne wydzielanie usług.", "tags": []},
                        {"title": "Client / API / Services / Domain", "description": "Porządkowanie warstw aplikacji i odpowiedzialności pomiędzy klientem, API, usługami, shared i domeną.", "tags": []},
                        {"title": "Skalowanie aplikacji Blazor", "description": "Rozważanie architektury dla wielu klientów i wielu instancji backendu, w tym SignalR, stan aplikacji i Load Balancer.", "tags": []}
                    ]
                }
            ]
        }
    }

    for page, payload in data.items():
        conn.execute(
            "INSERT OR REPLACE INTO page_data (page, key, payload) VALUES (?, ?, ?)",
            (page, "content", json.dumps(payload, ensure_ascii=False)),
        )

    conn.commit()
    conn.close()


def load_page_data(page):
    conn = connect_db()
    row = conn.execute(
        "SELECT payload FROM page_data WHERE page = ? AND key = 'content'",
        (page,),
    ).fetchone()
    conn.close()
    if row is None:
        return {}
    return json.loads(row["payload"])


class SiteHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self._handle_request(send_body=True)

    def do_HEAD(self):
        self._handle_request(send_body=False)

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, OPTIONS, HEAD")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def _handle_request(self, send_body):
        path = unquote(urlparse(self.path).path)

        if path in ("/", "/index.html"):
            self.serve_file("index.html", send_body=send_body)
            return

        if path.startswith("/api/"):
            self.serve_api(path, send_body=send_body)
            return

        if path.startswith("/"):
            self.serve_file(path.lstrip("/"), send_body=send_body)
            return

        self.send_error(404, "Not found")

    def serve_api(self, path, send_body=True):
        endpoint = path.replace("/api/", "", 1)
        if endpoint == "about":
            payload = load_page_data("about")
        elif endpoint == "projects":
            payload = load_page_data("projects")
        elif endpoint == "health":
            payload = {"status": "ok"}
        else:
            payload = {"error": "Not found"}
            self.send_response(404)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            if send_body:
                self.wfile.write(json.dumps(payload, ensure_ascii=False).encode("utf-8"))
            return

        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, OPTIONS, HEAD")
        self.end_headers()
        if send_body:
            self.wfile.write(body)

    def serve_file(self, relative_path, send_body=True):
        safe_path = relative_path if relative_path else "index.html"
        target = os.path.normpath(os.path.join(ROOT, safe_path))

        if not target.startswith(ROOT):
            self.send_error(403, "Forbidden")
            return

        if not os.path.exists(target) or not os.path.isfile(target):
            self.send_error(404, "Not found")
            return

        content_type = "text/html; charset=utf-8"
        if target.endswith(".css"):
            content_type = "text/css; charset=utf-8"
        elif target.endswith(".js"):
            content_type = "application/javascript; charset=utf-8"
        elif target.endswith(".json"):
            content_type = "application/json; charset=utf-8"

        try:
            with open(target, "rb") as f:
                data = f.read()
        except OSError:
            self.send_error(500, "Internal Server Error")
            return

        self.send_response(200)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        if send_body:
            self.wfile.write(data)

    def log_message(self, format, *args):
        return


if __name__ == "__main__":
    seed_database()
    server = ThreadingHTTPServer(("0.0.0.0", PORT), SiteHandler)
    print(f"Uruchomiono serwer na http://localhost:{PORT}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
