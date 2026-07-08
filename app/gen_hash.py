from passlib.context import CryptContext

# Configuramos el contexto de seguridad
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Generamos el hash
## its gonna be your password in plain text, you can change it to whatever you want
password_plano = "Fifa-2013"
password_hasheado = pwd_context.hash(password_plano)

print("\n" + "="*50)
print("COPIA ESTE HASH PARA TU SQL:")
print("="*50)
print(password_hasheado)
print("="*50 + "\n")