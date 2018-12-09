import discord
from discord.ext import commands

class Help:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='help', aliases=['h'])
    async def _help(self, ctx, *, command = None):
        pref = '```\n'
        postf = f'\nGet info on a command group, category or just a command with @{self.bot.user.name}#{self.bot.user.discriminator} help <Category>/<Command>/<Command group> or *help <Category>/<Command>/<Command group>```'
        result = ''
        postfix = '\n```'
        if command is None:
            li = [cog[0] for cog in self.bot.cogs.items()]
            for smth in li:
                if smth != 'Help' and smth != 'OwnerCog':
                    s = list(self.bot.get_cog_commands(smth))
                    result += "{}:\n{}".format(s[0].cog_name, '    '.join('\n    {} - {}\n'.format(c.name, c.help) for c in s))
            await ctx.send("{}{}{}".format(pref, result, postf))
        else:
            if command not in self.bot.all_commands:
                if command not in self.bot.cogs:
                    cmd = self.bot.get_command(command)
                    if cmd:
                        result += "{}\n\n    {}".format(cmd.signature, cmd.help)
                        await ctx.send("{}{}{}".format(pref, result, postfix))
                    else:
                        result = 'That command/category/command group does not exist!'
                        await ctx.send(result)
                else:
                    the_cog = list(self.bot.get_cog_commands(command))
                    result += "{}:\n".format(the_cog[0].cog_name)
                    for cmd in the_cog:
                        result += ''.join('\n    {} - {}\n'.format(cmd.name, cmd.help))
                    await ctx.send("{}{}{}".format(pref, result, postfix))
            else:
                cmd = self.bot.get_command(command)
                # helptext = ' '.join('[{}]'.format(cmd) for (cmd, param) in dict(cmd.clean_params).items())
                # result += '' + cmd.name + ' ' + helptext + '\n\n    ' + cmd.help + '\n'
                result += "{}\n\n    {}".format(cmd.signature, cmd.help)
                await ctx.send("{}{}{}".format(pref, result, postfix))

def setup(bot):
    bot.add_cog(Help(bot))
