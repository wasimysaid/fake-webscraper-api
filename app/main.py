from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse, Response

app = FastAPI(title="Fake WebScraper API")

API_KEY = "teamjaguar-test-key-2026"
DATA_FILE = Path("test-data/currentweek.xml")
DEFAULT_XML = """<m:leads xmlns:m=\"http://webscraper.se.leads-format.1.0\">
    <lead xmlns=\"http://ws.webscraper.test.se/ns/lead\" id=\"test-001\">
        <name>Testbolaget AB</name>
        <address>Testgatan 1</address>
        <zip>12345</zip>
        <city>Karlstad</city>
        <contact>Test Person</contact>
        <tele>010-123456</tele>
        <size>10</size>
        <current_provider>Google</current_provider>
        <email>test@example.com</email>
    </lead>
</m:leads>
"""


def check_key(request: Request):
    api_key = request.headers.get("X-API-KEY")

    if api_key is None or api_key.strip() == "":
        return PlainTextResponse("Missing X-API-KEY", status_code=401)

    if api_key != API_KEY:
        return PlainTextResponse("Wrong X-API-KEY", status_code=403)

    return None


def get_xml():
    if DATA_FILE.exists():
        return DATA_FILE.read_text(encoding="utf-8")
    return DEFAULT_XML


@app.get("/leads/v1/currentweek")
def current_week(request: Request):
    auth_error = check_key(request)

    if auth_error is not None:
        return auth_error

    return Response(content=get_xml(), media_type="application/xml")


@app.post("/test/leads")
async def set_test_leads(request: Request):
    auth_error = check_key(request)

    if auth_error is not None:
        return auth_error

    xml = (await request.body()).decode("utf-8")

    if xml.strip() == "":
        return PlainTextResponse("XML body is empty", status_code=400)

    DATA_FILE.parent.mkdir(exist_ok=True)
    DATA_FILE.write_text(xml, encoding="utf-8")
    return {"message": "test XML saved"}


@app.post("/test/reset")
def reset_test_leads(request: Request):
    auth_error = check_key(request)

    if auth_error is not None:
        return auth_error

    if DATA_FILE.exists():
        DATA_FILE.unlink()

    return {"message": "test XML reset"}
