# Copyrigth(c) 2020, Germán Andrés Rojas Mahecha
# @AGORA BIM
# [www.agorabim.com](http://www.agorabim.com/)

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with this program. If not, see [https://www.gnu.org/licenses/](https://www.gnu.org/licenses/).
from __future__ import annotations
from typing import Dict
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .configuration import Configuration

import requests
import json
# from .apiresponse import ApiResponse
# from .apiexception import ApiException

class ApiClient():

    """Class for making the HTTP calls to the Forge API Backend"""
    
    def __init__(self, base_url: str, configuration: Configuration):
                
        self.base_url = base_url
        self.configuration = configuration     

    def call_api(self, method, local_url: str = "", headers: Dict = None, params: Dict = None, data: Dict = None):

        endpoint_url = self.base_url + local_url  

        response = requests.request(method, endpoint_url, params=params, data=data, headers=headers)

        return response
        

        # if str(r.status_code)[0] == '2':
        #     api_response = ApiResponse(r.status_code, r.headers, r.json()['data'])       
            
        # else:
        #     api_response = ApiException(r.status_code, r.json())
        
        



        

    

        
