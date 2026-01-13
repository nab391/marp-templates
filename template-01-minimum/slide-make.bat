cd "%~dp0"
docker run --rm -v "./src:/src" -v "./dist:/dist" marp-docker %*
