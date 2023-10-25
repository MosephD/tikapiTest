from tiktokapipy.api import TikTokAPI
import re
import pandas as pd


def do_something(tag_name):
    data = []  # Mueve la inicialización de la lista de datos dentro de la función
    # Un conjunto para llevar un registro de los correos electrónicos vistos
    seen_emails = set()
    # Una bandera para indicar si se ha encontrado un correo electrónico duplicado
    duplicate_found = False

    with TikTokAPI() as api:
        challenge = api.challenge(tag_name)
        for video in challenge.videos:
            if duplicate_found:  # Si se ha encontrado un duplicado, rompe el bucle
                break
            user = video.creator()
            nickname = user.nickname
            num_views = video.stats.play_count
            email_list = re.findall("[\w\.-]+@[\w\.-]+", user.signature)

            for email in email_list:
                if email in seen_emails:  # Si el correo electrónico ya ha sido visto, activa la bandera y rompe el bucle
                    duplicate_found = True
                    break

                # Añade el correo electrónico al conjunto de correos electrónicos vistos
                seen_emails.add(email)
                data.append({
                    'email': email,
                    'num_views': num_views,
                    'nickname': nickname

                })

    return data  # Devuelve los datos recolectados


# Llama a la función y guarda el resultado en una variable
collected_data = do_something('tj')

# Crea un DataFrame a partir de los datos recolectados
df = pd.DataFrame(collected_data)

# Elimina duplicados si es necesario (opcional)
df.drop_duplicates(subset="email", keep="first", inplace=True)

# Guarda los datos en un archivo CSV
df.to_csv('tiktokdata.csv', index=False)

print('file created')
