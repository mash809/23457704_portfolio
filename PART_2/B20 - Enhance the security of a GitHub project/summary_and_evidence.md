I enhanced the security of a GitHub project by improving how passwords are handled in the application. Instead of storing passwords in plain text, I used Werkzeug’s security module to implement secure password hashing and password verification. The solution uses generate_password_hash() to hash passwords with a salt and a strong hashing method, and check_password_hash() to verify passwords safely during login.

This improvement makes the project more secure because user passwords are no longer stored in a readable form. Even if the database is exposed, the original passwords are much harder to recover. Overall, this enhancement improves authentication security and follows better password-handling practices in real-world software development.

I have added the link to the repository (password hashing file is in the app folder) along with the code

https://github.com/qwertytops/AudioAnalyser.git






