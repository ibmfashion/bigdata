./configure \
    --prefix=/usr/local/php \
    --exec-prefix=/usr/local/php \
    --bindir=/usr/local/php/bin \
    --sbindir=/usr/local/php/sbin \
    --includedir=/usr/local/php/include \
    --libdir=/usr/local/php/lib/php \
    --mandir=/usr/local/php/php/man \
    --with-config-file-path=/usr/local/php/etc \
    --with-mysql-sock=/var/lib/mysql/mysql.sock \
    --with-mhash \
    --with-openssl \
    --with-mysqli=shared,mysqlnd \
    --with-pdo-mysql=shared,mysqlnd \
    --with-gd \
    --with-jpeg-dir \
    --with-png-dir \
    --with-iconv \
    --with-zlib \
    --enable-zip \
    --enable-inline-optimization \
    --disable-debug \
    --disable-rpath \
    --enable-shared \
    --enable-xml \
    --enable-bcmath \
    --enable-shmop \
    --enable-sysvsem \
    --enable-mbregex \
    --enable-mbstring \
    --enable-ftp \
    --enable-pcntl \
    --enable-sockets \
    --with-xmlrpc \
    --enable-soap \
    --without-pear \
    --with-gettext \
    --enable-session \
    --with-curl \
    --with-freetype-dir \
    --enable-opcache \
    --enable-fpm \
    --with-fpm-user=nginx \
    --with-fpm-group=nginx \
    --without-gdbm \
    --enable-fileinfo \
    --with-apxs2=/usr/bin/apxs

    --disable-fileinfo
    
    
    云社区 博客 博客详情
    “化鲲为鹏，我有话说”基于鲲鹏搭建网站环境amh面板篇 https://bbs.huaweicloud.com/blogs/127585
    云社区 博客 博客详情
    “化鲲为鹏，我有话说”基于鲲鹏搭建网站环境wdcp面板篇 https://bbs.huaweicloud.com/blogs/127586
    
centos 6 系统 
    echo '12345' > /www/server/panel/data/port.pl && /etc/init.d/bt restart
    iptables -I INPUT -p tcp -m state --state NEW -m tcp --dport 12345 -j ACCEPT
    service iptables save
    centos 7 系统 
    echo '12345' > /www/server/panel/data/port.pl && /etc/init.d/bt restart
    firewall-cmd --permanent --zone=public --add-port=12345/tcp
    firewall-cmd --reload
    以上代码将BT宝塔面板的端口改成了12345，注意：需要使用root用户来改。
    ————————————————
    版权声明：本文为CSDN博主「Api - 小柒」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
    原文链接：https://blog.csdn.net/qq15577969/java/article/details/103081789
