<<<<<<<< HEAD:.tmp_rules_android/unpack/rules_android-0.7.1/rules/acls/aar_import_deps_checker.bzl
# Copyright 2020 The Bazel Authors. All rights reserved.
========
# Copyright 2026 Google LLC.
>>>>>>>> origin:litert/python/litert_wrapper/environment_wrapper/_pywrap_litert_environment_wrapper.pyi
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
<<<<<<<< HEAD:.tmp_rules_android/unpack/rules_android-0.7.1/rules/acls/aar_import_deps_checker.bzl
#    http://www.apache.org/licenses/LICENSE-2.0
========
#      http://www.apache.org/licenses/LICENSE-2.0
>>>>>>>> origin:litert/python/litert_wrapper/environment_wrapper/_pywrap_litert_environment_wrapper.pyi
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
<<<<<<<< HEAD:.tmp_rules_android/unpack/rules_android-0.7.1/rules/acls/aar_import_deps_checker.bzl
"""Allowlist to run ImportDepsChecker on aar_import.

See b/148478031 for context.
"""

load("//rules:visibility.bzl", "PROJECT_VISIBILITY")

visibility(PROJECT_VISIBILITY)

# keep sorted
AAR_IMPORT_DEPS_CHECKER_ROLLOUT = [
    "//:__subpackages__",
]

# keep sorted
AAR_IMPORT_DEPS_CHECKER_FALLBACK = [
]
========

"""Python type stubs for the LiteRT environment wrapper."""

def CreateEnvironment(
        runtime_path: str = ...,
        compiler_plugin_path: str = ...,
        dispatch_library_path: str = ...
) -> object:
    """Creates a LiteRT environment capsule."""
    ...
>>>>>>>> origin:litert/python/litert_wrapper/environment_wrapper/_pywrap_litert_environment_wrapper.pyi
