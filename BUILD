# Copyright 2025 The Google AI Edge Authors. All Rights Reserved.
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

# The default `android_sdk_repository` inside `rules_android` v0.7.1 registers toolchains using the type `@rules_android//toolchains/android:sdk_toolchain_type`.
# However, the native `android_binary` rules inside `@org_tensorflow` are mapped to the older `@@bazel_tools//tools/android:sdk_toolchain_type`.
# When running outside of Bzlmod (i.e. `WORKSPACE` mode), Bazel does not inject the legacy type aliases, causing "No matching toolchains found".
# Here, we explicitly register dummy toolchains bound to the `@@bazel_tools` type but returning the `rules_android` generated toolchain arrays.
toolchain(
    name = "fallback_legacy_android_sdk_toolchain",
    toolchain = "@androidsdk//:sdk",
    toolchain_type = "@bazel_tools//tools/android:sdk_toolchain_type",
    target_compatible_with = [
        "@platforms//os:android",
    ],
)
