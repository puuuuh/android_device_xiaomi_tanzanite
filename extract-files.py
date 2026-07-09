#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2025 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import blob_fixups_user_type, blob_fixup
from extract_utils.fixups_lib import (
    lib_fixup_remove_arch_suffix,
    lib_fixup_remove_proto_version_suffix,
    lib_fixup_vendorcompat,
    lib_fixups_user_type,
    libs_clang_rt_ubsan,
    libs_proto_3_9_1,
    libs_proto_21_12,
)
from extract_utils.fixups_lib import (
    lib_fixups,
    lib_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'device/xiaomi/tanzanite',
    "hardware/mediatek",
    'hardware/mediatek/libaedv',
    "hardware/mediatek/libmtkperf_client",
    "hardware/xiaomi"
]


lib_fixups: lib_fixups_user_type = {
    libs_clang_rt_ubsan: lib_fixup_remove_arch_suffix,
    libs_proto_3_9_1: lib_fixup_vendorcompat,
    libs_proto_21_12: lib_fixup_remove_proto_version_suffix,
}


def lib_fixup_vendor_suffix(lib: str, partition: str, *args, **kwargs):
    return f'{lib}_{partition}' if partition == 'vendor' else None


lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
    ('vendor.mediatek.hardware.videotelephony@1.0',): lib_fixup_vendor_suffix,
}

