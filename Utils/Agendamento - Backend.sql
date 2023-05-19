create schema clinica;

create table clinica.pessoa(

	id_pessoa bigserial,
	nm_pessoa varchar(255) not null,
	dt_nascimento timestamp not null,
	cd_cpf varchar(255) not null,
	tx_sexo varchar not null,
	nr_altura float4 not null,
	nr_peso float4 not null,
	
	constraint pessoa_pkey primary key (id_pessoa)

);


create table clinica.cliente(

	id_cliente bigserial,
	dt_criacao timestamp not null,
	dt_exclusao timestamp null,
	
	id_pessoa int4 not null,
		
	constraint cliente_pkey primary key (id_cliente),
	constraint fk_cliente_pessoa foreign key (id_pessoa) references clinica.pessoa (id_pessoa)
	
);

create table clinica.email (

	id_email bigserial,
	tx_email varchar(255) not null,
	
	id_cliente int4 not null,
		
	constraint email_pkey primary key (id_email),
	constraint fk_email_cliente foreign key (id_cliente) references clinica.cliente (id_cliente)

);

create table clinica.telefone (

	id_telefone bigserial,
	tx_telefone varchar(255) not null,
	
	id_cliente int4 not null,
	
	constraint telefone_pkey primary key (id_telefone),
	constraint fk_telefone_cliente foreign key (id_cliente) references clinica.cliente (id_cliente)

);

create table clinica.medico(

	id_medico bigserial,
	cd_crm varchar(255) not null,
	dt_criacao timestamp not null,
	dt_exclusao timestamp null,
	
	id_pessoa int4 not null,
	
	constraint medico_pkey primary key (id_medico),
	constraint fk_medico_pessoa foreign key (id_pessoa) references clinica.pessoa (id_pessoa)
	
);

create table clinica.especialidade(

	id_especialidade bigserial,
	ds_especialidade varchar(255) not null,
	
	constraint especialidade_pkey primary key (id_especialidade)
	
);

create table clinica.medico_especialidade(
	
	id_medico_especialidade bigserial,
	dt_criacao timestamp not null,
	dt_exclusao timestamp null,

	id_medico int4 not null,
	id_especialidade int4 not null,

	constraint medico_especialidade_pkey primary key (id_medico_especialidade),
	constraint fk_medico_especialidade_medico foreign key (id_medico) references clinica.medico (id_medico),
	constraint fk_medico_especialidade_especializaca foreign key (id_especialidade) references clinica.especialidade (id_especialidade)
	
);


create table clinica.agendamento(

	id_agendamento bigserial,
	nr_valor float4 not null,
	dt_abertura timestamp not null,
	dt_consulta timestamp not null,
	
	id_cliente int4 not null,
	id_medico int4 not null,
	
	constraint agendamento_pkey primary key (id_agendamento),
	constraint fk_agendamento_cliente foreign key (id_cliente) references clinica.cliente (id_cliente),
	constraint fk_agendamento_medico foreign key (id_medico) references clinica.medico (id_medico)
	
);


