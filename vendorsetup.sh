TARGET_FILE="frameworks/base/packages/SystemUI/src/com/android/systemui/biometrics/UdfpsSurfaceView.java"

# https://github.com/crdroidandroid/android_frameworks_base/commit/24501ff1bdc0ba56d14eccc89fd65db2cf21aabe.diff
UDFPS_PATCH="
diff --git a/packages/SystemUI/src/com/android/systemui/biometrics/UdfpsSurfaceView.java b/packages/SystemUI/src/com/android/systemui/biometrics/UdfpsSurfaceView.java
index 3bfdddea37d55..dae25f71af0f9 100644
--- a/packages/SystemUI/src/com/android/systemui/biometrics/UdfpsSurfaceView.java
+++ b/packages/SystemUI/src/com/android/systemui/biometrics/UdfpsSurfaceView.java
@@ -41,7 +41,7 @@ public class UdfpsSurfaceView extends SurfaceView implements SurfaceHolder.Callb
     /**
      * Notifies {@link UdfpsView} when to enable GHBM illumination.
      */
-    interface GhbmIlluminationListener {
+    public interface GhbmIlluminationListener {
         /**
          * @param surface the surface for which GHBM should be enabled.
          * @param onDisplayConfigured a runnable that should be run after GHBM is enabled.
"

if echo "$UDFPS_PATCH" | patch -f -d "$ANDROID_BUILD_TOP/frameworks/base/" -p1 --dry-run > /dev/null; then
    echo "Apply patch for udfps"
    echo "$UDFPS_PATCH" | patch -f -d "$ANDROID_BUILD_TOP/frameworks/base/" -p1
fi
