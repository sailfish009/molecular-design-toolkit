# Copyright 2017 Autodesk Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
Exposes the correct version of pathlib, with some compatibility help for python 2
"""
from __future__ import absolute_import
from future.utils import PY2 as _PY2

if _PY2:
    from pathlib2 import *

    try:
        import pathlib as _backportpathlib
    except ImportError:
        _backportpathlib = None

    if _backportpathlib:
        def _backport_pathlib_fixup(p):
            if isinstance(p, _backportpathlib.Path):
                return Path(str(p))
            else:
                return p
    else:
        def _backport_pathlib_fixup(p):
            return p

else:
    from pathlib import *