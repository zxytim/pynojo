# $File: __init__.py
# $Date: Thu Feb 02 22:31:06 2012 +0800
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
"""
This module define the views for stooj. When initializing the application,
:meth:`pyramid.config.Configurator.scan` should be called on this module.

The following globals will be added to Chameleon templates:
    * *layout*: global layout macro
    * *_*: normal translation function (see
      :meth:`stooj.nls.Translator.get_translation`)
    * *_pl*: plural translation function (see
      :meth:`stooj.nls.Translator.get_plural_translation`)
"""

from os.path import dirname as _dirname, join as _join

from pyramid.events import subscriber, BeforeRender, NewResponse
from chameleon import PageTemplateFile as _PtFile

_layout_macro = _PtFile(_join(_dirname(__file__), 'template', 'layout.pt'))
@subscriber(BeforeRender)
def _add_global(event):
    # pylint: disable=W0212
    event['layout'] = _layout_macro
    event['_'] = event['request']._
    event['_pl'] = event['request']._pl


@subscriber(NewResponse)
def _chg_charset(event):
    event.response.charset = 'utf-8'

_route_list = list()    # list(kargs:dict)
_route_cnt = 0

def mkroute(**kargs):
    """Return a route name that can be passed to *pyramid.config.add_view*.
    :func:`setup_pyramid_route` should be called to add these routes to a config
    
    :param kargs: keyword arguments to be passed to *pyramid.config.add_route*.
        Note that it might be modified.  """
    global _route_list, _route_cnt
    name = 'mkrt-' + str(_route_cnt)
    _route_cnt += 1
    kargs['name'] = name
    _route_list.append(kargs)
    return name


def setup_pyramid_route(conf):
    """Setup pyramid routes used by :func:`mkroute`
    
    :param conf: the instance of *pyramid.conf.Configurator* to be configured
    """

    global _route_list
    for i in _route_list:
        conf.add_route(**i)

