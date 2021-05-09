CREATE TABLE incomes (
    income_id int auto_increment,
    user_id int not null,
    income_type varchar(255),
    primary key(income_id),
    foreign key(user_id) references users(user_id)
);

CREATE TABLE income_types (
    income_type varchar(255) not null,
    description 
);