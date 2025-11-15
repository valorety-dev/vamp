import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Bot setup
intents = discord.Intents.default()
intents.message_content = True
intents.members = True  # For member management
intents.guilds = True
bot = commands.Bot(command_prefix='!', intents=intents, help_command=None)  # Disable default help

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    print(f'Bot is in {len(bot.guilds)} guilds')

# Kick Command
@bot.command(name='kick')
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member = None, *, reason: str = "No reason provided"):
    """Kick a member from the server"""
    if not member:
        embed = discord.Embed(description="Please mention a user to kick", color=0xFF4444)
        await ctx.send(embed=embed)
        return
    
    if member.id == ctx.author.id:
        embed = discord.Embed(description="You cannot kick yourself", color=0xFF4444)
        await ctx.send(embed=embed)
        return
    
    if member.top_role >= ctx.author.top_role:
        embed = discord.Embed(description="You don't have permission to kick this member", color=0xFF4444)
        await ctx.send(embed=embed)
        return
    
    try:
        await member.kick(reason=reason)
        embed = discord.Embed(
            title="Member Kicked",
            description=f"**{member.mention}** has been kicked from the server",
            color=0x5865F2
        )
        embed.add_field(name="Reason", value=reason, inline=False)
        embed.set_footer(text=f"Moderator: {ctx.author.name}", icon_url=ctx.author.avatar.url if ctx.author.avatar else None)
        await ctx.send(embed=embed)
    except Exception as e:
        embed = discord.Embed(description=f"⚠️ Failed: {str(e)}", color=0xFF0000)
        await ctx.send(embed=embed)

# Ban Command
@bot.command(name='ban')
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member = None, *, reason: str = "No reason provided"):
    """Ban a member from the server"""
    if not member:
        embed = discord.Embed(description="Please mention a user to ban", color=0xFF4444)
        await ctx.send(embed=embed)
        return
    
    if member.id == ctx.author.id:
        embed = discord.Embed(description="You cannot ban yourself", color=0xFF4444)
        await ctx.send(embed=embed)
        return
    
    if member.top_role >= ctx.author.top_role:
        embed = discord.Embed(description="You don't have permission to ban this member", color=0xFF4444)
        await ctx.send(embed=embed)
        return
    
    try:
        await member.ban(reason=reason)
        embed = discord.Embed(
            title="Member Banned",
            description=f"**{member.mention}** has been permanently banned",
            color=0xFF4444
        )
        embed.add_field(name="Reason", value=reason, inline=False)
        embed.set_footer(text=f"Moderator: {ctx.author.name}", icon_url=ctx.author.avatar.url if ctx.author.avatar else None)
        await ctx.send(embed=embed)
    except Exception as e:
        embed = discord.Embed(description=f"⚠️ Failed: {str(e)}", color=0xFF0000)
        await ctx.send(embed=embed)

# Unban Command
@bot.command(name='unban')
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member_name: str = None):
    """Unban a user from the server"""
    if not member_name:
        embed = discord.Embed(description="⚠️ Provide username", color=0xFF0000)
        await ctx.send(embed=embed)
        return
    
    banned_users = [entry async for entry in ctx.guild.bans()]
    
    for ban_entry in banned_users:
        user = ban_entry.user
        if f"{user.name}#{user.discriminator}" == member_name or str(user.name) == member_name:
            try:
                await ctx.guild.unban(user)
                embed = discord.Embed(
                    title="Member Unbanned",
                    description=f"**{user.mention}** has been unbanned",
                    color=0x43B581
                )
                embed.set_footer(text=f"Moderator: {ctx.author.name}", icon_url=ctx.author.avatar.url if ctx.author.avatar else None)
                await ctx.send(embed=embed)
                return
            except Exception as e:
                embed = discord.Embed(description=f"⚠️ Failed: {str(e)}", color=0xFF0000)
                await ctx.send(embed=embed)
                return
    
    embed = discord.Embed(description="⚠️ User not found in ban list", color=0xFF0000)
    await ctx.send(embed=embed)

# Mute Command (timeout)
@bot.command(name='mute')
@commands.has_permissions(moderate_members=True)
async def mute(ctx, member: discord.Member = None, duration: int = 5, *, reason: str = "No reason provided"):
    """Timeout (mute) a member"""
    if not member:
        embed = discord.Embed(description="⚠️ Mention a user to mute", color=0xFF0000)
        await ctx.send(embed=embed)
        return
    
    if member.id == ctx.author.id:
        embed = discord.Embed(description="⚠️ Cannot mute yourself", color=0xFF0000)
        await ctx.send(embed=embed)
        return
    
    if member.top_role >= ctx.author.top_role:
        embed = discord.Embed(description="⚠️ Insufficient permissions", color=0xFF0000)
        await ctx.send(embed=embed)
        return
    
    try:
        import datetime
        timeout_duration = datetime.timedelta(minutes=duration)
        await member.timeout(timeout_duration, reason=reason)
        embed = discord.Embed(
            title="Member Muted",
            description=f"**{member.mention}** has been muted",
            color=0xFAA61A
        )
        embed.add_field(name="Duration", value=f"{duration} minutes", inline=True)
        embed.add_field(name="Reason", value=reason, inline=True)
        embed.set_footer(text=f"Moderator: {ctx.author.name}", icon_url=ctx.author.avatar.url if ctx.author.avatar else None)
        await ctx.send(embed=embed)
    except Exception as e:
        embed = discord.Embed(description=f"⚠️ Failed: {str(e)}", color=0xFF0000)
        await ctx.send(embed=embed)

