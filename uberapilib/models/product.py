# -*- coding: utf-8 -*-

"""
    uberapilib.models.product
 
    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ) on 07/19/2016
"""

from uberapilib.models.base_model import BaseModel


class Product(BaseModel):

    """Implementation of the 'Product' model.

    Describes a product with its image and capacity

    Attributes:
        capacity (int): Capacity of product. For example, 4 people.
        description (string): Description of product.
        display_name (string): Display name of product.
        image (string): Image URL representing the product.
        product_id (string): Unique identifier representing a specific product
            for a given latitude & longitude. For example, uberX in San
            Francisco will have a different product_id than uberX in Los
            Angeles.

    """

    def __init__(self, 
                 capacity = None,
                 description = None,
                 display_name = None,
                 image = None,
                 product_id = None):
        """Constructor for the Product class"""
        
        # Initialize members of the class
        self.capacity = capacity
        self.description = description
        self.display_name = display_name
        self.image = image
        self.product_id = product_id

        # Create a mapping from Model property names to API property names
        self.names = {
            "capacity": "capacity",
            "description": "description",
            "display_name": "display_name",
            "image": "image",
            "product_id": "product_id",
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
            capacity = dictionary.get("capacity")
            description = dictionary.get("description")
            display_name = dictionary.get("display_name")
            image = dictionary.get("image")
            product_id = dictionary.get("product_id")
            # Return an object of this model
            return cls(capacity,
                       description,
                       display_name,
                       image,
                       product_id)
