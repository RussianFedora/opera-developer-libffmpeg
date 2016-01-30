#!/bin/sh

DEBUG=1

CHROMIUM_VER=$(grep "%define chromium_ver" *.spec | cut --delimiter=\  --fields=3)
if [ "$DEBUG" = 1 ]; then
    echo "$CHROMIUM_VER"
fi

rm -rf chromium-$CHROMIUM_VER
curl -sO https://commondatastorage.googleapis.com/chromium-browser-official/chromium-$CHROMIUM_VER.tar.xz
tar -xf chromium-$CHROMIUM_VER.tar.xz

pushd chromium-$CHROMIUM_VER/native_client &> /dev/null || :
    if [ -d toolchain ]; then
        if [ "$DEBUG" = 1 ]; then
            echo "native_client/toolchain"
        fi
        rm -rf toolchain
    fi
popd &> /dev/null || :

tar cavf chromium-$CHROMIUM_VER.clipped.tar.xz chromium-$CHROMIUM_VER &> /dev/null || :
rm -rf chromium-$CHROMIUM_VER
