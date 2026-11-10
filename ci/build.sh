#!/bin/sh
# CI build script for macOS/Linux Jenkins agents ("Execute shell" build step).
set -u

echo "=== CI Build Started ==="
echo "Build: ${BUILD_NUMBER:-local}  Commit: ${GIT_COMMIT:-unknown}"

PYTHON="${PYTHON:-python3}"
"$PYTHON" --version || { echo "Python not found on agent"; exit 1; }

echo "=== Checking source files ==="
ls -la

echo "=== Compiling sources (syntax check) ==="
"$PYTHON" -m compileall -q app tests || { echo "COMPILE FAILED"; exit 1; }

echo "=== Running application ==="
"$PYTHON" -m app.calculator || { echo "APPLICATION FAILED TO RUN"; exit 1; }

echo "=== Running Application Tests ==="
if ! "$PYTHON" tests/run_tests.py; then
    echo "TESTS FAILED"
    exit 1
fi

echo "=== CI Build Completed Successfully ==="
exit 0
