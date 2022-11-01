# rover_web_gui
## KURULUM

mkdir -p catkin_ws/src

cd catkin_ws/src

git clone https://github.com/mustafaslan0/rover_web_gui.git

cd ..

catkin_make
![Ekran Görüntüsü (11)](https://user-images.githubusercontent.com/89737685/199282842-f90d8ed0-3e5e-4819-8f4f-b25cc563f0b0.png)




# Ayarlamalar

- rover_control_website içerisindeki control.js dosyasının içerisinden ip="localhost" degerini aracın ip adresini (ifconfig) yazızınız.


### kamera ayarlama

- control.js içerisindeki cam1_node="???????" kendi kameralarınızın nodelarını giriniz
- 
   :warning: **Warning:** kameraların çalışmasın için web_video_server başlatmak gerekir.
   
   :bulb: **Tip:**  ``` sudo apt install ros-noetic-web-video-server ```
- 44-49 satırda olan (/* */ ) işaretleri silerek yorum satınını kaldırınız.


# kullanım

- Sol üst köşede yer alan pil simgesi /bat_msg  isimli topikten batarya bilgisini alır. (icon üzerine yaklaşınca batarya durumunu görebilirsiniz.) 
