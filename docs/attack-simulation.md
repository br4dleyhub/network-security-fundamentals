## Attack Simulation – Repeated Connections

### Description
A scripted client generated multiple rapid TCP connections to the server.

### Observation
The server logged repeated connections from the same IP within a short time window and generated suspicious activity warnings.

### Security Insight
Repeated connection attempts within a short period may indicate brute-force or scanning behavior, though false positives are possible.