------------------------------------------------------------------------------------------------
		  

		  
insert into clinica.pessoa (nm_pessoa, dt_nascimento, cd_cpf, tx_sexo, nr_altura, nr_peso)
	values 	('Fernando Fábio Novaes', '1951/04/06', '58080582017', 'Masculino', 1.71, 52),
			('Catarina Evelyn Clara da Luz', '1975/01/21', '59939294727', 'Feminino', 1.53, 70),
			('Antônia Carolina Lúcia Lopes', '1981/05/07', '54093831840', 'Feminino', 1.58, 63),
	 		('Lucca Vinicius Araújo', '1943/12/18', '30991994353', 'Masculino', 1.71, 90),
	 		('Adriana Adriana Porto', '1950/04/14', '55589666295','Feminino', 1.65, 60),
	 		('Levi Carlos Eduardo Francisco', '1987/08/27', '96386746015','Masculino', 1.55, 51),
	 		('Bento Marcos Manoel Silva', '1993/06/04', '71878634895','Masculino', 1.69, 58),
	 		('Daniel Rovetta', '2000/06/12', '12345678910','Masculino', 1.73, 90),
	 		('Gabriel Dias', '1989/12/11', '14545678910','Masculino', 1.70, 90),
	 		('João Silva', '199/02/15', '12345678901', 'Masculino', 1.75, 70.5),
			('Maria Souza', '1985/08/20', '23456789012', 'Feminino', 1.68, 65.2),
			('Pedro Santos', '1992/04/10', '34567890123', 'Masculino', 1.80, 80.0),
			('Ana Oliveira', '1998/12/05', '45678901234', 'Feminino', 1.62, 55.8),
	 		('Carlos Costa', '1991/06/25', '56789012345', 'Masculino', 1.78, 72.3),
			('Lúcia Pereira', '1987/03/12', '67890123456', 'Feminino', 1.70, 68.9),
			('Rafael Mendes', '1995/09/18', '78901234567', 'Masculino', 1.85, 75.6),
			('Fernanda Almeida', '1993/07/08', '89012345678', 'Feminino', 1.63, 57.4),
			('Gustavo Ferreira', '1996/11/30', '90123456789', 'Masculino', 1.76, 71.8),
			('Mariana Castro', '1989/01/24', '01234567890', 'Feminino', 1.67, 64.1),
			('Ricardo Santos', '1997/10/05', '11122233344', 'Masculino', 1.81, 78.5),
			('Camila Lima', '1994/05/17', '22233344455', 'Feminino', 1.64, 58.7),
			('Bruno Oliveira', '1999/03/02', '33344455566', 'Masculino', 1.79, 73.2),
			('Larissa Carvalho', '1992/09/13', '44455566677', 'Feminino', 1.68, 66.5),
			('Daniel Costa', '1988/06/08', '55566677788', 'Masculino', 1.74, 69.3),
			('Isabela Rodrigues', '1995/02/20', '66677788899', 'Feminino', 1.71, 67.2),
			('Thiago Pereira', '1991/12/03', '77788899900', 'Masculino', 1.83, 76.8),
		 	('Juliana Fernandes', '1997/07/26', '88899900011', 'Feminino', 1.66, 63.9),
			('Lucas Martins', '1993/04/14', '99900011122', 'Masculino', 1.82, 74.1),
			('Amanda Sousa', '1986/11/27', '00011122233', 'Feminino', 1.69, 67.8),
			('Rodiele Cardoso', '1999/05/27', '99911122233', 'Masculino', 1.79, 89.8);
			
insert into clinica.cliente (dt_criacao, dt_exclusao, id_pessoa)
	values 	('2023/01/01', null, 11),
			('2023/01/01', null, 12),
			('2023/01/01', null, 13),
			('2023/01/01', null, 14),
			('2023/01/01', null, 15),
			('2022/01/01', null, 16),
			('2022/01/01', null, 17),
			('2022/01/01', null, 18),
			('2022/01/01', null, 19),
			('2022/01/01', null, 20),
			('2021/01/01', null, 21),
			('2021/01/01', null, 22),
			('2021/01/01', null, 23),
			('2021/01/01', '2023/03/11', 24),
			('2021/01/01', '2022/02/21', 25),
			('2019/01/01', '2021/01/05', 26),
			('2018/01/01', '2020/02/10', 27),
			('2017/01/01', '2019/03/15', 28),
			('2016/01/01', '2018/04/20', 29),
			('2015/01/01', '2017/05/30', 30);

insert into clinica.email (id_cliente, tx_email)
	values	(2, 'Pedro@droganews.com.br'),
			(2, 'Pedro@gmail.com'),
			(4, 'Carlos@imobiliariamaciel.com.br'),
			(6, 'Rafael@geometrabte.com.br'),
			(8, 'Gustavo@jci.com'),
			(8, 'Gustavo@gmail.com'),
			(11, 'Camila@email.com'),
			(12, 'Bruno@email.com'),
			(14, 'Daniel@email.com'),
			(14, 'Daniel@outlook.com'),
			(16, 'Thiago@email.com'),
			(17, 'Juliana@email.com'),
			(20, 'RodieleCardoso@email.com'),
			(20, 'Rodiele@outlook.com');
		
