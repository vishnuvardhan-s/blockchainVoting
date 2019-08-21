/*Access to this file : Election Head only!*/
create database VotingSystem;
use VotingSystem;
create table voters
(
    uniqueid varchar(20) unique not null,
    voterName varchar(20) not null,
    voterAadhar varchar(20) unique not null,
    voterMail varchar(50) unique not null,
    isVoted varchar(20) not null
)
insert into voters
values('blockchainvoter1', 'name1', '12345678', 'greenmatrix22@gmail.com', 'false')
insert into voters
values('blockchainvoter2', 'name2', '12348765', 'raswath5@gmail.com', 'false')
select *
from voters