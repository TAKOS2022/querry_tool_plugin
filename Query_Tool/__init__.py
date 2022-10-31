# -*- coding: utf-8 -*-
"""
/***************************************************************************
 QueryTool
                                 A QGIS plugin
 The plugin is use to make query on shapefile
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2022-08-16
        copyright            : (C) 2022 by Previan 
        email                : jjtakodjou@pavemetrics.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""
# Test debug
import os
import shutil
if os.environ.get("QGIS_DEBUGPY_HAS_LOADED"):
    try:
        import debugpy
        debugpy.configure(python=shutil.which("python"))
        debugpy.listen(('localhost', 5678))
    except Exception as e:
        print("Unable to create debugpy debugger: {}".format(e))
    else:
        os.environ["QGIS_DEBUGPY_HAS_LOADED"] = "1"





# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load QueryTool class from file QueryTool.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .Query_Tool import QueryTool
    return QueryTool(iface)
