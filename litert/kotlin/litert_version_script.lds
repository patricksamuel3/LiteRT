VERS_1.0 {
  # Export JNI and native C symbols.
  global:
    TfLite*;
    LiteRt*;

  # Hide everything else.
  local:
    *;
};
