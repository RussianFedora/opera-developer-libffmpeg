#!/bin/sh

INCORRECT_URL=0
DEBUG=1
REPACK=0

CHROMIUM_VER=$(rpm -q --specfile *.spec --qf "%{version}")
if [ "$DEBUG" = 1 ]; then
    echo "Chromium version: $CHROMIUM_VER"
fi

rm -rf chromium-$CHROMIUM_VER
if [ "$INCORRECT_URL" = 1 ]; then
    curl -sO https://chromium.googlesource.com/chromium/src.git/+archive/$CHROMIUM_VER.tar.gz
else
    curl -sO https://commondatastorage.googleapis.com/chromium-browser-official/chromium-$CHROMIUM_VER.tar.xz
fi

echo "Unpacking Chromium source archive..."
if [ "$INCORRECT_URL" = 1 ]; then
    mkdir -p chromium-$CHROMIUM_VER
    tar -xf $CHROMIUM_VER.tar.gz -C chromium-$CHROMIUM_VER
    rm $CHROMIUM_VER.tar.gz
else
    tar -xf chromium-$CHROMIUM_VER.tar.xz
fi

if [ -d chromium-$CHROMIUM_VER/native_client/toolchain ]; then
    if [ "$DEBUG" = 1 ]; then
        echo "Removing native_client/toolchain..."
    fi
    rm -rf toolchain
    REPACK=1
else
    if [ "$INCORRECT_URL" = 1 ]; then
        REPACK=1
    fi
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
