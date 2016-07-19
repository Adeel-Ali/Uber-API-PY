# -*- coding: utf-8 -*-

"""
    uberapilib.models.price_estimate_collection
 
    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ) on 07/19/2016
"""

from uberapilib.models.base_model import BaseModel
from uberapilib.models.price_esitmate import PriceEsitmate

class PriceEstimateCollection(BaseModel):

    """Implementation of the 'Price Estimate Collection' model.

    Collection of price estimates

    Attributes:
        prices (list of PriceEsitmate): List of price estimates

    """

    def __init__(self, 
                 prices = None):
        """Constructor for the PriceEstimateCollection class"""
        
        # Initialize members of the class
        self.prices = prices

        # Create a mapping from Model property names to API property names
        self.names = {
            "prices": "prices",
        }

    @classmethod
    def from_dictionary(cls, 
                        dictionary):
        """Creates an instance of this model from a dictionary
       
        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.
            
        Returns:
            object: An instance of this structure class.
            
        """

        if dictionary == None:
            return None
        else:	
            # Extract variables from the dictionary
            prices = None
            if dictionary.get("prices") != None:
                prices = list()
                for structure in dictionary.get("prices"):
                    prices.append(PriceEsitmate.from_dictionary(structure))
            # Return an object of this model
            return cls(prices)
