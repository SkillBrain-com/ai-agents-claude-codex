#!/usr/bin/env python3
"""Fetch current weather for a city using Open-Meteo (no API key required).

Usage:
    python3 get_weather.py "București"
    python3 get_weather.py "Cluj-Napoca"

Output:
    19.4°C în București

Returns "N/A (oraș negăsit: X)" if the city can't be geocoded.
"""
from __future__ import annotations

import json
import sys
import urllib.parse
import urllib.request


def get_weather(city: str) -> str:
    """Return a one-line weather summary for the given city."""
    # 1. Geocode the city name → lat/lon
    geo_url = "https://geocoding-api.open-meteo.com/v1/search?" + urllib.parse.urlencode(
        {"name": city, "count": 1, "language": "ro"}
    )
    try:
        with urllib.request.urlopen(geo_url, timeout=10) as resp:
            geo = json.load(resp)
    except Exception as exc:  # noqa: BLE001
        return f"N/A (eroare geocoding: {exc})"

    results = geo.get("results") or []
    if not results:
        return f"N/A (oraș negăsit: {city})"

    lat = results[0]["latitude"]
    lon = results[0]["longitude"]
    name = results[0].get("name", city)

    # 2. Get current weather
    w_url = "https://api.open-meteo.com/v1/forecast?" + urllib.parse.urlencode(
        {
            "latitude": lat,
            "longitude": lon,
            "current": "temperature_2m,weather_code",
            "timezone": "auto",
        }
    )
    try:
        with urllib.request.urlopen(w_url, timeout=10) as resp:
            weather = json.load(resp)
    except Exception as exc:  # noqa: BLE001
        return f"N/A (eroare API vreme: {exc})"

    temp = weather["current"]["temperature_2m"]
    return f"{temp}°C în {name}"


def main() -> int:
    city = sys.argv[1] if len(sys.argv) > 1 else "București"
    print(get_weather(city))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
