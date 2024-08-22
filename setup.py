from setuptools import setup, find_packages

setup(
    name="pygame_alglin",  # Nome do pacote
    version="0.1.0",  # Versão do pacote
    packages=find_packages(),  # Encontrar automaticamente todos os pacotes
    install_requires=[  # Dependências
        # Liste aqui outras bibliotecas que seu pacote precisa
    ],
    package_data={
        '': ['pygame_alglin\img\a.png',
             'pygame_alglin\img\dardo.png',
             'pygame_alglin\img\ima.png',
             'pygame_alglin\img\iman.png',
             'pygame_alglin\img\parqu.png',
             'pygame_alglin\img\red.png',
             'pygame_alglin\img\redsprite.png'
             ]     # Inclui todos os arquivos .png dentro do diretório 'img' de todos os pacotes
    },
    entry_points={
        "console_scripts": [
            "pygame_alglin=pygame_alglin.main:main",  # Se quiser criar um comando de terminal
        ],
    },
    author="Felipe e Vinicius",  # Seu nome
    author_email="felipemf2@al.insper.edu.br e vinileal2005@gmail.com",  # Seu email
    description="Em um jogo desafiador de física, o jogador deve lançar um dardo para acertar um balão em um cenário que contém tanto um campo gravitacional quanto um campo magnético. Cada lançamento requer estratégia e precisão, já que os campos afetam a trajetória do dardo de maneiras distintas, tornando cada nível único e progressivamente mais difícil. O objetivo é acertar o balão com o menor número de tentativas possível, superando as forças naturais que desviam o curso do dardo.",
    long_description=open("README.md").read(),  # Descrição longa (usualmente do README)
    long_description_content_type="text/markdown",
    url="https://github.com/felipemarianoferr/pygame_alglin.git",  # URL do seu repositório
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Versão mínima do Python
)
