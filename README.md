# Fake WebScraper API

Base URL:

```text
https://testapi.kernelvm.xyz
```

## Routes

```text
GET /leads/v1/currentweek
```

Returns current XML leads.

Header:

```text
X-API-KEY: any-value
```

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
```
