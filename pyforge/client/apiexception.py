# Copyrigth(c) 2020, Germán Andrés Rojas Mahecha
# @AGORA BIM
# [www.agorabim.com](http://www.agorabim.com/)

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with this program. If not, see [https://www.gnu.org/licenses/](https://www.gnu.org/licenses/).

from typing import Dict
import requests
import json

class ApiException():

    """Class for manage Errors in the API Responde"""
    
    def __init__(self, error_code: int, error_content: Dict[str, str]):
                
        self.error_code = error_code
        self.error_content = error_content




        

    

        
