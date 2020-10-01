# -*- coding: utf-8 -*-
"""
    Copyright (C) 2020 Tubed (plugin.video.tubed)

    This file is part of plugin.video.tubed

    SPDX-License-Identifier: GPL-2.0-only
    See LICENSES/GPL-2.0-only.txt for more information.
"""

import xbmc  # pylint: disable=import-error
import xbmcgui  # pylint: disable=import-error

from ..lib.memoizer import reset_cache
from ..lib.url_utils import unquote


def invoke(context, action, channel_id='', subscription_id='', channel_name=''):
    if '%' in channel_name:
        channel_name = unquote(channel_name)

    if action == 'add':
        if not channel_id:
            return

        payload = context.api.subscribe(channel_id)

        try:
            successful = int(payload.get('error', {}).get('code', 204)) == 204
        except ValueError:
            successful = False

        if successful:
            message = context.i18n('Subscribed')
            if channel_name:
                message = context.i18n('Subscribed to %s') % channel_name

            xbmcgui.Dialog().notification(
                context.addon.getAddonInfo('name'),
                message,
                context.addon.getAddonInfo('icon'),
                sound=False
            )

            reset_cache()

    elif action == 'remove':
        if not subscription_id:
            return

        payload = context.api.unsubscribe(subscription_id)

        try:
            successful = int(payload.get('error', {}).get('code', 204)) == 204
        except ValueError:
            successful = False

        if successful:
            message = context.i18n('Unsubscribed')
            if channel_name:
                message = context.i18n('Unsubscribed from %s') % channel_name

            xbmcgui.Dialog().notification(
                context.addon.getAddonInfo('name'),
                message,
                context.addon.getAddonInfo('icon'),
                sound=False
            )

            reset_cache()
            xbmc.executebuiltin('Container.Refresh')