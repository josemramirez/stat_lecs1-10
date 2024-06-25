#!/bin/bash

## Modifico el manifest.json
#cp ./assets/manifest_ORIG.json ./assets/manifest.json
## Los detalles que van a salir en el App de Firefox
#sed -i -e 's/\"name\": \"myApp\"/\"name\": \"Nobita3\"/g' ./assets/manifest.json
#sed -i -e 's/\"short_name\"\: \"myApp\"/\"short_name\"\: \"Nobita3\"/g' ./assets/manifest.json
#sed -i -e 's/\"description\"\: \"myChat\"/\"description\"\: \"Nobita Chat3\"/g' ./assets/manifest.json

##
cp fly_toml_ORIG fly.toml 
#sed -i -e 's/app = \"myApp\"/app = \"nobita3\"/g' ./fly.toml
cp assistant_v1.py app.py
fly launch --wait-timeout 30000
