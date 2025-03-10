from fabric import Connection

# List of servers with SSH credentials
servers = [
    {"host": "192.168.6.14", "user": "admin", "password": "pass"},
    {"host": "192.168.2.13", "user": "admin", "password": "pass"}
]

def run_command_on_servers(command):
    for server in servers:
        try:
            conn = Connection(
                host=server["host"], 
                user=server["user"], 
                connect_kwargs={"password": server["password"]}
            )
            result = conn.run(command, hide=True)
            print(f"✔ {server['host']}: {result.stdout.strip()}")
        except Exception as e:
            print(f"❌ {server['host']}: {e}")

# Run a command on all servers
run_command_on_servers("ifconfig")
