# Handy commands
## Set up control plane:
```
sudo kubeadm init --pod-network-cidr=10.244.0.0/16
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config
kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml
```

## Get docker image from private repo:
```
kubectl create secret generic regcred \
    --from-file=.dockerconfigjson=/home/naman/.docker/config.json \
    --type=kubernetes.io/dockerconfigjson
```

## Set up raspberry pi node:

on node: `sudo kubeadm join [your unique string from the kubeadm init command]`

## Label Node

label node as RaspberryPi: `kubectl label nodes raspberrypi4 raspberrypi=4 --overwrite`
## Set up dashboard
```
kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.0.0/aio/deploy/recommended.yaml

kubectl proxy

```
go to: `http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/`

### Auth token: 
```
kubectl create serviceaccount dashboard-admin-sa
kubectl create clusterrolebinding dashboard-admin-sa \
--clusterrole=cluster-admin --serviceaccount=default:dashboard-admin-sa

kubectl get secrets

kubectl describe secret dashboard-admin-sa-token-XXXX

```