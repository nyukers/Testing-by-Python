import sqlite3
from sqlite3 import Error
import datetime

def read_contact_txt_gui_list(file_name):
    # Открытие файла для чтения данных.
    file_txt_r = open(file_name, 'r') 
    # Переменная для хранения списка контактов.
    data_list_all = []
    # Бесконечный цикл для обработки контактов построчно.
    while True: 
        # Получение строки с контактом из txt-файла.
        data_str = file_txt_r.readline()
        # Если строка пустая, то выход из цикла. 
        if data_str == '': 
            file_txt_r.close() # Закрытие текстового файла.
            break # Выход из цикла.
        # С каждым проходом цикла в список добавляется контакт.
        data_list_all.append(data_str)
    # Функция возвращает список контактов.   
    return data_list_all 

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def create_project(conn, project):
    sql = ''' INSERT INTO contact_data(timewrite,lastname,firstname,address,\
                  phonenumber, email, addinform, dt, d, url_photo, img)\
                  VALUES(?,?,?,?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()
    return cur.lastrowid

def write_contacts(data_list_all):
    database = r"db.sqlite3"
    # create a database connection
    conn = create_connection(database)
    with conn:
        for data_str in data_list_all:
            data_list = data_str.split('&')
        # Получение времени записи в БД.
            timewrite = datetime.datetime.now()
        # Получение фамилии.
            lastname = data_list[0]
        # Получение имени.       
            firstname = data_list[1]
        # Получение адреса.        
            address = data_list[2]
        # Получение номера телефона.         
            phonenumber = data_list[3]
        # Получение электронного адреса.    
            email = data_list[4] 
        # Получение дополнительной информации.          
            addinform = data_list[5]
        # Получение даты и времени записи контакта.
            dt = data_list[6]
        # Получение даты создания контакта.              
            d = dt.split(' ')[0] 
        # Получение URL (ссылки) на фотографию контакта.        
            url_photo = lastname + d
        # Получение URL (ссылки) на фотографию контакта через upload_to.        
            img = 'image/' +lastname + d + '.png'
	    # Из полученных элементов контакта формирую кортеж. 
        # Кортежем также называется строка в таблице БД.
            project = (timewrite, lastname, firstname, address, phonenumber, email, addinform, dt, d, url_photo, img)
            project_id = create_project(conn, project)
#    cur.close()  # Закрываю курсор.
    conn.close() # Закрываю соединение с БД.

def main():
    write_contacts(read_contact_txt_gui_list('contact.txt'))
       
		
if __name__ == '__main__':
    main()