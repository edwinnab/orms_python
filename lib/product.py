'''
class is mapped to the table 
python program ensures connectivity to the database
object attributes mapped to the table columns
class instances make up the table rows 

#implement methods  to work with the data
0. create the table - classmethod 
1. fetch all the data from the db
2. convert the raw data to python objects 

'''
from config import DB_CONN, DB_CURSOR

class Product:
    data = []
    
    def __init__(self, name, price, description):
        self.id = None
        self.name = name
        self.price  = price
        self.description = description
        
    # def __repr__(self):
    #     return f"{self.name}" \
    #         + f"{self.price}" \
    #             + f"{self.description}"
    
    #convert the records to an object
    @classmethod
    def record_from_db(cls, row):
        product = cls(
            name = row[1],
            price = row[2],
            description = row[3],
        )
        product.id = row[0]
        return product.__dict__
        
        
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE products
        """
        DB_CURSOR.execute(sql)
        DB_CONN.commit()
        
    @classmethod
    def clear_table(cls):
        sql = """
            DELETE FROM products 
        """
        DB_CURSOR.execute(sql)
        DB_CONN.commit()
        
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE products (
                id INTEGER PRIMARY KEY,
                name TEXT,
                price INTEGER,
                description TEXT
            )
        """
        DB_CURSOR.execute(sql)
        DB_CONN.commit()
        
    #class method to create the instances 
    @classmethod
    def create(cls,name, price,description):
        product = Product(name, price, description)
        product.save()
        
    # save method to add data to the db
    def save(self):
        sql = """
            INSERT INTO products(name, price, description)
            VALUES(?,?,?)
        """
        DB_CURSOR.execute(sql, (self.name, self.price, self.description))
        DB_CONN.commit()
        
    # fetches from the db
    @classmethod
    def get_all(cls):
        sql = """
            SELECT * FROM products
        """
        data = DB_CURSOR.execute(sql).fetchall()
        return data
    
    #find_by_name 
    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT * FROM products 
            WHERE name = ?
        """
        records = DB_CURSOR.execute(sql, (name,)).fetchall()
        record = [cls.record_from_db(row) for row in records]
        if record:
            return record
        else:
            return "Record doed not exist!!"
        
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT * FROM products 
            WHERE id = ?
        """
        product =  DB_CURSOR.execute(sql, (id,)).fetchone()
        return cls.record_from_db(product)
            
            
        
        
        