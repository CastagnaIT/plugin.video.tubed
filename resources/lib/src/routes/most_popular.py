# -*- coding: utf-8 -*-
"""
    Copyright (C) 2020 Tubed (plugin.video.tubed)

    This file is part of plugin.video.tubed

    SPDX-License-Identifier: GPL-2.0-only
    See LICENSES/GPL-2.0-only.txt for more information.
"""

import xbmcplugin  # pylint: disable=import-error

# from ..constants import MODES
# from ..lib.items.next_page import NextPage
# from ..lib.items.video import Video
# from ..lib.url_utils import create_addon_path


def invoke(context, page_token=''):
    _ = page_token
    items = []

    xbmcplugin.addDirectoryItems(context.handle, items, len(items))

    xbmcplugin.endOfDirectory(context.handle, True)