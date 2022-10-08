drop table users;

create table users
(
    id            varchar(100) not null,
    name          varchar(100) not null,
    address       varchar(100) not null,
    date          varchar(100) not null,
    account       varchar(100) not null,
    type          varchar(100) not null,
    description   varchar(100) not null,
    coin          varchar(100) not null,
    coin_quantity varchar(100) not null,
    coin_usd      varchar(100) not null,
    constraint users_pk
        primary key (id)
);

create index users_name_date_index
    on users (name, date);

