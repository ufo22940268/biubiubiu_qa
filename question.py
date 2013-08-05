from db_util import *

def add_question(q):
    conn = get_db();
    c = conn.cursor();
    c.execute("insert into questions(title, content) values(?, ?)",
            (q["title"], q["content"]));
    rid = c.lastrowid;
    conn.commit();
    #add_tags(rid, q["tags"]);
    c.close();
    conn.close()
    
#def add_tags(rid, tags):
    #conn = get_db();
    #c = conn.cursor();
    #c.execute("insert into ");
    
    #conn.commit();
    #c.close();
    #conn.close()
    
def get_questions():
    conn = get_db();
    c = conn.cursor();
    c.execute("select * from questions");
    all = c.fetchall();
    c.close();
    conn.close()
    return all;
