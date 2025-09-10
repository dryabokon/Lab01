docker_name="lab01"
docker run -it \
  -v "$(pwd)/data":/data \
  -v "$(pwd)/output":/output \
  -v "$(pwd)/src":/src \
  $docker_name bash -c "cd src && python main.py"