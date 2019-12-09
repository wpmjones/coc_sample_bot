import sqlite3

class Bot_Database:
    def __init__(self, db_filepath):
        try:
            self.conn = sqlite3.connect(db_filepath)
            self.conn.cursor().execute("PRAGMA foreign_keys = 1")  #Enables foreign keys
        except IOError as e:
            print(e)

        self.instantiate_db()

    def instantiate_db(self):
        """Method creates the database if they do not exist"""
        create_player_table = ('''\
            CREATE TABLE IF NOT EXISTS coc_players (
                coc_tag text NOT NULL,
                coc_name text NOT NULL,
                coc_th integer NOT NULL,
                PRIMARY KEY(coc_tag)

            );
            ''')
        create_donation_table = ('''\
            CREATE TABLE IF NOT EXISTS player_donation (
                update_date date NOT NULL,
                coc_tag text NOT NULL,
                coc_donation integer NOT NULL,
                PRIMARY KEY (update_date, coc_tag),
                CONSTRAINT coc_tag_ref FOREIGN KEY (coc_tag)
                REFERENCES coc_players (coc_tag)
            );
            ''')

        try:
            self.conn.cursor().execute(create_player_table)
            self.conn.cursor().execute(create_donation_table)
            self.conn.commit()
        except sqlite3.OperationalError as e:
            print(e)

    def register_user(self, tuple_data):
        """Method is used to register a user by taking a tuple of data to commit"""
        sql = ('''\
            INSERT INTO coc_players (
                coc_tag,
                coc_name,
                coc_th
            ) VALUES (?,?,?)
            ''')
        try:
            self.conn.cursor().execute(sql, tuple_data)
            self.conn.commit()
            return
        except Exception as e:
            return e

    def update_donation(self, tuple_data):
        """Method updates the donation of the registered users"""
        sql = ('''\
            INSERT INTO player_donation (
                update_date,
                coc_tag,
                coc_donation
                ) VALUES (?,?,?)
            ''')

        try:
            self.conn.cursor().execute(sql, tuple_data)
            self.conn.commit()
            return
        except Exception as e:
            return e
        
    def get_players(self):
        """Method gets all the regsitered users"""
        sql = ('''\
            SELECT coc_tag
            FROM coc_players;
            ''')
        cur = self.conn.cursor()
        cur.execute(sql)
        row = cur.fetchall()
        return row
        