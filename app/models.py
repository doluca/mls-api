import json

from tortoise.models import Model
from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator
from pydantic import BaseModel

class Listings(Model):
    listing_id = fields.IntField(pk=True) 
    listing_address = fields.CharField(max_length=250)
    listing_price = fields.IntField()
    def __str__(self):
        return json.dumps(list(self))

listing_pydantic = pydantic_model_creator(Listings, name='Listing')
listing_pydantic_no_ids = pydantic_model_creator(Listings, name='ListingExceptId', exclude=('listing_id',))

class Status(BaseModel):
    message: str