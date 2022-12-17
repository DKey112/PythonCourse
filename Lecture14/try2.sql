PRAGMA foreing_key = on;
CREATE TABLE "users" (
	"Id"	INTEGER PRIMARY KEY,
	"First_name"	TEXT,
	"Last_name"	TEXT,
	"gender"	TEXT,
	"login"	TEXT,
	"email"	TEXT,
	"date_register"	TEXT
);

CREATE TABLE "category" (
	"category_id"	INTEGER PRIMARY KEY,
	"category_title"	TEXT
);

CREATE TABLE post(
id INTEGER,
title TEXT NOT NULL,
date_create INTEGER,
content VARCHAR(140),
post_author_id INTEGER,
post_category_id INTEGER,
FOREIGN KEY("id") REFERENCES "category"("category_id") ON DELETE SET NULL,
FOREIGN KEY("post_author_id")REFERENCES "users"("Id") ON DELETE CASCADE
);