CLOSE TABLES ALL 

USE \\serv_coromoto\shc\farmacia\datos\farmacos.dbf IN 0 SHARED ALIAS farmacia
USE \\serv_coromoto\shc\suministro\datos\insumos.dbf IN 0 SHARED ALIAS suministro
USE \\serv_coromoto\shc\hemodinamia\datos\insumos.dbf IN 0 SHARED ALIAS hemodinamia
USE \\serv_coromoto\shc\nutricion\datos\insumos.dbf IN 0 SHARED ALIAS nutricion


SELECT 'F'+cod_far, nom_far,'farmacia' as tipo FROM farmacia;
UNION ;
SELECT 'S'+cod_far, nom_far,'suministro' as tipo FROM  suministro;
UNION;
SELECT 'H'+cod_far, nom_far,'hemodinamia' as tipo FROM  hemodinamia;
UNION;
SELECT 'N'+cod_far, nom_far,'nutricion' as tipo FROM  nutricion;
INTO CURSOR productos