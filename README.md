# rover_web_gui
## KURULUM
```
mkdir -p catkin_ws/src

cd catkin_ws/src

git clone https://github.com/mustafaslan0/rover_web_gui.git

cd ..

catkin_make
```



![Ekran Görüntüsü (11)](https://user-images.githubusercontent.com/89737685/199282842-f90d8ed0-3e5e-4819-8f4f-b25cc563f0b0.png)




# Ayarlamalar

- rover_control_website içerisindeki control.js dosyasının içerisinden ip="localhost" degerini aracın ip adresini (ifconfig) yazızınız.


### kamera ayarlama

- control.js içerisindeki cam1_node="???????" kendi kameralarınızın nodelarını giriniz
- 
   :warning: **Warning:** kameraların çalışmasın için web_video_server başlatmak gerekir. ``` rosrun web_video_server web_video_server ```
   
   :bulb: **Tip:**  ``` sudo apt install ros-noetic-web-video-server ```
- 44-49 satırda olan (/* */ ) işaretleri silerek yorum satınını kaldırınız.







# kullanım

- Araç kontrolü için ```/cmd_vel``` ile data göndermektedir.

- Sol üst köşede yer alan pil simgesi ``` /bat_msg ``` isimli topikten batarya bilgisini alır. (icon üzerine yaklaşınca batarya durumunu görebilirsiniz.)

- Sağ alt köşede bulunan iki icon ise araç ve joystick bağlantılarının durumunu göstermektedir. Ayrıca herhangi bir bağlantı kesilmesinde bildirim gelmektedir.

- Sol taraftaki kamera görüntülerine tıklayarak kameraları tam ekran olarak görüntülenebilmektedir.


#v2 updates




![Screenshot_20221103_021826](https://user-images.githubusercontent.com/89737685/199620384-82b953a1-c633-4070-a7db-a3eb68e9fd63.png)








