create database YL_comentarios;
use YL_comentarios;

create table tb_comentarios(
	com_id int auto_increment primary key,
    com_text varchar(250) not null
);