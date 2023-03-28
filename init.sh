# echo 'Starting Server'
# cd Server
# docker build -t server .
# echo 'Built the server'0
# cd ..
# cd Client
# docker build -t client .
# echo "Built the client"
# echo "....."
docker run --network=host -p 6677:6677 server



