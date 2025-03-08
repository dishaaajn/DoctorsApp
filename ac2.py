"""create table ac(
    aid int primary key auto_increment,
    cid int,
    model varchar (256),
    brand varchar (20),
    next_service_on varchar (256),
    serviced_on datetime,
    FOREIGN KEY (cid) REFERENCES customer (cid)
);"""
import datetime
class ac:
    def __init__(self ,aid , cid , model , brand , next_service_on , serviced_on ) :
        self.aid = aid
        self.cid= cid
        self.model = model 
        self.brand = brand
        self.next_service_on = next_service_on
        self.serviced_on = datetime.datetime.now()

    def add_ac_details(self):
        self.cid = input("enter customer id :")
        self.model = input("enter ac's model :") 
        self.brand = input("enter ac's brand :") 
        self.next_service_on = input("enter ac's next service date :") 

    def show(self):

        print("==========AC==========")
        print("""
        {aid} | {cid}
        {model} | {brand}
        {next_service_on} | {serviced_on}
        """.format(self.aid , self.cid , self.model , self.brand , self.next_service_on , self.serviced_on))
        print("======================")