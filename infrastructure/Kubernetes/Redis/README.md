# Redis Deployment Guide for (2 Agents to 2 Worker Ratio)

Run this command via kubectl. Type yes if prompted.
```shell 
kubectl exec -it redis-cluster-0 -- redis-cli --cluster create --cluster-replicas 1 $(kubectl get pods -l app=redis-cluster -o jsonpath='{range.items[*]}{.status.podIP}:6379 ')
```
Check Redis Cluster Deployment
```shell
kubectl exec -it redis-cluster-0 -- redis-cli cluster info
```
Check Each Node's Information 
```shell
for x in $(seq 0 3); do echo "redis-cluster-$x"; kubectl exec redis-cluster-$x -- redis-cli role; echo; done
```
 You should be done after that :)