# LuaBot - Instruções para o Claude

## Sobre o Projeto
A LuaBot é uma bot do Discord que utiliza **discord.py**, ela foi feita por diversão, mas ela tem diversos comandos para moderar e automoderar o servidor(Caramelo System).

Além disso, a LuaBot tem uma personalidade de uma Shihtzu brincalhona.

## Stack

- Python **3.11+**
- Discord.py
- Banco de Dados usando MongoDB

## Estrutura de Pastas

```
caramelo/
    blacklist/
        blacklist.py   Sistema de Blacklist da LuaBot
    caramelo.py   Comandos de AutoMod/Mod da LuaBot
    README.md

command/
    dev/
        shutdown.py   Comando de desligar a LuaBot
        performance   Comando de ver a Performance da LuaBot
        restart.py    Comando de reiniciar a LuaBot
    infos/
        botinfo.py   Comando de ver a info da LuaBot
        perfil.py    Comando de ver o perfil do Usuário
        userinfo.py  Comando de ver a info do usuário

    roleplay/
        abraco.py  Comando de roleplay: abraço
        beijar.py  Comando de roleplay: beijar

    commands_assets/
        Imagens dos comando que usam imagem

    database/
        database.py  Lógica da DB da LuaBot
    
    shih/
        shih_manager.py  Lógica de proteger o ".env".

    utils/
        isGestor.py  Verifica se é gestor da Loja da LuaBot

    blacklisted_users.json  Usuários banidos da LuaBot
    docker-compose.yml      Docker Compose da LuaBot 
    Dockerfile              Docker da LuaBot
    (O Docker é utilizado apenas no GitHub)

    main.py           Arquivo principal da LuaBot
    requirements.txt  libs da LuaBot
```
## Padrões de código
- Sempre usar async/await (nunca código síncrono em eventos)
- Não usar cogs.
- Prefixo de comandos: `/` (slash command)
- Tratar erros com `on_command_error`
- Variáveis de ambiente via `python-dotenv` (nunca hardcodar tokens)

## Comandos úteis
- Rodar o bot: `python main.py`
- Instalar dependências: `pip install -r requirements.txt`
