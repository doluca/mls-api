from app.models import Listings, listing_pydantic, listing_pydantic_no_ids


async def listing_get_all():
    return await listing_pydantic.from_queryset(Listings.all())


async def listing_create(listing: listing_pydantic_no_ids):
    return await Listings.create(**listing.dict())


async def listing_get(id: int):
    return await Listings.get(listing_id=id)


async def listing_update(id: int, listing: listing_pydantic_no_ids):
    return await Listings.filter(listing_id=id).update(**listing.dict())


async def listing_delete(id: int):
    return await Listings.filter(listing_id=id).delete()
