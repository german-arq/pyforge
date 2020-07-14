# Copyrigth(c) 2020, Germán Andrés Rojas Mahecha
# @AGORA BIM
# [www.agorabim.com](http://www.agorabim.com/)

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with this program. If not, see [https://www.gnu.org/licenses/](https://www.gnu.org/licenses/).

import requests

class ThreeLeggedApi():

    """Authentication with user login"""
       
    def __init__(self, cliend_id: str, cliend_secret: str, scope: str, callback_url:str):        
        
        self.client_id = cliend_id
        self.client_secret = cliend_secret
        self.callback_url = callback_url
        self.scope = scope
        self.default_headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        self.default_params = {'client_id': self.client_id, 'client_secret': self.client_secret}
        
    def url_for_authorization_code(self):

        end_point_url = 'https://developer.api.autodesk.com/authentication/v1/authorize'
        response_type = "response_type=code"

        url_authorization_code = end_point_url + "?" + response_type + "&" + "client_id=" + self.client_id + "&" + "redirect_uri=" + self.callback_url + "&" + "scope=" + self.scope

        return url_authorization_code
    
    def get_token(self, auth_code: str):
        
        end_point_url = 'https://developer.api.autodesk.com/authentication/v1/gettoken'

        headers = self.default_headers
        
        params = self.default_params
        params.update({'grant_type': 'authorization_code', 'code': auth_code, 'redirect_uri': self.callback_url})
 
        access_token = requests.request('POST', end_point_url, data=params, headers=headers)

        if access_token.status_code == 200:
            return access_token       
        else:
            return "Error {}".format(access_token.status_code)

    def refresh_token(self, refresh_token: str, scope: str=None):
        
        end_point_url = 'https://developer.api.autodesk.com/authentication/v1/refreshtoken'

        headers = self.default_headers
        
        params = self.default_params
        params.update({'grant_type': 'refresh_token', 'refesh_token': refresh_token, 'scope': scope})

        new_token = requests.request('POST', end_point_url, data=params, headers=headers)

        return new_token




