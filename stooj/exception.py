# $File: exception.py
# $Date: Mon Jan 30 11:04:20 2012 +0800
#
# This file is part of stooj
# 
# stooj is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# stooj is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with stooj.  If not, see <http://www.gnu.org/licenses/>.
#

class StoojError(Exception):
    pass

class StoojInnerError(StoojError):
    """Internal errors, usually caused by uncareful development.
    If this exception is caught, a page containing error message
    and bug reporting information should be presented to the user."""
    pass

class StoojRuntimeError(StoojError):
    """Runtime errors, usually caused by incorrect user operations."""
    pass

