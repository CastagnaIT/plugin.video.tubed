# -*- coding: utf-8 -*-
"""
    Copyright (C) 2020 Tubed (plugin.video.tubed)

    This file is part of plugin.video.tubed

    SPDX-License-Identifier: GPL-2.0-only
    See LICENSES/GPL-2.0-only.txt for more information.
"""

from .config import ADDON_ID
from .credentials import CREDENTIALS
from .modes import MODES
from .strings import STRINGS
from .time import ONE_DAY
from .time import ONE_HOUR
from .time import ONE_MINUTE
from .time import ONE_MONTH
from .time import ONE_WEEK

# the actual constants
__all__ = ['ADDON_ID', 'CREDENTIALS', 'MODES', 'STRINGS', 'ONE_MINUTE', 'ONE_HOUR', 'ONE_DAY',
           'ONE_WEEK', 'ONE_MONTH']

# the modules containing the constants
__all__ += ['config', 'credentials', 'modes', 'strings', 'time']
