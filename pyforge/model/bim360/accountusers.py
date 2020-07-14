# Copyrigth(c) 2020, Germán Andrés Rojas Mahecha
# @AGORA BIM
# [www.agorabim.com](http://www.agorabim.com/)

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with this program. If not, see [https://www.gnu.org/licenses/](https://www.gnu.org/licenses/).

from __future__ import annotations
from typing import Dict

class AccountUsers():
    
    """Return all the users in a specific BIM360 account"""
    
    def __init__(self, accountUsersData: Dict):
        
        self.id = accountUsersData.get('id')
        self.account_id = accountUsersData.get('account_id')
        self.role = accountUsersData.get('role')
        self.status = accountUsersData.get('status')
        self.company_id = accountUsersData.get('company_id')
        self.company_name = accountUsersData.get('company_name')
        self.last_sign_in = accountUsersData.get('last_sign_in')
        self.email = accountUsersData.get('email')
        self.name = accountUsersData.get('name')
        self.nickname = accountUsersData.get('nickname')
        self.first_name = accountUsersData.get('first_name')
        self.last_name = accountUsersData.get('last_name')
        self.uid = accountUsersData.get('uid')
        self.image_url = accountUsersData.get('image_url')
        self.address_line_1 = accountUsersData.get('address_line_1')
        self.address_line_2 = accountUsersData.get('address_line_2')
        self.city = accountUsersData.get('city')
        self.state_or_province = accountUsersData.get('state_or_province')
        self.postal_code = accountUsersData.get('postal_code')
        self.country = accountUsersData.get('country')
        self.phone = accountUsersData.get('phone')
        self.company = accountUsersData.get('company')
        self.job_tittle = accountUsersData.get('job_title')
        self.industry = accountUsersData.get('industry')
        self.about_me = accountUsersData.get('about_me')
        self.created_at = accountUsersData.get('created_at')
        self.updated_at = accountUsersData.get('updated_at')




    