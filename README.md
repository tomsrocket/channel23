# channel23
Another web experiment :)

## Import old database

    docker run -p 3306:3306 --name hb-mysql-example -e MYSQL_ROOT_PASSWORD=loremPassum -d mysql

    mysql -h127.0.0.1 -uroot -ploremPassum
    
    create database blog;
    STRG+D
    
    mysql -h127.0.0.1 -uroot -pBuster blog < dbfile.sql

    
