CREATE DATABASE IF NOT EXISTS db_password CHARSET utf8mb4 COLLATE utf8mb4_general_ci;

CREATE TABLE IF NOT EXISTS tb_usuarios (
	id_usuario INT(11) AUTO_INCREMENT,
    nome_usuario VARCHAR(50) NOT NULL,
    senha_usuario BLOB(50) NOT NULL,
    tipo_usuario ENUM('Administrador', 'Usuário') NOT NULL,
PRIMARY KEY (id_usuario)
)AUTO_INCREMENT = 1;

CREATE TABLE IF NOT EXISTS tb_sistemas (
	id_sistema INT(11) AUTO_INCREMENT,
    nome_sistema VARCHAR(50) NOT NULL,
    ip_sistema VARCHAR(50) NOT NULL,
    usuario_sistema VARCHAR(50) NOT NULL,
    senha_sistema BLOB NOT NULL,
    id_tipo_sistema INT(11) NOT NULL,
PRIMARY KEY (id_sistema),
CONSTRAINT fk_id_tipo_sistema FOREIGN KEY(id_tipo_sistema) REFERENCES tb_tipo_sistema (id_tipo_sistema)
)AUTO_INCREMENT = 1;

CREATE TABLE IF NOT EXISTS tb_tipo_sistema (
	id_tipo_sistema INT(11) AUTO_INCREMENT,
    nome_tipo_sistema VARCHAR(50) NOT NULL,
PRIMARY KEY (id_tipo_sistema)
);

CREATE TABLE IF NOT EXISTS tb_logs (
	id_log INT(11) AUTO_INCREMENT,
    descricao_log VARCHAR(255) NOT NULL,
PRIMARY KEY (id_log)
);
