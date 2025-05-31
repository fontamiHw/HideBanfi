echo "clean docker paths"
rm -rf host
rm -rf app

echo "Coping all the python files"
mkdir -p app
cp -R ../OtdrBot/src/* app/.

echo "create directory for mount volume"
mkdir -p host/resources


echo "Docker image 'CiscoBanfi' generating"
docker build -t cisco-banfi .

