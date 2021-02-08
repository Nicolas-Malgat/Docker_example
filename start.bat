set app="flask"

docker build -t %app% .
docker run --rm -d --name %app% -p 80:5000 %app% -v C:\Users\utilisateur\Documents\Docker_flask:/app