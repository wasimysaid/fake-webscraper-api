# Fake WebScraper API

Base URL:

```text
https://testapi.kernelvm.xyz
```

API key:

```text
teamjaguar-test-key-2026
```

Header:

```text
X-API-KEY: teamjaguar-test-key-2026
```

## Routes

```text
GET /leads/v1/currentweek
```

Returns current XML leads.

```text
POST /test/leads
```

Replaces the XML returned by `/leads/v1/currentweek`.

Body:

```text
application/xml
```

```text
POST /test/reset
```

Resets back to the default test XML.

## Java config

```properties
webscraperAPIURL=https://testapi.kernelvm.xyz/leads/v1/currentweek
webscraperX-API-KEY=teamjaguar-test-key-2026
```
