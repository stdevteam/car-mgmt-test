create table if not exists car
(
	id int auto_increment
		primary key,
	created datetime(6) not null,
	modified datetime(6) not null,
	mark varchar(255) not null,
	color varchar(255) null,
	year date null,
	engine varchar(255) null,
	seats varchar(32) null,
	transmission varchar(32) not null,
	categories varchar(32) not null
);

create table if not exists customer
(
	id int auto_increment
		primary key,
	created datetime(6) not null,
	modified datetime(6) not null,
	first_name varchar(255) not null,
	last_name varchar(255) not null,
	email varchar(255) not null,
	last_booking datetime(6) null
);

create table if not exists booking
(
	id int auto_increment
		primary key,
	created datetime(6) not null,
	modified datetime(6) not null,
	date_of_hire datetime(6) not null,
	date_of_finish datetime(6) not null,
	confirmed tinyint(1) not null,
	payed tinyint(1) not null,
	car_id int not null,
	customer_id int not null,
	constraint booking_car_id_e27dd7ef_fk_car_id
		foreign key (car_id) references car (id),
	constraint booking_customer_id_6791ff7a_fk_customer_id
		foreign key (customer_id) references customer (id)
);

create table if not exists invoice
(
	id int auto_increment
		primary key,
	created datetime(6) not null,
	modified datetime(6) not null,
	status varchar(32) not null,
	price decimal(10,2) not null,
	note varchar(1024) not null,
	booking_id int null,
	constraint booking_id
		unique (booking_id),
	constraint invoice_booking_id_19b3b932_fk_booking_id
		foreign key (booking_id) references booking (id)
);
