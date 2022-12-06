#!/bin/bash

PACKAGE_NAME=Requisites-Generator
VERSION=$(plutil -extract version raw -o - src/info.plist)

ditto -ck src "$PACKAGE_NAME.$VERSION.alfredworkflow"
