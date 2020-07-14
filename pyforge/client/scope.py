# Copyrigth(c) 2020, Germán Andrés Rojas Mahecha
# @AGORA BIM
# [www.agorabim.com](http://www.agorabim.com/)

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with this program. If not, see [https://www.gnu.org/licenses/](https://www.gnu.org/licenses/).


class Scope():

    """Scope options for access tokens"""
    
    OPTIONS = {'userProfileRead': 'user-profile:read', \
                'userRead': 'user:read', \
                'userWrite': 'user:write', \
                'viewablesRead': 'viewables:read', \
                'dataRead': 'data:read', \
                'dataWrite': 'data:write', \
                'dataCreate': 'data:create', \
                'dataSearch': 'data:search', \
                'bucketCreate': 'bucket:create', \
                'bucketRead': 'bucket:read', \
                'bucketUpdate': 'bucket:update', \
                'bucketDelete': 'bucket:delete', \
                'codeAll': 'code:all', \
                'accountRead': 'account:read', \
                'accountWrite': 'account:write'
                }

    #@staticmethod    
    #def construct_scope_list():

    

