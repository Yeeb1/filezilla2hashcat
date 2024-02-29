import argparse
import xml.etree.ElementTree as ET

def parse_users_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    namespaces = {'fz': 'https://filezilla-project.org'}
    
    user_info = []
    for user in root.findall(".//fz:user", namespaces):
        username = user.get('name')
        for password in user.findall(".//fz:password", namespaces):
            hash_value = password.find('fz:hash', namespaces).text if password.find('fz:hash', namespaces) is not None else "No hash found"
            salt = password.find('fz:salt', namespaces).text if password.find('fz:salt', namespaces) is not None else "No salt found"
            iterations = password.find('fz:iterations', namespaces).text if password.find('fz:iterations', namespaces) is not None else '100000'
            user_info.append((username, hash_value, salt, iterations))
    return user_info

def parse_server_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    namespaces = {'fz': 'https://filezilla-project.org'}

    admin_password = root.find(".//fz:admin_options/fz:password", namespaces)
    if admin_password:
        hash_value = admin_password.find('fz:hash', namespaces).text
        salt = admin_password.find('fz:salt', namespaces).text
        iterations = admin_password.find('fz:iterations', namespaces).text
        print(f"Admin: sha256:{iterations}:{salt}:{hash_value}")
    else:
        print("No admin password information found.")

    for user in root.findall(".//fz:users/fz:user", namespaces):
        username = user.get('name')
        password = user.find(".//fz:password", namespaces)
        if password:
            hash_value = password.find('fz:hash', namespaces).text if password.find('fz:hash', namespaces) is not None else "No hash found"
            salt = password.find('fz:salt', namespaces).text if password.find('fz:salt', namespaces) is not None else "No salt found"
            iterations = password.find('fz:iterations', namespaces).text if password.find('fz:iterations', namespaces) is not None else '100000'
            print(f"User: {username}, sha256:{iterations}:{salt}:{hash_value}")
        else:
            print(f"User: {username} has no password information")

def main():
    parser = argparse.ArgumentParser(description="Converts FileZilla hashes into a format compatible with Hashcat mode 10900 for cracking. Additionally, can parse users.xml or server.xml files to extract hashes, salts, and iterations automatically.")
    
    parser.add_argument("--salt", help="The salt", type=str)
    parser.add_argument("--hash", help="The hash value", type=str)
    parser.add_argument("--iterations", type=int, default=100000, help="Number of iterations (default: 100000)")
    parser.add_argument("--users", help="Path to the FileZilla users.xml file to parse", type=str)
    parser.add_argument("--server", help="Path to the FileZilla server.xml file to parse", type=str)

    args = parser.parse_args()

    if args.users:
        user_info = parse_users_xml(args.users)
        for username, hash_value, salt, iterations in user_info:
            print(f"User: {username}, sha256:{iterations}:{salt}:{hash_value}")
    elif args.server:
        parse_server_xml(args.server)
    elif args.salt and args.hash:
        print(f"sha256:{args.iterations}:{args.salt}:{args.hash}")
    else:
        print("Please provide either --users or --server for parsing XML files, or --salt and --hash for direct hash conversion.")

if __name__ == "__main__":
    main()
