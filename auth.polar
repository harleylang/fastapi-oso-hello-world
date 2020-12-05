allow(actor: User, "read", content: User) if 
    actor.username = content.username or
    actor.role = "mib"; 

allow(actor: User, "read", content: Message) if 
    actor.username = content.sent_from or
    actor.username = content.sent_to or
    actor.role = "mib"; 
