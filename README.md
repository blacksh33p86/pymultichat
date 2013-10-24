pyChatServ pre-alpha

********************************ToDo***********************************

- [x] connect from Client
- [x] Send Msgs to all Users via "/send" command
- [*] Login and nicknaming, including guests
- [*] clean logout
- [ ] multiple channels at the same time
- [ ] privilege system (e.g. create channel, delete channel, kick/ban user)
- [ ] temp channel
- [x] logging system

- [ ] HTML5 client

***************************issues to be solved*************************

- [ ] infinite loop on some ways of clientside connection shutdown
      comment: "'!exited clientSockClose'" queued multiple times

***************************future ideas********************************

- [ ] multiple channels for clients
- [ ] private chat system
- [ ] colors and emoticons
- [ ] avatars for registered users
- [ ] moderator bot
- [ ] gaming channels (e.g. quiz)
- [ ] webcam support for private chat

to be continued ...

***************************fixes and updates***************************

- [2013-10-24] - onlinestatus for registered users
- [2013-10-24] - basic activity logging in database
- [2013-10-23] - basic logout for users
- [2013-10-23] - basic login for registered users
- [2013-10-23] - basic database structure for mysql
- [2013-10-23] - clean logout on clientside connection "abort"