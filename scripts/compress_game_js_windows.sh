#! /bin/bash

JS_PATH=C:/Users/Orrero/Desktop/acapp/game/static/game/js/
JS_PATH_DIST=${JS_PATH}dist/
JS_PATH_SRC=${JS_PATH}src/

find $JS_PATH_SRC -type f -name '*.js' | sort | xargs cat > ${JS_PATH_DIST}game.js


echo yes | python manage.py collectstatic