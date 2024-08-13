from setuptools import setup, find_packages

setup(
    name="pygame_alglin",  # Nome do pacote
    version="0.1.0",  # Versão do pacote
    packages=find_packages(),  # Encontrar automaticamente todos os pacotes
    install_requires=[  # Dependências
        # Liste aqui outras bibliotecas que seu pacote precisa
    ],
    entry_points={
        "console_scripts": [
            "meu-comando=meu_pacote.modulo:main",  # Se quiser criar um comando de terminal
        ],
    },
    author="Seu Nome",  # Seu nome
    author_email="seu.email@example.com",  # Seu email
    description="Uma breve descrição do pacote",
    long_description=open("README.md").read(),  # Descrição longa (usualmente do README)
    long_description_content_type="text/markdown",
    url="https://github.com/seu_usuario/meu_pacote",  # URL do seu repositório
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Versão mínima do Python
)
