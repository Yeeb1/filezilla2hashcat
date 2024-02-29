# filezilla2hashcat

This script converts FileZilla hashes into a format compatible with Hashcat (PBKDF2-HMAC-SHA256) for cracking. Additionally, it can parse `users.xml` or `server.xml` files to extract hashes, salts, and iterations automatically.

## Usage

### Converting Hashes

```sh
python filezilla2hashcat.py --salt [salt] --hash [hash_value] [--iterations 100000]
```

- `--salt`: The salt used in the hash.
- `--hash`: The hash value to convert.
- `--iterations`: Number of iterations (default: 100000).

### Parsing XML Files

You can also parse `users.xml` or `server.xml` files to extract hashes, salts, and iterations automatically. If no hash can be constructed, the password is likely empty.

#### Parsing `users.xml`

```sh
python3 filezilla2hashcat.py --users users.xml 
User: filemanager, sha256:100000:AdRNx7rAs1CEM23S5Zp7NyAQYHcuo2LuevU3pAXKB18:mSbrgj1R6oqMMSk4Qk1TuYTchS5r8Yk3Y5vsBgf2tF8
User: ftp, sha256:100000:No salt found:No hash found
```

#### Parsing `server.xml`

```sh
python3 filezilla2hashcat.py --users server.xml 
User: ftp, sha256:100000:No salt found:No hash found
User: filemanager, sha256:100000:AdRNx7rAs1CEM23S5Zp7NyAQYHcuo2LuevU3pAXKB18:mSbrgj1R6oqMMSk4Qk1TuYTchS5r8Yk3Y5vsBgf2tF8
```

## FileZilla Installation Log

During installation, FileZilla logs the admin user's hash and salt (actually the output of `filezilla-server-crypt`) by default into `[INSTALL_PATH]\FileZilla Server\install.log``.

```sh
python3 filezilla2hashcat.py --salt 't3jAFWk4oZRo8fiOrpzlH21/vUZ8zPHmZZMnykOLwcM' --hash 'WGha3qUR2LsM80X/w2bqpVwsf8YzDXhDAWqqssJBkRY'       
sha256:100000:t3jAFWk4oZRo8fiOrpzlH21/vUZ8zPHmZZMnykOLwcM:WGha3qUR2LsM80X/w2bqpVwsf8YzDXhDAWqqssJBkRY
```

---

*The script is for informational and educational purposes only. The author and contributors of this script are not responsible for any misuse or damage caused by this tool.* <!-- meme -->
