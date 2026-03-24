# buildifier: disable=load-on-top

workspace(name = "litert")

# buildifier: disable=load-on-top

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "rules_shell",
    sha256 = "bc61ef94facc78e20a645726f64756e5e285a045037c7a61f65af2941f4c25e1",
    strip_prefix = "rules_shell-0.4.1",
    url = "https://github.com/bazelbuild/rules_shell/releases/download/v0.4.1/rules_shell-v0.4.1.tar.gz",
)

load("@rules_shell//shell:repositories.bzl", "rules_shell_dependencies", "rules_shell_toolchains")

rules_shell_dependencies()

rules_shell_toolchains()

http_archive(
    name = "rules_platform",
    sha256 = "0aadd1bd350091aa1f9b6f2fbcac8cd98201476289454e475b28801ecf85d3fd",
    urls = [
        "https://github.com/bazelbuild/rules_platform/releases/download/0.1.0/rules_platform-0.1.0.tar.gz",
    ],
)


# Configure Android SDK and NDK repositories for kt_android_library
# This registers the Android SDK toolchain that rules_kotlin requires
http_archive(
    name = "rules_android",
    sha256 = "7c45b6aaa837fb6f2f23ad11387638cb00fa9f839a04ec564caac70a543a9cd5",
    strip_prefix = "rules_android-0.7.1",
    url = "https://github.com/bazelbuild/rules_android/releases/download/v0.7.1/rules_android-v0.7.1.tar.gz",
)

load("@rules_android//rules:rules.bzl", "android_sdk_repository")
load("@bazel_tools//tools/build_defs/repo:android.bzl", "android_ndk_repository")

android_sdk_repository(
    name = "androidsdk",
    api_level = 35,
)

android_ndk_repository(
    name = "androidndk",
    api_level = 26,
)

load(
    "@xla//third_party/py:python_wheel.bzl",
    "python_wheel_version_suffix_repository",
)

python_wheel_version_suffix_repository(name = "tf_wheel_version_suffix")

# Toolchains for ML projects hermetic builds.
# Details: https://github.com/google-ml-infra/rules_ml_toolchain
http_archive(
    name = "rules_ml_toolchain",
    sha256 = "9dbee8f24cc1b430bf9c2a6661ab70cbca89979322ddc7742305a05ff637ab6b",
    strip_prefix = "rules_ml_toolchain-545c80f1026d526ea9c7aaa410bf0b52c9a82e74",
    urls = [
        "https://github.com/google-ml-infra/rules_ml_toolchain/archive/545c80f1026d526ea9c7aaa410bf0b52c9a82e74.tar.gz",
    ],
)

load(
    "@rules_ml_toolchain//cc/deps:cc_toolchain_deps.bzl",
    "cc_toolchain_deps",
)

cc_toolchain_deps()

register_toolchains("@rules_ml_toolchain//cc:linux_x86_64_linux_x86_64")

# load(
#     "@rules_ml_toolchain//gpu/cuda:cuda_json_init_repository.bzl",
#     "cuda_json_init_repository",
# )
# 
# cuda_json_init_repository()
#
# load(
#     "@cuda_redist_json//:distributions.bzl",
#     "CUDA_REDISTRIBUTIONS",
#     "CUDNN_REDISTRIBUTIONS",
# )
# load(
#     "@rules_ml_toolchain//gpu/cuda:cuda_redist_init_repositories.bzl",
#     "cuda_redist_init_repositories",
#     "cudnn_redist_init_repository",
# )
#
# cuda_redist_init_repositories(
#     cuda_redistributions = CUDA_REDISTRIBUTIONS,
# )

# load(
#     "@rules_ml_toolchain//gpu/cuda:cuda_redist_init_repositories.bzl",
#     "cudnn_redist_init_repository",
# )
# 
# cudnn_redist_init_repository(
#     cudnn_redistributions = CUDNN_REDISTRIBUTIONS,
# )

load(
    "@rules_ml_toolchain//gpu/cuda:cuda_configure.bzl",
    "cuda_configure",
)

cuda_configure(name = "local_config_cuda")

load(
    "@rules_ml_toolchain//gpu/nccl:nccl_redist_init_repository.bzl",
    "nccl_redist_init_repository",
)

nccl_redist_init_repository()

load(
    "@rules_ml_toolchain//gpu/nccl:nccl_configure.bzl",
    "nccl_configure",
)

nccl_configure(name = "local_config_nccl")

load("//third_party/tqdm:workspace.bzl", tqdm = "repo")

tqdm()

load("//third_party/dawn:workspace.bzl", dawn = "repo")

dawn()

load("//third_party/lark:workspace.bzl", lark = "repo")

lark()

load("//third_party/xdsl:workspace.bzl", xdsl = "repo")

xdsl()

load("@rules_jvm_external//:defs.bzl", "maven_install")

