# default local execution by reference
class Number:
    value = 0
    
i = Number()

def increment(a,b):
    a.value += 1
    b.value += 1
    
increment(i,i)

i.value


# simulate an RPC implementation with copy in / copy out semantics
i = Number()

def increment_client_stub(a,b):
    request_message = (a.value, b.value)
    reply = increment_server_stub(request_message)  # copy in
    a.value = reply[0]  # copy out
    b.value = reply[1]  # copy out
    
    
def increment_server_stub(message):
    a = Number()
    b = Number()
    a.value = message[0]
    b.value = message[1]
    increment(a,b)
    return (a.value,b.value)


increment_client_stub(i, i)

i.value



