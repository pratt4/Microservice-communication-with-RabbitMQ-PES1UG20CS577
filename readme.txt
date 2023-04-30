ipconfig
1)mysql server create by typing (inside any connection)--->
Create user 'root'@'%' identified by 'password';
grant all privileges on *.* to 'root'@'%' with grant option;
flush privileges;
2)new test connection hostname-->ip address of ur laptop-->password whatever u typed above.
3)create database names student_records;
3.1)CREATE TABLE STUDENTS_INFO(name VARCHAR(50), SRN VARCHAR(15), section VARCHAR(1)); 

4)in vs code file(change ip address to your ip address)

5)open cmd to run rabbitmq-->docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management
6)open cmd and -->docker compose up

7)postman desktop
8)while sending health check dont use space in msge.

9)follow everything in pdf
--------------------------------------------------------
TO RUN WITH NO ERRORS:
1)open docker
2)cmd in folder-->docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management
3)new cmd-->docker compose up
4)psotman desktop







http://localhost:5000/health_check?message=heyyoualive?