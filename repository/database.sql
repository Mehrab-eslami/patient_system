create database patient_db;



create table patient_db.persons
(
    p_id       int primary key auto_increment,
    name       varchar(30),
    family     varchar(30),
    birth_date date,
    username   varchar(30),
    password   varchar(20)
);

create table patient_db.information
(
    in_id           int primary key auto_increment,
    doctor          varchar(30),
    visit_date_time date,
    hospital        varchar(30),
    prescription    varchar(30),
    extra_data      varchar(30)


);

create table patient_db.prescription
(
    id          int primary key auto_increment,
    date_time   date,
    doctor      varchar(30),
    drug        varchar(30),
    dosage      int,
    description varchar(30)


)