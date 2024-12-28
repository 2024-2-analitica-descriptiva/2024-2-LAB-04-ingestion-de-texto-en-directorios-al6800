import os
import pandas as pd

def process_files(base_dir='files/input', output_dir='files/output'):
    print("Iniciando el procesamiento de archivos...")
    train_data = []
    test_data = []

    # Rutas absolutas a las carpetas 'train' y 'test'
    train_folder = os.path.join(base_dir, 'train')
    test_folder = os.path.join(base_dir, 'test')

    # Verificación de la existencia de las carpetas
    if not os.path.exists(train_folder):
        print(f"La carpeta 'train' no existe en la ruta: {train_folder}")
        return

    if not os.path.exists(test_folder):
        print(f"La carpeta 'test' no existe en la ruta: {test_folder}")
        return

    # Procesamos la carpeta train
    for sentiment in ['positive', 'negative', 'neutral']:
        sentiment_folder = os.path.join(train_folder, sentiment)
        if not os.path.exists(sentiment_folder):
            continue
        for filename in os.listdir(sentiment_folder):
            if filename.endswith('.txt'):
                file_path = os.path.join(sentiment_folder, filename)
                with open(file_path, 'r', encoding='utf-8') as file:
                    phrase = file.read().strip()
                    if phrase:  # Si hay texto en el archivo
                        train_data.append({'phrase': phrase, 'target': sentiment})

    # Procesamos la carpeta test
    for sentiment in ['positive', 'negative', 'neutral']:
        sentiment_folder = os.path.join(test_folder, sentiment)
        if not os.path.exists(sentiment_folder):
            continue
        for filename in os.listdir(sentiment_folder):
            if filename.endswith('.txt'):
                file_path = os.path.join(sentiment_folder, filename)
                with open(file_path, 'r', encoding='utf-8') as file:
                    phrase = file.read().strip()
                    if phrase:  # Si hay texto en el archivo
                        test_data.append({'phrase': phrase, 'target': sentiment})

    # Crear los DataFrames y guardar como CSV si hay datos
    if train_data:
        train_df = pd.DataFrame(train_data)
        os.makedirs(output_dir, exist_ok=True)
        train_df.to_csv(os.path.join(output_dir, 'train_dataset.csv'), index=False)
        print("train_dataset.csv creado.")
    else:
        print("No se encontraron datos para 'train'.")

    if test_data:
        test_df = pd.DataFrame(test_data)
        test_df.to_csv(os.path.join(output_dir, 'test_dataset.csv'), index=False)
        print("test_dataset.csv creado.")
    else:
        print("No se encontraron datos para 'test'.")

def pregunta_01():
    """
    Función principal que procesa los archivos y genera los archivos CSV.
    """
    process_files()

if __name__ == "__main__":
    pregunta_01()
