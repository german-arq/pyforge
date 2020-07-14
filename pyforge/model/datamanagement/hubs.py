# Copyrigth(c) 2020, Germán Andrés Rojas Mahecha
# @AGORA BIM
# [www.agorabim.com](http://www.agorabim.com/)

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with this program. If not, see [https://www.gnu.org/licenses/](https://www.gnu.org/licenses/).

from __future__ import annotations
from typing import Dict

class Hub():
    
    """Return a collection of accesible hubs for this member"""
    
    def __init__(self, hubJsonData: Dict):
        
        self.type = hubJsonData.get('type')
        self.id = hubJsonData.get('id')
        self.attributes = HubAttributes(hubJsonData.get('attributes'))
        self.relationships = HubRelationships(hubJsonData.get('relationships'))

class HubAttributes():

    def __init__(self, attributes: Dict):

       self.name = attributes.get('name')
       self.extensionType = attributes.get('extension').get('type')
       self.extensionVersion = attributes.get('extension').get('version')
       self.extensionSchemaHref = attributes.get('extension').get('schema').get('href')
       self.extensionData = attributes.get('extension').get('data')
       self.region = attributes.get('region')
    
class HubRelationships():

    def __init__(self, relationships: Dict):

        self.projectsHref = relationships.get('projects').get('links').get('related').get('href')


    