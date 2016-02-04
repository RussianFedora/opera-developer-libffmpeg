#!/bin/sh

DEBUG=1
REPACK=0

CHROMIUM_VER=$(rpm -q --specfile *.spec --qf "%{version}")
if [ "$DEBUG" = 1 ]; then
    echo "Chromium version: $CHROMIUM_VER"
fi

rm -rf chromium-$CHROMIUM_VER
curl -sO https://commondatastorage.googleapis.com/chromium-browser-official/chromium-$CHROMIUM_VER.tar.xz
echo "Unpacking Chromium source archive..."
tar -xf chromium-$CHROMIUM_VER.tar.xz

if [ -d chromium-$CHROMIUM_VER/native_client/toolchain ]; then
    if [ "$DEBUG" = 1 ]; then
        echo "Removing native_client/toolchain..."
    fi
    rm -rf toolchain
    REPACK=1
fi

if [ "$REPACK" = 1 ]; then
    if [ "$DEBUG" = 1 ]; then
        echo "Repacking Chromium source..."
    fi
    tar caf chromium-$CHROMIUM_VER.clipped.tar.xz chromium-$CHROMIUM_VER
else
    if [ "$DEBUG" = 1 ]; then
        echo "Renaming Chromium source..."
    fi
    mv chromium-$CHROMIUM_VER.tar.xz chromium-$CHROMIUM_VER.clipped.tar.xz
fi

rm -rf chromium-$CHROMIUM_VER
