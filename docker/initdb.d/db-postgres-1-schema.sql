-- TRAILLERPLAN authentication app - postgresql schema
drop table if exists trailerplan_schema.USER cascade;
drop schema if exists trailerplan_schema;

create schema trailerplan_schema;

create table trailerplan_schema.USER (
    ID SERIAL PRIMARY KEY,

    CIVILITY varchar(32) not null,
    FIRST_NAME VARCHAR(32) not null,
    LAST_NAME VARCHAR(32) not null,
    GENDER varchar(10) not null,
    BIRTHDAY date null,
    MAIL VARCHAR(255) not null,
    CITY VARCHAR(32) null,
    COUNTRY VARCHAR(32) not null,
    PHONE VARCHAR(32) null,

    USER_CATEGORY varchar(32) null,     --USER, GUEST, ADMIN
    ROLE_TYPE varchar(32) null,         --STANDARD, PRIVILEGED
    LOGIN_TYPE varchar(32) null,        --MAIL, MSISDN, USER_NUMBER, USER_NAME
    USER_NAME varchar(255) null,
    ENCODED_PASSWORD VARCHAR(255) null,

    SECRET_QUESTION varchar(255) null,
    ENCODED_SECRET_ANSWER VARCHAR(255) null,
    ENCODED_CUSTOM_SECRET_QUESTION varchar(255) null,
    ENCODED_CUSTOM_SECRET_ANSWER VARCHAR(255) null
);
