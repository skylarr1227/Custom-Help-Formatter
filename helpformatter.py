import discord
from discord.ext import commands

class Help:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='help', aliases=['h'])
    async def _help(self, ctx, command: str=None):
        pref = '```\n'
        postf = '\n```'
        result = ''
        if command is None:
            li = [cog[0] for cog in self.bot.cogs.items()]
            for smth in li:
                s = self.bot.get_cog_commands(smth)
                result += list(s)[0].cog_name + ':\n' + '    '.join('\n    {} - {}\n'.format(c.name, c.help) for c in list(s)) + '\n'
            await ctx.send(pref + result + postf)
        else:
            if command not in self.bot.all_commands:
                if command not in self.bot.cogs:
                    await ctx.send('That command or cog does not exist!')
                else:
                    the_cog = list(self.bot.get_cog_commands(command))
                    result += the_cog[0].cog_name + ':\n'
                    for cmd in the_cog:
                        result += ''.join('\n    {} - {}\n'.format(cmd.name, cmd.help)) + '\n'
                    await ctx.send(pref + result + postf)
            else:
                cmd = self.bot.get_command(command)
                # helptext = ' '.join('[{}]'.format(cmd) for (cmd, param) in dict(cmd.clean_params).items())
                # result += '' + cmd.name + ' ' + helptext + '\n\n    ' + cmd.help + '\n'
                result += cmd.signature + '\n\n    ' + cmd.help + '\n'
                await ctx.send(pref + result + postf)

def setup(bot):
    bot.add_cog(Help(bot))
