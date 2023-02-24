# PROCEDURE de Insert na tabela tb_sistemas
DELIMITER //
CREATE PROCEDURE sp_insert_sistema (nome_sis VARCHAR(50), ip_sis VARCHAR(50), usu_sis VARCHAR(50), pass_sis BLOB(50))
BEGIN
	
    INSERT INTO tb_sistemas (nome_sistema, ip_sistema, usuario_sistema, senha_sistema) VALUES (nome_sis, ip_sis, usu_sis, pass_sis);
    
END //
DELIMITER ;

DROP PROCEDURE sp_insert_sistema;