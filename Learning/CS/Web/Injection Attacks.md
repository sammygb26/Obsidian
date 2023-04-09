These attacks take place taking over the **server**. In general this allows us to inject code that the machine interprets. The original plan was for the program to not run any attack. This happens for many languages like SQL, NoSQL, OS and LDAP. 

##### Key Steps
1) Attacker provides malicious input
2) Server accept input without validating it first
3) Server run's attacker's arbitrary code

- [[Buffer Overruns]] are an example of injection attacks.

### Command Injection
Command injection attacks take place when a user can send command through their input channel. These will be interpreted by a shell on the host computer. This is caused when *data and code* share the same channel.

##### Simple Example
A simple example takes the code

![[Pasted image 20230406152758.png]]

Here a user can control the domain field and so we control part of the shell. This way we can send a field that isn't a domain.

![[Pasted image 20230406153321.png]]

This was cuased by poor input validation for example ; should have been checked for. Another problem is the **system** function is very powerful. For example **execv** could have been used instead. This goes against secure program validation.

### Defense: Input Escaping
To solve this we can pass the input through **escapeshellarg()** which adds quotes around the argument and escapes all quotes to prevent escape.

![[Pasted image 20230406153914.png]]

This prevents the argument from being interpreted wrong

### SQL Injection
Here DBs often contain confidential information and are frequently the **target of attacks**.

![[Pasted image 20230406154142.png]]

These allow efficient scalable access to user information. These are critical as all user information is often stored here. In general the flow goes as:

1. Web server sends **queries** or **commands** according to incoming HTTP requests
2. DB server returns associated values
3. DB server can **modify/update** records based on requests.

### Databases
A database is a system that stores information in an organizes way and produces report about the information based in queries.

![[Pasted image 20230406154747.png]]

These table based databases are called **relational databases**. SQL is a language that allows you to query and modify the database. For example 

![[Pasted image 20230406155038.png]]

We may also return certain values. If we want to get a users password we might have

![[Pasted image 20230406155114.png]]

We also have INSERT to allow addition of records. For example

![[Pasted image 20230406155246.png]]

Some other commands are UPDATE to change a record. Or we may want to delete a record with DELETE. We can also remove an entire table with DROP TABEL. 

Similar to commands in a shell we can use semicolons to separate commands.

![[Pasted image 20230406155454.png]]


##### Simple Example
The web serve logs in a user if the user exits with the given username and password.

![[Pasted image 20230406155554.png]]

Similar to command injection we can escape from the script and input our own command.

![[Pasted image 20230406160322.png]]

This will escape and comment our the rest. This just removes the password check in the SQL query. But we can do **anything** for example returning 

![[Pasted image 20230406160458.png]]

We may be able to return the query depending on the logic of the webserver.

##### Defense
SQL injections vulnerabilities are the result of programmers failing to sanities user input before using that input to construct database queries. For example PHP provides **mysql_real_escape_string** to escape special characters. For example appending \ to special characters. \x00, \n, \r, \, " and \x1a.

![[Pasted image 20230406161300.png]]

Another solution is **prepared statements**. Here the query and the data are sent to the server separately.  This speeds up use. Then later SQL is send later. This ensures untrusted value are not interpreted as a command.

![[Pasted image 20230406161454.png]]

