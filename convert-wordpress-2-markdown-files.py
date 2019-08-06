import mysql.connector
import sys
from datetime import datetime
from slugify import slugify

if len(sys.argv) < 2:
    print("MISSING mysql pw as first argument")
    exit()    
mysqlPw = str(sys.argv[1])


mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password=mysqlPw,
    database='blog',
)

print(mydb) 



mycursor = mydb.cursor(dictionary=True)
mycursor.execute("""
    SELECT wp_posts.*, wp_users.display_name 
    FROM wp_posts 
    LEFT join wp_users on wp_users.ID = wp_posts.post_author 
    WHERE post_type='post' AND post_status='publish' 
    """)
myresult = mycursor.fetchall()

tagcursor = mydb.cursor(dictionary=True)



for x in myresult:

    filename = slugify(x['post_title'], to_lower=True)
    if not (x['post_title'] and filename):
        continue

    f = open("blog/source/_posts/" + filename + ".md", "w")

    f.write("---"
        + "\ntitle: \"" + x['post_title'].replace('"', "'") + '"'
        + "\ndate: " + x['post_date'].date().isoformat()
        + "\nauthor: " + x['display_name']
        + "\ncategories:")

    tagcursor.execute("""
        select * 
        from wp_term_relationships 
        left join wp_terms on wp_terms.term_id = wp_term_relationships.term_taxonomy_id 
        left join wp_term_taxonomy on wp_term_taxonomy.term_id = wp_terms.term_id
        where taxonomy='category' 
        AND object_id = """ + str(x['ID'])
        )
    tagresult = tagcursor.fetchall();
    
    for tag in tagresult:
        f.write("\n- [\"" + tag['name'].lower() + '"]')

    f.write("\ntags:")

    tagcursor.execute("""
        select * 
        from wp_term_relationships 
        left join wp_terms on wp_terms.term_id = wp_term_relationships.term_taxonomy_id 
        left join wp_term_taxonomy on wp_term_taxonomy.term_id = wp_terms.term_id
        where taxonomy='post_tag' 
        AND object_id = """ + str(x['ID'])
        )
    tagresult = tagcursor.fetchall();
    
    for tag in tagresult:
        f.write("\n- [\"" + tag['name'].lower() + '"]')

    f.write("\n---\n")
    f.write(x['post_content'])
    print(filename)
    

    f.close()

#tags:
#- Injury
#- Fight
#- Shocking
#---