blob_fixups: blob_fixups_user_type = {
    (
        'vendor/lib64/hw/audio.primary.mediatek.so'
    ): blob_fixup()
        .replace_needed('android.hardware.audio.effect-V2-ndk.so', 'android.hardware.audio.effect-V3-ndk.so')
        .replace_needed('android.hardware.bluetooth.audio-V4-ndk.so', 'android.hardware.bluetooth.audio-V5-ndk.so'),
    (
        'vendor/lib64/libbluetooth_audio_session_aidl_mtk.so'
    ): blob_fixup()
        .replace_needed('android.hardware.bluetooth.audio-V5-ndk.so', 'android.hardware.bluetooth.audio-V5-ndk.so'),
    (
        'system_ext/bin/hw/android.hardware.audio.parameter_parser.service'
    ): blob_fixup()
        .replace_needed('av-audio-types-aidl-ndk.so', 'av-audio-types-aidl-ndk-vendor.so'),
    "vendor/lib64/libmorpho_video_stabilizer.so": blob_fixup()
        .add_needed("libutils.so"),
    (
        "vendor/lib64/android.hardware.audio.core-impl-mediatek.so",
    ): blob_fixup()
        .add_needed("libaudioutils_shim.so"),
    (
        'vendor/lib64/libmorpho_Ldc.so',
        'vendor/lib64/libTrueSight.so',
	    'vendor/lib64/libMiVideoFilter.so',
        'vendor/lib64/libneuralnetworks_sl_driver_mtk_prebuilt.so',
        'vendor/lib64/mt6789/libneuron_adapter_mgvi.so',
        'vendor/lib64/libMiPhotoFilter.so',
        'vendor/lib64/libMiVideoFilter.so',
        'vendor/lib64/libtflite_mtk.so'
    ): blob_fixup()
        .clear_symbol_version('AHardwareBuffer_acquire')
        .clear_symbol_version('AHardwareBuffer_allocate')
        .clear_symbol_version('AHardwareBuffer_describe')
        .clear_symbol_version('AHardwareBuffer_lock')
        .clear_symbol_version('AHardwareBuffer_lockPlanes')
        .clear_symbol_version('AHardwareBuffer_release')
        .clear_symbol_version('AHardwareBuffer_unlock')
        .clear_symbol_version('AHardwareBuffer_createFromHandle')
        .clear_symbol_version('AHardwareBuffer_getNativeHandle')
        .clear_symbol_version('AHardwareBuffer_isSupported'),
    (
        'vendor/lib64/mt6789/libneuralnetworks_sl_driver_mtk_prebuilt.so',
        'vendor/lib64/libnvram.so', 'vendor/lib64/libsysenv.so'
    ): blob_fixup()
        .add_needed('libbase_shim.so'),
    'vendor/lib64/hw/hwcomposer.mtk_common.so': blob_fixup()
        .add_needed('libprocessgroup_shim.so'),
    'vendor/lib64/mt6789/libmtkcam_hal_aidl_common.so': blob_fixup()
        .replace_needed('android.hardware.camera.common-V2-ndk.so', 'android.hardware.camera.common-V1-ndk.so'),
    (
        'vendor/bin/mnld',
        'vendor/lib64/libmifpext.so',
        'vendor/lib64/mt6789/libcam.utils.sensorprovider.so',
        'vendor/lib64/hw/mt6789/vendor.mediatek.hardware.pq_aidl-impl.so'
    ): blob_fixup()
        .replace_needed('android.hardware.sensors-V2-ndk.so', 'android.hardware.sensors-V3-ndk.so'),
    (
        'vendor/bin/hw/vendor.xiaomi.sensor.citsensorservice.aidl',
        'vendor/lib64/hw/audio.primary.mediatek.so',
        'vendor/lib64/hw/displayfeature.default.so',
        'vendor/lib64/hw/hwcomposer.mtk_common.so',
        'vendor/lib64/hw/mt6789/vendor.mediatek.hardware.pq_aidl-impl.so',
        'vendor/lib64/lib_power_applist.so',
        'vendor/lib64/libeffectsconfig.so',
        'vendor/lib64/libpowerhal.so',
        'vendor/lib64/libpqxmlflagparser.so',
        'vendor/lib64/libpqxmlparser.so',
        'vendor/lib64/librt_extamp_intf.so',
        'vendor/lib64/libsilkybrightnesscore.so',
        'vendor/lib64/hw/android.hardware.audio.effect.aidl-impl-mediatek.so',
        'vendor/lib64/hw/displayfeature.default.so',
        'vendor/lib64/hw/hwcomposer.mtk_common.so',
        'vendor/lib64/hw/mt6789/vendor.mediatek.hardware.pq_aidl-impl.so',
        'vendor/lib64/lib_power_applist.so',
        'vendor/lib64/libeffectsconfig.so',
        'vendor/lib64/libpowerhal.so',
        'vendor/lib64/libpqxmlflagparser.so',
        'vendor/lib64/libpqxmlparser.so',
        'vendor/lib64/librt_extamp_intf.so',
        'vendor/lib64/libsilkybrightnesscore.so',
    ): blob_fixup()
        .replace_needed('libtinyxml2.so', 'libtinyxml2-v34.so'),
    (
        'vendor/lib64/vendor.mediatek.hardware.pq_aidl-V3-ndk.so',
        'vendor/lib64/vendor.mediatek.hardware.pq_aidl-V7-ndk.so',
        'vendor/lib64/mt6789/libmtkcam_grallocutils.so',
        'vendor/lib64/hw/hwcomposer.mtk_common.so',
        'vendor/lib64/hw/mt6789/android.hardware.graphics.allocator-V2-mediatek.so',
        'vendor/lib64/hw/mt6789/mapper.mediatek.so',
        'vendor/lib64/libgpud.so',
        'vendor/lib64/libcodec2_fsr.so',
        'vendor/lib64/libcodec2_vpp_AIMEMC_plugin.so',
        'vendor/lib64/libcodec2_vpp_AISR_plugin.so',
        'vendor/bin/hw/mt6789/android.hardware.graphics.allocator-V2-service-mediatek.mt6789',
        'vendor/lib64/hw/mt6789/android.hardware.graphics.allocator-V2-mediatek.so',
        'vendor/lib64/vendor.mediatek.hardware.camera.isphal-V1-ndk.so',
    ): blob_fixup()
        .replace_needed('android.hardware.graphics.common-V6-ndk.so', 'android.hardware.graphics.common-V7-ndk.so')
        .replace_needed('android.hardware.graphics.common-V5-ndk.so', 'android.hardware.graphics.common-V7-ndk.so'),
    'vendor/bin/hw/android.hardware.wifi-service-lazy': blob_fixup()
        .replace_needed('android.hardware.wifi-V3-ndk.so', 'android.hardware.wifi-V4-ndk.so'),
    'vendor/etc/init/v3avpud-64b.rc': blob_fixup()
        .regex_replace('v3avpud-64b', 'v3avpud'),
}  # fmt: skip

module = ExtractUtilsModule(
    'tanzanite',
    'xiaomi',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
    check_elf=True,
    add_firmware_proprietary_file=True,
)

if __name__ == "__main__":
    utils = ExtractUtils.device(module)
    utils.run()
