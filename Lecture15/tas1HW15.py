'''
1. Используя тестовую БД sqlite „chinook.db“ определите:
1) Сколько всего байт «занимают» песни из таблицы tracks
2) Сколько записей находится в таблицах employees и customers
3) Получить список треков tracks из альбома «A-Sides»
4) Используя группировку (https://www.w3schools.com/sql/sql_groupby.asp) определите общую стоимость треков в каждом альбоме
'''

#1 
# SELECT SUM(Bytes) FROM tracks;
# (117386255350)

#2 
# SELECT sum(total_sum) FROM(
# 	SELECT count(*)as total_sum FROM customers 
# 	UNION
# 	SELECT count(*) FROM employees);

#3
# SELECT name FROM tracks WHERE Albumid = (
# 	SELECT Albumid FROM albums WHERE Title = "A-Sides");

#4
# SELECT Title as name, albumPrice as Price
# FROM albums
# INNER JOIN (SELECT SUM(UnitPrice) as albumPrice, Albumid FROM tracks);
#
# SELECT Title as Name, albumPrice as Price
# FROM albums
# INNER JOIN (
# 	SELECT SUM(UnitPrice) as albumPrice, Albumid
# 	FROM tracks
# 	GROUP BY Albumid
# 	)
# USING (Albumid)
#
#
#
#SELECT Name, albumPrice 
# FROM tracks
# INNER JOIN (SELECT SUM (UnitPrice) as albumPrice, 
# Albumid FROM tracks);
#
# Вроде как раотают оба, но второй варик старнно выводит данные 