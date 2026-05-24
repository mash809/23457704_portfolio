I designed and implemented a simple threat intelligence module that checks user input against a small database of suspicious Internet Protocol addresses, domains, and phishing-related keywords. The module returns a result such as safe, suspicious, or known malicious depending on whether a match is found. This demonstrates the basic idea of threat intelligence, which is using known threat information to identify risks earlier.

The practical implementation was a Python-based checker that compares entered indicators against a predefined list of known suspicious items and then displays a warning result. For example, if the user enters a suspicious domain or Internet Protocol address, the program can flag it as malicious. If the user enters a phishing-style phrase such as “verify your account” or “urgent action required,” it can also mark it as suspicious.

This implementation helped me understand that threat intelligence is useful because it turns stored threat data into practical defensive action. However, it also has limitations, because it can only detect threats that already exist in its database. Real-world systems would need regular updates and larger data sources to remain effective.

<img width="574" height="384" alt="Screenshot 2026-05-23 232247" src="https://github.com/user-attachments/assets/862dc3a0-44b1-42f4-af91-f9888f6d0e4a" />
