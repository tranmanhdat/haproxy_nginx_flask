#Using haproxy server as a load balancer for nginx servers 
Enviroment: Ubuntu 18.04.5 LTS + docker 
![system](./images/haproxy%20(1).png)
## To run
1. [install docker](https://docs.docker.com/engine/install/)
2. Run: docker-compose up -d
3. Open browser (google chrome,...) and access [http://0.0.0.0/](http://0.0.0.0/) to see response
4. Access [http://0.0.0.0:8900/stats](http://0.0.0.0:8900/stats) to see stats of haproxy server
5. Dont forget remove docker-compose when dont need anymore: docker-compose down