maven_install(
    name = "litert_maven",
    artifacts = [
        "androidx.lifecycle:lifecycle-common:2.8.7",
        "com.google.android.play:ai-delivery:0.1.1-alpha01",
        "com.google.guava:guava:33.4.6-android",
        "org.jetbrains.kotlinx:kotlinx-coroutines-android:1.8.0",
        "org.jetbrains.kotlinx:kotlinx-coroutines-guava:1.8.0",
        "org.jetbrains.kotlinx:kotlinx-coroutines-play-services:1.8.0",
    ],
    repositories = [
        "https://jcenter.bintray.com",
        "https://maven.google.com",
        "https://dl.google.com/dl/android/maven2",
        "https://repo1.maven.org/maven2",
    ],
    version_conflict_policy = "pinned",
)

# Kotlin rules
http_archive(
    name = "rules_kotlin",
    sha256 = "e1448a56b2462407b2688dea86df5c375b36a0991bd478c2ddd94c97168125e2",
    url = "https://github.com/bazelbuild/rules_kotlin/releases/download/v2.1.3/rules_kotlin-v2.1.3.tar.gz",
)

# Sentencepiece
http_archive(
    name = "sentencepiece",
    build_file = "@//:BUILD.sentencepiece",
    patch_cmds = [
        # Empty config.h seems enough.
        "touch config.h",
        # Replace third_party/absl/ with absl/ in *.h and *.cc files.
        "sed -i -e 's|#include \"third_party/absl/|#include \"absl/|g' *.h *.cc",
        # Replace third_party/darts_clone/ with include/ in *.h and *.cc files.
        "sed -i -e 's|#include \"third_party/darts_clone/|#include \"include/|g' *.h *.cc",
    ],
    patches = ["@//:PATCH.sentencepiece"],
    sha256 = "9970f0a0afee1648890293321665e5b2efa04eaec9f1671fcf8048f456f5bb86",
    strip_prefix = "sentencepiece-0.2.0/src",
    url = "https://github.com/google/sentencepiece/archive/refs/tags/v0.2.0.tar.gz",
)

# Darts Clone
http_archive(
    name = "darts_clone",
    build_file = "@//:BUILD.darts_clone",
    sha256 = "4a562824ec2fbb0ef7bd0058d9f73300173d20757b33bb69baa7e50349f65820",
    strip_prefix = "darts-clone-e40ce4627526985a7767444b6ed6893ab6ff8983",
    url = "https://github.com/s-yata/darts-clone/archive/e40ce4627526985a7767444b6ed6893ab6ff8983.tar.gz",
)

# tomlplusplus
http_archive(
    name = "tomlplusplus",
    build_file = "@//:BUILD.tomlplusplus",
    patch_cmds = [
        "echo '#define TOML_IMPLEMENTATION' > toml.cc",
        "echo '#include \"toml.hpp\"' >> toml.cc",
    ],
    sha256 = "8517f65938a4faae9ccf8ebb36631a38c1cadfb5efa85d9a72e15b9e97d25155",
    strip_prefix = "tomlplusplus-3.4.0",
    url = "https://github.com/marzer/tomlplusplus/archive/refs/tags/v3.4.0.tar.gz",
)

load("@rules_kotlin//kotlin:repositories.bzl", "kotlin_repositories")

kotlin_repositories()  # if you want the default. Otherwise see custom kotlinc distribution below

load("@rules_kotlin//kotlin:core.bzl", "kt_register_toolchains")

kt_register_toolchains()  # to use the default toolchain, otherwise see toolchains below

load("//third_party/stblib:workspace.bzl", stblib = "repo")

stblib()

# TEST DATA ########################################################################################

load("//third_party/models:workspace.bzl", "models")

models()

# VENDOR SDKS ######################################################################################

# QUALCOMM ---------------------------------------------------------------------------------------

# The actual macro call will be set during configure for now.
load("//third_party/qairt:workspace.bzl", "qairt")

qairt()

# MEDIATEK ---------------------------------------------------------------------------------------

# Currently only works with local sdk
load("//third_party/neuro_pilot:workspace.bzl", "neuro_pilot")

neuro_pilot()

# GOOGLE TENSOR ----------------------------------------------------------------------------------
load("//third_party/google_tensor:workspace.bzl", "google_tensor")

google_tensor()

# LiteRT GPU ----------------------------------------------------------------------------------
load("//third_party/litert_gpu:workspace.bzl", "litert_gpu")

litert_gpu()

# LiteRT Prebuilts ---------------------------------------------------------------------------------
load("//third_party/litert_prebuilts:workspace.bzl", "litert_prebuilts")

litert_prebuilts()

# INTEL OPENVINO ---------------------------------------------------------------------------------
load("//third_party/intel_openvino:openvino.bzl", "openvino_configure")

openvino_configure()
