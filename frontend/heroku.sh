#!/usr/bin/env bash
export NODE_ENV=development # HACK
echo "Installing npm packages..."
npm install
echo "Building static asserts..."
npm run build
echo "Done!"
