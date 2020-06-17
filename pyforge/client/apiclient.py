# Copyrigth(c) 2020, Germán Andrés Rojas Mahecha
# @AGORA BIM
# [www.agorabim.com](http://www.agorabim.com/)

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with this program. If not, see [https://www.gnu.org/licenses/](https://www.gnu.org/licenses/).

from typing import Dict
import requests
import json

from configuration import Configuration

class ApiClient():

    """Class for making the HTTP calls to the Forge API Backend"""
    
    def __init__(self, method, configuration: Configuration, base_url: str = None, local_url: str = "", headers: Dict = None, params: Dict = None, data: Dict = None):

        self.method = method
        self.configuration = configuration
        if base_url:
            self.base_url = base_url
        else:
            self.base_url = "https://developer.api.autodesk.com/"
        self.local_url = local_url
        self.headers = {'Content-Type': 'application', 'Authorization': 'Bearer {0}'.format(self.configuration.access_token)} 
        self.headers.update(headers) 
        self.params = {'scope': 'account:read', 'grant_type': 'client_credentials'}
        self.params.update(params)
        self.data = data            
        self.endpoint_url = base_url + local_url

    def request(self):
        response = requests.request(self.method, self.endpoint_url, params=self.params, data=self.data, headers=self.headers)
        return response



        

    

        
