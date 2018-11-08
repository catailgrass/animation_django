from utils.db_controller import *


# animation curd
def get_all_animation():
    db = get_local_sqlite3_db()
    cursor = db.cursor()
    sql = '''
        select an.*,img.img_location,img.content,img.path from animation_info an left join animation_image img
        where an.an_id = img.an_id
    '''
    try:
        cursor.execute(sql)
        values = cursor.fetchall()
        return values
    except Exception as e:
        print(e)


if __name__ == '__main__':
    values = get_all_animation()
    for row in values:
        print(row)
