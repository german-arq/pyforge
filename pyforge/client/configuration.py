# Copyrigth(c) 2020, Germán Andrés Rojas Mahecha
# @AGORA BIM
# [www.agorabim.com](http://www.agorabim.com/)

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with this program. If not, see [https://www.gnu.org/licenses/](https://www.gnu.org/licenses/).

from .apiclient import ApiClient

class Configuration():

    """General settings"""
    
    def __init__(self, region: str='US'):        
               
        self.base_url = 'https://developer.api.autodesk.com'        
        self.api_client = ApiClient(self.base_url, self)
        self.access_token = None
        self.refresh_token = None
        self.region = region

    @property
    def default_headers(self):
        return {'Authorization': 'Bearer ' + self.access_token}

