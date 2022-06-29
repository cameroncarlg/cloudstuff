FROM kalilinux/kali-rolling

COPY *.ovpn /root
COPY ovpnstart.sh /root
COPY startvpn.sh /root

RUN apt-get update && apt-get upgrade -y

RUN DEBIAN_FRONTEND=noninteractive apt-get install -y kali-linux-headless openvpn net-tools inetutils-ping apt-utils neovim bash-completion man-db gobuster ripgrep

RUN sudo apt-get update && sudo apt-get upgrade -y

