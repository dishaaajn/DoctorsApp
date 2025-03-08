"""
create table customer(
    cid int primary key auto_increment,
    name varchar(256), 
    phone varchar(15), 
    email varchar(256), 
    age int,
    gender varchar(10)
);
    
student = first_name , last_name , age , course , class , gender , club 


create table student(
    sid int primary key auto_increment,
    first_name varchar(256) , 
    last_name varchar(256), 
    age int, 
    course varchar(20), 
    classrm varchar(20), 
    gender varchar(10), 
    club varchar(50)
);

insert into customer values(null, 'john' , '+91 2222255555' , 'john@gmail.com' , 20 , 'male')

insert into student values(null ,'arsh' , 'jindal' , 23 , 'bcom' , 'a' , 'male' , 'business');
"""


class customer:
    def __init__(self , name , phone , email , age , gender):
        self.name = name
        self.phone = phone
        self.email = email
        self.age = age
        self.gender = gender


class student:
    def __init__(self , first_name , last_name , age , course , classrm , gender , club):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.course = course 
        self.classrm = classrm  
        self.gender = gender  
        self.club = club  