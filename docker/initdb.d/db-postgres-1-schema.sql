-- TRAILLERPLAN authentication app - postgresql schema
drop table if exists trailerplan_schema.USER cascade;
drop schema if exists trailerplan_schema;

create schema trailerplan_schema;

create table trailerplan_schema.USER (
    ID SERIAL PRIMARY KEY,
    FIRST_NAME VARCHAR(32) not null,
    LAST_NAME VARCHAR(32) not null,
    GENDER varchar(10) null,
    EMAIL VARCHAR(255) not null,
    COUNTRY VARCHAR(32) null,

    USER_CATEGORY varchar(32) null,     --USER, GUEST, ADMIN
    ROLE_TYPE varchar(32) null,         --STANDARD, PRIVILEGED
    LOGIN_TYPE varchar(32) null,        --MAIL, MSISDN, USER_NUMBER, USER_NAME

    USERNAME VARCHAR(255) not null,
    PASSWORD VARCHAR(255) not null,

    SECRET_QUESTION varchar(255) null,
    ENCODED_SECRET_ANSWER VARCHAR(255) null,
    ENCODED_CUSTOM_SECRET_QUESTION varchar(255) null,
    ENCODED_CUSTOM_SECRET_ANSWER VARCHAR(255) null,

    IS_ACTIVE boolean default false,
    IS_STAFF boolean default false,
    IS_SUPERUSER boolean default false,
    DATE_JOINED timestamp,
    LAST_LOGIN timestamp,
    CREATED_AT timestamp,
    UPDATED_AT timestamp
);

create table trailerplan_schema.USER_GROUPS (
    user_id integer,
    group_id integer,
    permissions integer
);

create table trailerplan_schema.user_user_permissions (
    permission_id integer,
    user_id integer
);