insert into clinica.telefone (id_cliente, tx_telefone)
	values	(1, '(94) 3519-2281'),
			(2, '(14) 4519-2281'),
			(3, '(94) 98755-8317'),
			(7, '(71) 3863-2959'),
			(8, '(15) 9999-9886'),
			(9, '(71) 98728-3421'),
			(11, '(98) 99376-0670'),
			(12, '(98) 9789-3680'),
			(13, '(43) 3774-4285'),
			(14, '(28) 99456-3149'),
			(15, '(69) 2758-1800'),
			(17, '(19) 6878-0210'),
			(17, '(17) 7898-4564'),
			(19, '(55) 4564-4560'),
			(20, '(27) 99159-9735');
		
insert into clinica.medico (dt_criacao, dt_exclusao, id_pessoa, cd_crm)
	values	('2023/01/01', null, 1, '456987123456'),
	 		('2023/02/01', null, 2, '741825369789'),
	 		('2022/01/01', null, 3, '159874236456'),
	 		('2021/01/01', null, 4, '159874236456'),
	 		('2020/02/01', null, 5, '741258933639'),
	 		('2019/03/01', null, 6, '989461335578'),
	 		('2018/04/01', '2023/01/01', 7, '986467464557'),
	 		('2017/05/01', '2022/01/01', 8, '145454643683'),
	 		('2016/06/01', '2021/01/01', 9, '789653578881'),
			('2015/07/01', '2020/01/01', 10, '456545654654');
	 	
insert into clinica.especialidade (ds_especialidade)
	values	('Neurologista'),
			('Urologista'),
			('Ortopedista'),
			('Clínico Geral'),
			('Dentista'),
			('Oftamologista'),
			('Cardiologista'),
			('Dermatologista'),
			('Psiquiatria'),
			('Radiologista');

insert into clinica.medico_especialidade (dt_criacao, dt_exclusao, id_medico, id_especialidade)
	values	('2023/01/01', null, 1, 1),
			('2023/01/01', null, 1, 3),
			('2023/01/01', null, 1, 5),
			('2023/01/01', null, 1, 7),
			('2023/02/01', null, 2, 2),
			('2023/02/01', null, 2, 4),
			('2023/02/01', null, 2, 6),
			('2023/02/01', null, 2, 8),
			('2022/01/01', null, 3, 3),
			('2022/01/01', null, 3, 6),
			('2021/01/01', null, 4, 4),
			('2021/01/01', null, 4, 8),
	 		('2020/02/01', null, 5, 5),
	 		('2018/04/01', '2023/01/01', 7 , 3),
	 		('2017/05/01', '2022/01/01', 8 , 1),
	 		('2017/05/01', '2022/01/01', 8 , 4),
	 		('2016/06/01', '2021/01/01', 9 , 9),
			('2015/07/01', '2020/01/01', 10 , 9);
		
insert into clinica.agendamento (id_cliente, id_medico, nr_valor, dt_abertura, dt_consulta)
	values	(1, 1, 200, '2023/01/05', '2023/02/05 12:00:00'),
			(2, 1, 200, '2023/02/15', '2023/03/15 12:00:00'),
			(3, 1, 200, '2023/05/15', '2023/07/05 12:00:00'),
			(4, 1, 200, '2023/05/09', '2023/06/05 12:00:00'),
			(5, 1, 200, '2023/01/05', '2023/02/05 12:00:00'),
			(6, 1, 250, '2023/02/05', '2023/04/05 10:00:00'),
			(7, 2, 250, '2023/03/05', '2023/05/05 10:00:00'),
			(8, 2, 250, '2023/04/05', '2023/06/05 12:00:00'),
			(9, 2, 250, '2023/05/05', '2023/07/05 14:00:00'),
			(10, 2, 250, '2023/05/05', '2023/07/05 12:00:00'),
			(7, 3, 300, '2022/01/05', '2022/02/05 12:00:00'),
			(8, 3, 300, '2022/02/05', '2022/03/05 10:00:00'),
			(9, 3, 300, '2022/02/05', '2022/03/05 16:00:00'),
			(10, 3, 300, '2022/02/05', '2023/03/05 8:00:00'),
			(13, 8, 200, '2021/01/05', '2021/02/05 15:00:00'),
			(18, 8, 230, '2018/06/05', '2018/06/09 12:00:00'),
			(19, 9, 200, '2017/01/05', '2017/02/05 12:00:00'),
			(20, 10, 180, '2015/03/05', '2015/04/05 12:00:00');

		
------------------------------------------------------------------------------------------------
		
