# -*- coding: utf-8 -*-

"""
    uberapilib.models.request_body
 
    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ) on 07/19/2016
"""

from uberapilib.models.base_model import BaseModel


class RequestBody(BaseModel):

    """Implementation of the 'Request Body' model.

    Request body containing post body parameters

    Attributes:
        end_latitude (float): The final or destination latitude.
        end_longitude (float): The final or destination longitude.
        product_id (string): The unique ID of the product being requested.
        start_latitude (float): The beginning or "pickup" latitude.
        start_longitude (float): The beginning or "pickup" longitude.
        surge_confirmation_id (string): The unique identifier of the surge
            session for a user. Required when returned from a 409 Conflict
            response on previous POST attempt.

    """

    def __init__(self, 
                 end_latitude = None,
                 end_longitude = None,
                 product_id = None,
                 start_latitude = None,
                 start_longitude = None,
                 surge_confirmation_id = None):
        """Constructor for the RequestBody class"""
        
        # Initialize members of the class
        self.end_latitude = end_latitude
        self.end_longitude = end_longitude
        self.product_id = product_id
        self.start_latitude = start_latitude
        self.start_longitude = start_longitude
        self.surge_confirmation_id = surge_confirmation_id

        # Create a mapping from Model property names to API property names
        self.names = {
            "end_latitude": "end_latitude",
            "end_longitude": "end_longitude",
            "product_id": "product_id",
            "start_latitude": "start_latitude",
            "start_longitude": "start_longitude",
            "surge_confirmation_id": "surge_confirmation_id",
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
            end_latitude = dictionary.get("end_latitude")
            end_longitude = dictionary.get("end_longitude")
            product_id = dictionary.get("product_id")
            start_latitude = dictionary.get("start_latitude")
            start_longitude = dictionary.get("start_longitude")
            surge_confirmation_id = dictionary.get("surge_confirmation_id")
            # Return an object of this model
            return cls(end_latitude,
                       end_longitude,
                       product_id,
                       start_latitude,
                       start_longitude,
                       surge_confirmation_id)
