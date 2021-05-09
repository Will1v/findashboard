DROP TABLE IF EXISTS family_users;
DROP TABLE  IF EXISTS users;
DROP TABLE  IF EXISTS families;

CREATE TABLE users (
    user_id int auto_increment,
    login varchar(255) not null,
    password varchar(255),
    date_of_birth date,
    primary key(user_id)
);

CREATE TABLE families (
    family_id int auto_increment,
    family_name varchar(255) not null,
    primary key(family_id)
);

CREATE TABLE family_users (
    user_id int not null,
    family_id int not null,
    dependant boolean default false,
    primary key(user_id, family_id),
    foreign key(user_id) references users(user_id),
    foreign key(family_id) references families(family_id)
);

CREATE TABLE accounts (
    account_id int not null,
    primary key(account_id)
);

CREATE TABLE user_accounts (
    user_id int not null,
    account_id int not null,
    stake_pct decimal(5, 2) default 100.00,

);