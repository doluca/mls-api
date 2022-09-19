# mypy: no-disallow-untyped-decorators
# pylint: disable=E0611,E0401
import asyncio
from typing import Generator

import pytest
from fastapi.testclient import TestClient
from .main import app, delete_listing
from app.models import Listings, listing_pydantic_no_ids
from app.operations import listing_get_all, listing_get, listing_create, listing_update, listing_delete

from tortoise.contrib.test import finalizer, initializer


@pytest.fixture(scope="module")
def client() -> Generator:
    initializer(["app.models"])
    with TestClient(app) as c:
        yield c
    finalizer()


@pytest.fixture(scope="module")
def event_loop(client: TestClient) -> Generator:
    yield client.task.get_loop()


def test_listing(client: TestClient, event_loop: asyncio.AbstractEventLoop):  # nosec
    #create
    response = client.post(
        "/listing", json={"listing_address": "Example Address", "listing_price": 123})
    assert response.status_code == 201, response.text
    data = response.json()

    assert data["listing_address"] == "Example Address"
    assert data["listing_price"] == 123
    assert "listing_id" in data

    id = data["listing_id"]
    
    listing_obj = event_loop.run_until_complete(listing_get(id))
    assert listing_obj.listing_id == id
    
    #get
    response = client.get("/listing/" + str(id))
    assert response.status_code == 200, response.text
    data = response.json()

    assert "listing_id" in data
    assert data["listing_id"] == id
    
    response = client.get("/listing/foo")
    assert response.status_code == 422, response.text
    data = response.json()

    #update
    response = client.put("/listing/" + str(id), json={"listing_address": "Changed Address", "listing_price": 246})
    assert response.status_code == 200, response.text
    data = response.json()

    assert data["listing_address"] == "Changed Address"
    assert data["listing_price"] == 246
    assert "listing_id" in data

    assert data["listing_id"] == id

    #delete
    response = client.delete("/listing/" + str(id))
    assert response.status_code == 200, response.text