# channel23
Another web experiment :)

Convert an old wordpress blog into single markdown files per blog post so they can be used with a static site generator like Hugo.

## Import old database

Run mysql daemon with docker so we dont have to install mysqld on the system:

    docker run -p 3306:3306 --name hb-mysql-example -e MYSQL_ROOT_PASSWORD=loremPassum -d mysql

    mysql -h127.0.0.1 -uroot -ploremPassum
    
    create database blog;
    STRG+D
    
    mysql -h127.0.0.1 -uroot -pBuster blog < dbfile.sql
    
    desc wp_posts;

## Convert wordpress content to markdown files

    python3 -m pip install mysql-connector-python
    python3 -m pip install awesome-slugify

    python3 convert-wordpress-2-markdown-files.py loremPassum

### Wordpress blog post database structure

desc wp_posts;

    +-----------------------+---------------------+------+-----+---------------------+----------------+
    | Field                 | Type                | Null | Key | Default             | Extra          |
    +-----------------------+---------------------+------+-----+---------------------+----------------+
    | ID                    | bigint(20) unsigned | NO   | PRI | NULL                | auto_increment |
    | post_author           | bigint(20) unsigned | NO   | MUL | 0                   |                |
    | post_date             | datetime            | NO   |     | 0000-00-00 00:00:00 |                |
    | post_date_gmt         | datetime            | NO   |     | 0000-00-00 00:00:00 |                |
    | post_content          | longtext            | NO   |     | NULL                |                |
    | post_title            | text                | NO   |     | NULL                |                |
    | post_category         | int(4)              | NO   |     | 0                   |                |
    | post_excerpt          | text                | NO   |     | NULL                |                |
    | post_status           | varchar(20)         | NO   |     | publish             |                |
    | comment_status        | varchar(20)         | NO   |     | open                |                |
    | ping_status           | varchar(20)         | NO   |     | open                |                |
    | post_password         | varchar(20)         | NO   |     |                     |                |
    | post_name             | varchar(200)        | NO   | MUL |                     |                |
    | to_ping               | text                | NO   |     | NULL                |                |
    | pinged                | text                | NO   |     | NULL                |                |
    | post_modified         | datetime            | NO   |     | 0000-00-00 00:00:00 |                |
    | post_modified_gmt     | datetime            | NO   |     | 0000-00-00 00:00:00 |                |
    | post_content_filtered | text                | NO   |     | NULL                |                |
    | post_parent           | bigint(20) unsigned | NO   | MUL | 0                   |                |
    | guid                  | varchar(255)        | NO   |     |                     |                |
    | menu_order            | int(11)             | NO   |     | 0                   |                |
    | post_type             | varchar(20)         | NO   | MUL | post                |                |
    | post_mime_type        | varchar(100)        | NO   |     |                     |                |
    | comment_count         | bigint(20)          | NO   |     | 0                   |                |
    +-----------------------+---------------------+------+-----+---------------------+----------------+

## Run hexo in dev mode

    npm run serve

Beware: This will NOT generate tag- or category-pages.. To test them you need to generate the real thing

## Deploy to production

    npm run generate

This will build all the files and write them to the "public" dir. 

Tar it with 

    tar -czvf blog.tgz public 
    
 Then upload it to server and unzip.   
    
