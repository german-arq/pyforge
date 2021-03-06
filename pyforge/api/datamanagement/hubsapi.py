# Copyrigth(c) 2020, Germán Andrés Rojas Mahecha
# @AGORA BIM
# [www.agorabim.com](http://www.agorabim.com/)

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with this program. If not, see [https://www.gnu.org/licenses/](https://www.gnu.org/licenses/).

from typing import List
from ...client.apiresponse import ApiResponse
from ...client.apiexception import ApiException

class HubsApi():

    """Functions to interact with the Hubs API Endpoints"""
       
    def __init__(self, configuration):
        
        self.configuration = configuration     
        
    def get_hubs(self, filterId: List[str]=None, filterName: List[str]=None):
        
        method = 'GET'
        local_url = '/project/v1/hubs'
        headers = self.configuration.default_headers   

        query = {}
        if filterId:
            query.update({'filter[id]': ','.join(filterId)})
        elif filterName:
            query.update({'filter[name]': ','.join(filterName)})

        api_response = self.configuration.api_client.call_api(method, local_url, headers, query)
        
        if api_response.status_code == 200:
            return ApiResponse(api_response.status_code, api_response.headers, api_response.json().get('data'))
        
        else:
            return ApiException(api_response.status_code, api_response.json())