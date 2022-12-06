#!/bin/bash

PACKAGE_NAME=Requisites-Generator
VERSION=$(plutil -extract version raw -o - src/info.plist)

zip -r $PACKAGE_NAME.$VERSION.alfredworkflow src