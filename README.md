# hackathon_containerlab
Containerlab for NANOG hackathon lab infrastructure

## Installation on Ubuntu

```bash
sudo apt install emacs-nox docker.io net-tools
bash -c "$(curl -sL https://get-clab.srlinux.dev)"
```

## Register Arista EOS Docker image
(Arista image not provided - containerized EOS lab images are available from Arista after created an account)
```bash
sudo docker import --change 'VOLUME /mnt/flash/' cEOS-lab-4.25.1F.tar ceos:4.25.1F
```

## Deploy simple two-node cEOS lab
```bash
sudo containerlab deploy --topo two_ceos.clab.yml
```
