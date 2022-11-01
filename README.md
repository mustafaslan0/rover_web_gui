# rover_web_gui
## KURULUM

mkdir -p catkin_ws/src

cd catkin_ws/src

git clone https://github.com/mustafaslan0/rover_web_gui.git

cd ..

catkin_make
![Ekran Görüntüsü (11)](https://user-images.githubusercontent.com/89737685/199282842-f90d8ed0-3e5e-4819-8f4f-b25cc563f0b0.png)




# Ayarlamalar

- rover_control_website içerisindeki control.js dosyasının içerisinden ip="localhost" degerini aracın ip adresini (ifconfig) yazızını.


-> ### kamera ayarlama

- contro.js içerisindeki cam1_node="???????" kendi kameralarınızın nodelarını giriniz
------ kameraların çalışmasın için web_video_server başlatmak gerekir.
    ### web_video_server kurulum
    
    
   :bulb: **Tip:** sudo apt install ros-noetic-web-video-server

  
