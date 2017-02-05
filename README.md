#Delay simulation between multicast and unicast with zmq 

 zmq
sudo apt-get install libtool pkg-config build-essential autoconf automake
sudo apt-get install libzmq-dev

Install libsodium

git clone git://github.com/jedisct1/libsodium.git
cd libsodium
./autogen.sh
./configure && make check
sudo make install
sudo ldconfig

Install zeromq

git clone https://github.com/Undev/zeromq2-1.git
./autogen.sh
./configure && make check
sudo make install
sudo ldconfig


./configure --with-pgm=libpgm-5.1.115~dfsg

