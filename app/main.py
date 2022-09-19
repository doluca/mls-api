from typing import List
from fastapi import FastAPI, status, HTTPException
from .config import settings
from app.models import Listings, Status, listing_pydantic, listing_pydantic_no_ids
from tortoise.contrib.fastapi import HTTPNotFoundError, register_tortoise
from app.operations import listing_get_all, listing_get, listing_create, listing_update, listing_delete


app = FastAPI(title="MLS API")


@app.get("/")
async def read_root():
    return await listing_get_all()


@app.post("/listing", status_code=status.HTTP_201_CREATED)
async def create_listing(listing: listing_pydantic_no_ids):
    listing = await listing_create(listing)
    return await listing_pydantic.from_tortoise_orm(listing)


@app.get("/listing/{id}", response_model=listing_pydantic, responses={404: {"model": HTTPNotFoundError}})
async def get_listing(id: int):
    listing = await listing_get(id)
    if not listing:
        raise HTTPException(
            status_code=404, detail=f"Listing '{id}' was not found.")
    return await listing_pydantic.from_queryset_single(Listings.get(listing_id=id))


@app.put("/listing/{id}", response_model=listing_pydantic, responses={404: {"model": HTTPNotFoundError}})
async def update_listing(id: int, listing: listing_pydantic_no_ids):
    listing = await listing_update(id, listing)
    if not listing:
        raise HTTPException(
            status_code=404, detail=f"Listing '{id}' was not found.")
    return await listing_pydantic.from_queryset_single(Listings.get(listing_id=id))


@app.delete("/listing/{id}", response_model=Status, responses={404: {"model": HTTPNotFoundError}})
async def delete_listing(id: int):
    deleted_listing = await listing_delete(id)
    if not deleted_listing:
        raise HTTPException(
            status_code=404, detail=f"Listing '{id}' was not found.")
    return Status(message=f"Listing '{id}' was deleted.")

register_tortoise(
    app,
    db_url=settings.db_url,
    modules={"models": ["app.models"]},
    add_exception_handlers=True,
)
