# -*- coding: utf-8 -*-
"""
    Copyright (C) 2020 Tubed (plugin.video.tubed)

    This file is part of plugin.video.tubed

    SPDX-License-Identifier: GPL-2.0-only
    See LICENSES/GPL-2.0-only.txt for more information.
"""

from html import unescape

from ..constants import MODES
from ..items.directory import Directory
from ..lib.url_utils import create_addon_path


def playlist_generator(items):
    for item in items:
        playlist_id = ''

        kind = item.get('kind', '')
        snippet = item.get('snippet', {})

        if not kind or kind not in ['youtube#playlist', 'youtube#searchResult']:
            continue

        if not snippet:
            continue

        if kind == 'youtube#playlist':
            playlist_id = item.get('id', '')

        elif kind == 'youtube#searchResult':
            playlist_id = item.get('id', {}).get('playlistId')

        if not playlist_id:
            continue

        payload = Directory(
            label=unescape(snippet.get('title', '')),
            label2=unescape(snippet.get('channelTitle', '')),
            path=create_addon_path({
                'mode': str(MODES.PLAYLIST),
                'playlist_id': playlist_id
            })
        )

        info_labels = {
            'plot': unescape(snippet.get('description', '')),
            'plotoutline': unescape(snippet.get('description', '')),
            'originaltitle': unescape(snippet.get('title', '')),
            'sorttitle': unescape(snippet.get('title', '')),
            'studio': unescape(snippet.get('channelTitle', ''))
        }
        payload.ListItem.setInfo('video', info_labels)

        thumbnails = snippet.get('thumbnails', {})
        thumbnail = thumbnails.get('standard', thumbnails.get('high', {}))
        if not thumbnail:
            thumbnail = thumbnails.get('medium', thumbnails.get('default', {}))
        thumbnail = thumbnail.get('url', '')

        payload.ListItem.setArt({
            'icon': thumbnail,
            'thumb': thumbnail,
        })

        yield tuple(payload)