# Unmute Command
@bot.command(name='unmute')
@commands.has_permissions(moderate_members=True)
async def unmute(ctx, member: discord.Member = None):
    """Remove timeout (unmute) a member"""
    if not member:
        embed = discord.Embed(description="⚠️ Mention a user to unmute", color=0xFF0000)
        await ctx.send(embed=embed)
        return
    
    try:
        await member.timeout(None)
        embed = discord.Embed(
            title="Member Unmuted",
            description=f"**{member.mention}** has been unmuted",
            color=0x43B581
        )
        embed.set_footer(text=f"Moderator: {ctx.author.name}", icon_url=ctx.author.avatar.url if ctx.author.avatar else None)
        await ctx.send(embed=embed)
    except Exception as e:
        embed = discord.Embed(description=f"⚠️ Failed: {str(e)}", color=0xFF0000)
        await ctx.send(embed=embed)

# Server Stats Command
@bot.command(name='stats')
async def stats(ctx):
    """Display server statistics"""
    guild = ctx.guild
    
    # Count members by status
    online = sum(1 for m in guild.members if m.status == discord.Status.online)
    bots = sum(1 for m in guild.members if m.bot)
    humans = guild.member_count - bots
    
    embed = discord.Embed(
        title=f"{guild.name} Stats",
        color=0x5865F2
    )
    embed.set_thumbnail(url=guild.icon.url if guild.icon else None)
    
    embed.add_field(name="Members", value=f"**{guild.member_count}** total\n**{humans}** humans\n**{bots}** bots", inline=True)
    embed.add_field(name="Online", value=f"**{online}** members", inline=True)
    embed.add_field(name="\u200b", value="\u200b", inline=True)
    embed.add_field(name="Channels", value=f"**{len(guild.text_channels)}** text\n**{len(guild.voice_channels)}** voice", inline=True)
    embed.add_field(name="Owner", value=guild.owner.mention, inline=True)
    embed.add_field(name="Created", value=guild.created_at.strftime('%b %d, %Y'), inline=True)
    
    await ctx.send(embed=embed)

# Clear Messages Command
@bot.command(name='clear')
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int = 5):
    """Delete a specified number of messages"""
    if amount < 1 or amount > 100:
        embed = discord.Embed(description="⚠️ Amount must be 1-100", color=0xFF0000)
        await ctx.send(embed=embed)
        return
    
    try:
        deleted = await ctx.channel.purge(limit=amount + 1)
        embed = discord.Embed(
            title="Messages Cleared",
            description=f"Successfully deleted **{len(deleted) - 1}** messages",
            color=0x5865F2
        )
        msg = await ctx.send(embed=embed)
        
        import asyncio
        await asyncio.sleep(3)
        await msg.delete()
    except Exception as e:
        embed = discord.Embed(description=f"⚠️ Failed: {str(e)}", color=0xFF0000)
        await ctx.send(embed=embed)

# Help Command
@bot.command(name='help', aliases=['vamp', 'commands'])
async def vamphelp(ctx):
    """Display help information"""
    embed = discord.Embed(
        title="VAMP Bot Commands",
        description="Powerful moderation bot for your server",
        color=0x5865F2
    )
    
    embed.add_field(
        name="Moderation Commands",
        value=(
            "`!kick @user [reason]` - Kick a member\n"
            "`!ban @user [reason]` - Ban a member\n"
            "`!unban username` - Unban a user\n"
            "`!mute @user <min> [reason]` - Timeout a member\n"
            "`!unmute @user` - Remove timeout\n"
            "`!clear <amount>` - Delete messages"
        ),
        inline=False
    )
    embed.add_field(
        name="Utility Commands",
        value="`!stats` - Server statistics\n`!help` - Show this message",
        inline=False
    )
    embed.set_footer(text="Requires moderator permissions to use commands")
    await ctx.send(embed=embed)

# Error handling
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(description="Missing required argument", color=0xFF4444)
        await ctx.send(embed=embed)
    elif isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(description="You don't have permission to use this command", color=0xFF4444)
        await ctx.send(embed=embed)
    elif isinstance(error, commands.CommandNotFound):
        pass
    else:
        embed = discord.Embed(description=str(error), color=0xFF4444)
        await ctx.send(embed=embed)
        print(f"Error: {error}")

# Run the bot
if __name__ == "__main__":
    token = os.getenv('DISCORD_TOKEN')
    if not token:
        print("❌ Error: DISCORD_TOKEN not found in environment variables!")
        print("Please create a .env file with your Discord bot token.")
        exit(1)
    
    bot.run(token)
