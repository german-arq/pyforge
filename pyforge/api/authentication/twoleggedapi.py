# Copyrigth(c) 2020, Germán Andrés Rojas Mahecha
# @AGORA BIM
# [www.agorabim.com](http://www.agorabim.com/)

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with this program. If not, see [https://www.gnu.org/licenses/](https://www.gnu.org/licenses/).

import requests

class TwoLeggedApi():

    """Simple Authentication without user login"""
       
    def __init__(self, cliend_id, cliend_secret, scope):
        
        self.url = 'https://developer.api.autodesk.com/authentication/v1/authenticate'
        self.data = {'client_id': cliend_id, 'client_secret': cliend_secret, 'grant_type': 'client_credentials', 'scope': scope}
        self.headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    def authenticate(self):
        response = requests.request('POST', self.url, data=self.data, headers=self.headers)

        if response.status_code == 200:
            return response
        
        else:
            return "Error {}".format(response.status_code)
