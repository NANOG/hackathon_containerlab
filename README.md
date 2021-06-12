# hackathon_containerlab
Containerlab for NANOG hackathon lab infrastructure

## Installation on Ubuntu

```bash
sudo apt install emacs-nox docker.io net-tools
bash -c "$(curl -sL https://get-clab.srlinux.dev)"
```

## Register Arista EOS Docker image
*Arista image not provided - containerized EOS lab images are available from Arista after creating an account*
```bash
sudo docker import --change 'VOLUME /mnt/flash/' cEOS-lab-4.25.1F.tar ceos:4.25.1F
```

## Register an Nokia SRL Docker image
*Nokia image and license not provided - contact your friendly Nokia rep*
```bash
sudo docker image load -i 21.3.1-410.tar.xz
```

## Deploy simple two-node lab
```bash
sudo containerlab deploy --topo two_node.clab.yml
```

## SSH tunneling
Useful for reaching your containerized devices' APIs from your laptop.

For example, if your containerized device's management interface is 172.16.0.2 and is listening on the standard https port (tcp/443), you can connect to it through a local socket tcp/8443 like this:
```bash
ssh -L 8443:172.16.0.2:443 username@containerlab_server -N
```
and then just stick https://127.0.0.1:8443 in your browser or use it to interact with the API.
